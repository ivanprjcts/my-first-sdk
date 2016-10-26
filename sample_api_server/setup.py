import os
from setuptools import setup, find_packages


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


EXCLUDE_FROM_PACKAGES = []


setup(
    name='sample_api_server',
    version='0.1',
    description='Sdklib Api Sample',
    author='Ivan Martin',
    author_email='ivanprjcts@gmail.com',
    url='https://github.com/ivanprjcts/my-first-sdk',
    install_requires=read_file('requirements.txt').splitlines(),
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Framework :: Django :: 1.10',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    py_modules=["manage"],
    include_package_data=True,
    zip_safe=False
)
