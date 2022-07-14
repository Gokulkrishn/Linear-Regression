import imp
from pytz import VERSION
from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    with open('requirements.txt') as f:
        return f.readlines()

PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Gokul"
DESCRIPTION="This is a housing price predictor project"
PACKAGES=["housing"]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),# PACKAGES ["housing"]
    install_requires=get_requirements_list()

)