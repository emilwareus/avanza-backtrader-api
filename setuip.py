  
#!/usr/bin/env python

import ast
import re
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('avanza_backtrader_api/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='avanza-backtrader-api',
    version=version,
    description='Avanza API within backtrader',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Emil Wåreus',
    author_email='emil.wareus47@gmail.com',
    url='https://github.com/emilwareus/avanza-backtrader-api',
    keywords='financial,timeseries,api,trade,backtrader',
    packages=['avanza_backtrader_api'],
    install_requires=[
        'backtrader',
        'smaland',
    ],
    tests_require=[
        'pytest',
        ],
    setup_requires=[],
)