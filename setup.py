from setuptools import find_packages, setup

with open('README.rst', 'r') as readme_fd:
    long_description = readme_fd.read()

setup(
    name='dynamorm',
    version='0.0.9',
    description='DynamORM is a Python object relation mapping library for Amazon\'s DynamoDB service.',
    long_description=long_description,
    author='Evan Borgstrom',
    author_email='evan@borgstrom.ca',
    url='https://github.com/NerdWallet/DynamORM',
    license='Apache License Version 2.0',

    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'boto3>=1.3,<1.4',
        'pytest>=2.9,<3.0',
        'six',
    ],
    packages=find_packages('.', exclude=['tests', 'docs']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries'
    ]
)
