from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:
    requirement_lst:List[str] = []
    try:
        with open("requirments.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except Exception as e:
        print("requirements.txt file not found")

    
    return requirement_lst

setup(
    name="NetworkSecruity",
    version="0.0.1",
    author="vipin kumar",
    author_email="vipinmemon8123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

print(get_requirements)