from setuptools import setup, find_packages
from codecs import open
from os import path
import os
import re
import io


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='poppunk',
    version=find_version("PopPUNK/__init__.py"),
    description='PopPUNK (POPulation Partitioning Using Nucleotide Kmers)',
    long_description=long_description,
    url='https://github.com/mgalardini/pyseer',
    author='John Lees and Nicholas Croucher',
    author_email='john@johnlees.me',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='bacteria genomics population-genetics k-mer',
    packages=['PopPUNK'],
    entry_points={
        "console_scripts": [
            'poppunk = PopPUNK.__main__:main'
            ]
    },
    install_requires=['numpy',
                      'scipy',
                      'statsmodels',
                      'scikit-learn',
                      'DendroPy',
                      'pymc3',
                      'theano',
                      'networkx',
                      'matplotlib'],
    test_suite="test",
)