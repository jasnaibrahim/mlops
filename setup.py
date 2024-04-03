from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    """
     function will return requirements
    """
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("/n","")for req in requirements]
    return requirements
setup(

    name="mlproject",
    version="0.0.1",
    author="jasnacp",
    author_email="jasna@123",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
)
