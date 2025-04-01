import os
from pathlib import Path

from setuptools import setup, find_packages
from os.path import join, dirname, realpath

__version__ = '0.0.1'


requirements_files = ['requirements.txt']
requirements_path = join(dirname(realpath(__file__)), 'requirements')
setup_path = Path(__file__).parent

requirements = []

for file_name in requirements_files:
    with open(join(requirements_path, file_name), "r") as f:
        requirements.append(f.readlines())

setup(
    name="model-registry",
    version=__version__,
    description='ModelRegistry',
    url='https://github.com/ErickSeo/insider-libs',
    maintainer='',
    maintainer_email='',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[],
    install_requires=requirements,
    extras_require={},
    python_requires=">=3.9",
    classifiers=[
        'Programming Language :: Python :: 3.9'
    ],
)