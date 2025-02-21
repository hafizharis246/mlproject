from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """Returns a list of requirements from a requirements file."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]


setup(
    name='mlproject',
    version='0.0.1',
    author= "Haris",
    author_email= "harismehmood948@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)