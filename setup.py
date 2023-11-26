#Dieser Codeteil ist aus dem Beispiel aus der Vorlesung entnommen und wurde für die Zwecke des Projektes angepasst.

from setuptools import setup, find_packages

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory+'ReadMe.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    author="Mehmet Karaca",
    author_email="Karaca.Mehmet@outlook.de",
    package_dir={'': 'src'},
    install_requires=['pyspark'],
)