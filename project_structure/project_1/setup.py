from setuptools import setup, find_packages

from typing import List

HYPEN_DOT = '-e .'
def getRequirements( path:str ) ->List[str] :
    '''
    This function will read the requirements.txt file and return a list of requirements
    
    '''

    requirement = []
    with open(path) as f:
        requirement = f.readlines()
        requirement = [ req.replace( '\n' , "" ) for req in requirement ]
    
    if HYPEN_DOT in requirement:
        requirement.remove( HYPEN_DOT )

    return requirement


setup(
    name="my_first_project",  # Project name
    version="0.1.0",  # Initial version
    description="This is a short description of my project",

    long_description=open("README.md").read(),

    long_description_content_type="text/markdown",

    author="Pavan Kalyan",
    author_email="Kalyan@gmail.com",

    url="https://github.com/yourusername/my_project",  # repo or website
    license="MIT",

    packages=find_packages(),  # Automatically find packages inside project

    install_requires=getRequirements('./requirements.txt') ,

    python_requires=">=3.7",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={
        "console_scripts": [
            "mycli=my_package.module:main",  
            # command -> package.module:function
        ],
    },
)

