from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.1'
DESCRIPTION = 'Ligature to roman urdu'
LONG_DESCRIPTION = 'This package allows you to convert urdu ligature to roman urdu'

# Setting up
setup(
    name="roman2urdu",
    version=VERSION,
    author="Amad durrani",
    author_email="<amadatiq786@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['urdu','roman_urdu','urdu_ligatures'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)