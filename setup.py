from setuptools import setup, find_packages
from os import path

__version__ = '1.0.0'

here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name='airodb',
    version=__version__,
    description='A python project to persist the airodump-ng output to a mongo database.',
    url='https://github.com/jeremydumais/airodb',
    download_url='https://github.com/jeremydumais/airodb.git',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    author='Jeremy Dumais',
    install_requires=install_requires,
    author_email='jeremydumais@hotmail.com'
)