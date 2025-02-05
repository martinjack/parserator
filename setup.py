import sys

try:
    from setuptools import setup
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")

reqs = [
    'future>=0.14.3',
    'lxml>=3.7.3',
    'python-crfsuite>=0.7',
    'chardet',
]

if sys.version < '3':
    reqs += ['backports.csv']


setup(
    version='0.7.0',
    url='https://github.com/martinjack/parserator',
    description='Create parsers',
    name='jackmartin.parserator',
    packages=['parserator'],
    install_requires=reqs,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis'],
    entry_points={
        'console_scripts': [
            'parserator = parserator.main:dispatch',
        ]
    }
)
