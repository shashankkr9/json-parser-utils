import io

import setuptools


def readme():
    with io.open('README.md', 'r', encoding='utf8') as f:
        return f.read()


setuptools.setup(
    name='json-parser-utils',
    version='0.0.0',
    author="Shashank Kumar",
    author_email="shashank.kr9@gmail.com",
    description="A python package that makes it easier to access nested json data",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/shashankkr9/json-parser-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
