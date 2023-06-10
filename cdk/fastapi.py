from aws_cdk import Stack
from constructs import Construct

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecs_patterns
from aws_cdk import CfnOutput, Duration

class FastAPIStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # Create VPC
        vpc = ec2.Vpc(self, "FastAPIYOLOVv5VPC", max_azs=1)

        # Create Fargate Cluster
        ecs_cluster = ecs.Cluster(
            self,
            "FastAPIYOLOVv5ECSCluster",
            vpc=vpc,
        )
        
        # Create Security Group to restrict access to the FastAPI service from a specific IP mask

        # MBARI IP mask
        ip_mask = '134.89.0.0/0'

        # Create a security group
        security_group = ec2.SecurityGroup(
            self, 'MBARIFastAPISecurityGroup', vpc=vpc,
            allow_all_outbound=True
        )

        # Allow inbound access from the specified IP mask
        security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4(ip_mask),
            connection=ec2.Port.tcp(80)
        )

        docker_image = ecs.ContainerImage.from_registry('mbari/fastapi-yolov5:1.0.1')

        # Configure health check on the load balancer
        # listener.add_targets('FastAPIYOLOVv5Target',
        #                      port=80,
        #                      targets=[ecs_service],
        #                      health_check=health_check)
        # Create Fargate Service and ALB
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ecs_patterns/ApplicationLoadBalancedTaskImageOptions.html
        image_options = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=docker_image,
            container_port=80,
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
            security_groups=[security_group]

        )

        self.ecs_service.target_group.configure_health_check(
            path="/health",
            healthy_http_codes="200-299",
            healthy_threshold_count=2,
            unhealthy_threshold_count=2,
            interval=Duration.seconds(60),
            timeout=Duration.seconds(5),
        )