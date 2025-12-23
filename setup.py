from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements file and returns a list of dependencies."""
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Jay Khandelwal',
    author_email="jaykh7777@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

