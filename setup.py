# -*- coding: utf-8 -*-
from os import path
from codecs import open as codecs_open
from setuptools import setup, find_packages

CURRENT_PATH = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs_open(path.join(CURRENT_PATH, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='lel-lang',

    version='0.0.6',

    description='Lel programming language(Lisp-esque language)',
    long_description=LONG_DESCRIPTION,

    url='https://github.com/osaatcioglu/Lisp-esque-language',

    author='Ömer Saatcioglu',
    author_email='osaatcioglu@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Compilers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='compiler lisp lel parser ast tokenize',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['six', 'py-require'],

    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={},

    entry_points={
        'console_scripts': [
            'pylel=pylel:package_main',
        ],
    },
)
