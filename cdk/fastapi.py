# !/usr/bin/env python
__author__ = "Danelle Cline"
__copyright__ = "Copyright 2024, MBARI"
__credits__ = ["MBARI"]
__license__ = "GPL"
__maintainer__ = "Danelle Cline"
__email__ = "dcline at mbari.org"
__doc__ = '''

Elastic YOLOv5 model deployed using AWS Fargate and AWS CDK

@author: __author__
@status: __status__
@license: __license__
'''

import yaml
import os
from aws_cdk import Stack
from constructs import Construct
from aws_cdk import (
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_ecs_patterns as ecs_patterns,
    aws_secretsmanager as secrets_manager,
)
from aws_cdk import CfnOutput, Duration
from app import __version__


class FastAPIStack(Stack):
    def __init__(
            self,
            scope: Construct,
            id: str,
            **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # Import project config from CDK_STACK_CONFIG environment variable
        if 'CDK_STACK_CONFIG' not in os.environ:
            raise ValueError("CDK_STACK_CONFIG environment variable not set")

        with open(os.environ['CDK_STACK_CONFIG'], 'r') as stream:
            config = yaml.safe_load(stream)

        # Cluster capacity
        min_capacity = config['MinCapacity']
        max_capacity = config['MaxCapacity']

        # Create VPC
        vpc = ec2.Vpc(self, "FastAPIYOLOVv5VPC", max_azs=2)

        # Create Fargate Cluster
        ecs_cluster = ecs.Cluster(
            self,
            "FastAPIYOLOVv5ECSCluster",
            vpc=vpc,
        )

        # Create Security Group to restrict access to the FastAPI service from a specific IP mask

        # MBARI IP mask up to 65,536 possible host addresses from the MBARI subnet
        ip_mask = '134.89.0.0/16'

        # Create a security group
        mbari_security_group = ec2.SecurityGroup(
            self, 'MBARIFastAPISecurityGroup', vpc=vpc,
            allow_all_outbound=True
        )

        # Allow inbound access from the specified IP mask
        mbari_security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4(ip_mask),
            connection=ec2.Port.tcp(80)
        )

        # Retrieve the AWS access key ID secret value from AWS Secrets Manager
        secret = secrets_manager.Secret.from_secret_name_v2(self, "MySecretID", secret_name="prod/s3download")

        docker_image = ecs.ContainerImage.from_registry(f'mbari/fastapi-yolov5:{__version__}')

        # Create Fargate Service and ALB
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ecs_patterns/ApplicationLoadBalancedTaskImageOptions.html
        image_options = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=docker_image,
            container_port=80,
            environment={
                "MODEL_WEIGHTS": config['MODEL_WEIGHTS'],
                "MODEL_LABELS": config['MODEL_LABELS'],
                "MODEL_DESCRIPTION": config['MODEL_DESCRIPTION'],
                "MODEL_INPUT_SIZE": str(config['MODEL_INPUT_SIZE']),
            },
            secrets={
                "AWS_ACCESS_KEY_ID": ecs.Secret.from_secrets_manager(secret, "AWS_ACCESS_KEY_ID"),
                "AWS_SECRET_ACCESS_KEY": ecs.Secret.from_secrets_manager(secret, "AWS_SECRET_ACCESS_KEY")
            }
        )

        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ecs_patterns/ApplicationLoadBalancedFargateService.html
        self.ecs_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "FastAPIYOLOv5Service",
            cluster=ecs_cluster,
            cpu=1024,
            memory_limit_mib=8192,
            desired_count=1,
            task_image_options=image_options,
            open_listener=False
        )

        # Get the ALB
        lb = self.ecs_service.load_balancer

        # Add the security group to the ALB
        lb.add_security_group(security_group=mbari_security_group)

        # Setup health check
        self.ecs_service.target_group.configure_health_check(
            path="/health",
            healthy_http_codes="200-299",
            healthy_threshold_count=2,
            unhealthy_threshold_count=2,
            interval=Duration.seconds(300),
            timeout=Duration.seconds(60),
        )

        # Increase scaling speed
        scaling = self.ecs_service.service.auto_scale_task_count(
            min_capacity=min_capacity,
            max_capacity=max_capacity,
        )

        scaling.scale_on_cpu_utilization('CpuScaling',
                                         target_utilization_percent=80,
                                         scale_in_cooldown=Duration.seconds(30),
                                         scale_out_cooldown=Duration.seconds(30),
                                         )
