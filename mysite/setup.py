#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

setup(
    name = "user_messages_project",
    version = "1.0",
	install_requires=[
          'wsgi-basic-auth',
      ],
)