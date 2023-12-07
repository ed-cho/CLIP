import os

from packaging.requirements import Requirement
from setuptools import setup, find_packages

requirements = [requirement.strip() for requirement in open(os.path.join(os.path.dirname(__file__), "requirements.txt")).readlines()]

setup(
    name="clip",
    py_modules=["clip"],
    version="1.0",
    description="",
    author="OpenAI",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(Requirement(r))
        for r in requirements
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
