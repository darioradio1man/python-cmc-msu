from setuptools import setup
from pathlib import Path
from os import path


datapath = Path(__file__).parent.resolve()

with open(datapath / "README.md") as file:
    long_decription = file.read()

setup(
    name='Graph calculator visualiser',
    version='0.0.1',
    author='Ildar Kharrasov, Stanislav Kitaev, Anastasia Mazurenko',
    author_email='kharrasov.radiokha94@yandex.ru',
    description='',
    long_decription=long_decription,
    url='https://github.com/darioradio1man/python-cmc-msu',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'matplotlib==3.1.0',
        'numpy==1.16.4',
        'networkx==2.3',
        'tkinter==8.6',
        'flake8-per-file-ignores==0.8.1',
    ],
)
