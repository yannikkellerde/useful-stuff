from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

setup(
    name="useful_stuff",
    version="0.1.0",
    description="some python scripts that I find useful",
    author="Yannik Keller",
    author_email="",
    packages=["cl_tools"],
    entry_points={
        "console_scripts": ["replace-map=cl_tools.replacements_map:replacements_map"]
    },
)
