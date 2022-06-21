from setuptools import setup, find_packages
from pathlib import Path
from os import path


datapath = Path(__file__).parent.resolve()

with open(datapath / "README.md", encoding="utf8") as file:
    long_description = file.read()

setup(
    name='GraphCalculator',
    version='0.0.1',
    author='Ildar Kharrasov, Stanislav Kitaev, Anastasia Mazurenko',
    author_email='kharrasov.radiokha94@yandex.ru',
    description='Python3 project',
    long_description=long_description,
    packages=find_packages(),
    url='https://github.com/darioradio1man/python-cmc-msu',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'matplotlib==3.1.0',
        'numpy==1.22.0',
        'networkx==2.3',
        'flake8-per-file-ignores==0.8.1',
    ],
    package_data={'': '*'},
    include_package_data=False,
    setup_require=["mo_installer"],
    #locale_src="./GraphCalculator/locale/ru/LC_MESSAGES",
),
