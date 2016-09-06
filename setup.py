from setuptools import setup


about = {}
with open('wakadump/__about__.py') as f:
    exec(f.read(), about)


packages = [
    about['__title__'],
]

install_requires = [x.strip() for x in open('requirements.txt').readlines()]

setup(
    name=about['__title__'],
    version=about['__version__'],
    license=about['__license__'],
    description=about['__description__'],
    long_description=open('README.rst').read(),
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_dir={about['__title__']: about['__title__']},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['wakadump = wakadump.cli:main'],
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
