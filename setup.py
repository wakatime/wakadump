from setuptools import setup

from wakadump.__about__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)


packages = [
    __title__,
]

install_requires = [x.strip() for x in open('requirements.txt').readlines()]

setup(
    name=__title__,
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=open('README.rst').read(),
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    packages=packages,
    package_dir={__title__: __title__},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['wakadump = wakadump:main'],
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Text Editors',
    ),
)
