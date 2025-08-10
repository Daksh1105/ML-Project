from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Return list of requirements from requirements.txt"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='myproject',
    version='0.0.1',
    author='Daksh',
    author_email='dakshg1105@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
