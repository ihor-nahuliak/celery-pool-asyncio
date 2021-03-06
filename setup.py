#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

long_description = '\n\n'.join((
    readme,
    history,
))

requirements = [
    'celery',
    'asgiref',
]

setup_requirements = [
    'setuptools>=38.6.0',
]


setup(
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Celery pool to run coroutine tasks",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    include_package_data=True,
    keywords='celery_pool_asyncio',
    name='celery-pool-asyncio',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    #tests_require=test_requirements,
    url='https://github.com/kai3341/celery-pool-asyncio',
    version='0.1.9',
    zip_safe=True,
)
