from setuptools import setup
from typing import List

# declaring variable for setup functions
PROJECT_NAME = "housing-predictor-project"
VERSION="0.0.2"
AUTHOR="Khushboo Singh"
DESCRIPTION="This is the first ML PROJECT"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_reuirements_list()->List[str]:
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_reuirements_list()
)