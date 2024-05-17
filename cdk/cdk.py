# !/usr/bin/env python
__author__ = "Danelle Cline"
__copyright__ = "Copyright 2023, MBARI"
__credits__ = ["MBARI"]
__license__ = "GPL"
__maintainer__ = "Danelle Cline"
__email__ = "dcline at mbari.org"
__doc__ = '''

Scalable deployment of YOLOv5 model

@author: __author__
@status: __status__
@license: __license__
'''
import datetime as dt
import yaml
import os
from fastapi import FastAPIStack
from aws_cdk import (
    App, Environment
)

app = App()

# Import project config from CDK_STACK_CONFIG environment variable
if 'CDK_STACK_CONFIG' not in os.environ:
    raise ValueError("CDK_STACK_CONFIG environment variable not set")

with open(os.environ['CDK_STACK_CONFIG'], 'r') as stream:
    config = yaml.safe_load(stream)

deletion_date = (dt.datetime.utcnow() + dt.timedelta(days=90)).strftime('%Y%m%dT%H%M%SZ')

# Tagging; these are used to track costs and for lifecycle management
# Replace with your own tags
tag_dict = {'mbari:project-number': str(config['ProjectNumber']),
            'mbari:owner': config['Author'],
            'mbari:description': 'YOLOv5 detection model',
            'mbari:customer-project': str(config['ProjectNumber']),
            'mbari:stage': 'prod',
            'mbari:application': 'processing',
            'mbari:deletion-date': deletion_date,
            'mbari:created-by': config['Author']}

env = Environment(account=str(config['Account']), region=config['Region'])
print(env)
app = App()

FastAPIStack(app, "FastAPIYOLOv5Stack",
             env=env,
             tags=tag_dict,
             description=config['Description'], )
app.synth()
