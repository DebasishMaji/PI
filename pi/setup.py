#!/usr/scripts/env python

from distutils.core import setup

setup(name='PI',
      version='1.0',
      description="Python Anomaly Detection Utilities",
      author="Debasish Maji",
      author_email="debasishmath92@gmail.com",
      url="https://github.com/DebasishMaji/PI",
      scripts=['scripts/anomaly_detector'],
      packages=['pi'],
      )

