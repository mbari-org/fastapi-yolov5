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
import json
from aws_cdk import App
from fastapi import FastAPIStack

app = App()

FastAPIStack(app, id="FastAPIStack")
app.synth()
