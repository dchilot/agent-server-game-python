#!/usr/bin/env python

import setuptools

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
    assert multiprocessing
except ImportError:
    pass

setuptools.setup(
    name='orwell.agent',
    version='0.0.1',
    description='Agent connecting to the game server.',
    author='',
    author_email='',
    packages=setuptools.find_packages(exclude="test"),
    test_suite='nose.collector',
    install_requires=['pyzmq', 'cliff'],
    tests_require=['nose', 'coverage', 'mock'],
    entry_points={
        'console_scripts': [
            'thought_police = orwell.agent.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.3'],
)
