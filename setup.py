# coding: utf-8
"""
Setup module.
"""
from __future__ import absolute_import

# Third-party imports
from setuptools import find_packages
from setuptools import setup


setup(
    name='AoikProjectStarter',

    version='0.1.0',

    description=(
        'Python starter project that can tidy-lint-test code and build'
        ' documentation in one command.'
    ),

    long_description="""`Documentation on Github
<https://github.com/AoiKuiyuyou/AoikProjectStarter-Python>`_""",

    url='https://github.com/AoiKuiyuyou/AoikProjectStarter-Python',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='project starter',

    package_dir={
        '': 'src'
    },

    packages=find_packages('src'),

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'aoikprojectstarter=aoikprojectstarter.__main__:main',
        ],
    },
)
