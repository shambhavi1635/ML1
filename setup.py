from setuptools import find_packages, setup
from typing import List

e_dot = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will retrun the list of requiremnts
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if e_dot in requirements:
            requirements.remove(e_dot)

    return requirements


setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Shambhavi',
    author_email='shambhavisingh1635@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
