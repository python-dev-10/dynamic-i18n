from setuptools import setup, find_packages
import os
import codecs
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'A basic dynamic class to support I18N translation from JSON'

project_urls = {
  'Link 1': 'https://mygreatsite.com',
}
setup(
    name="dynamic_i18n",
    version=VERSION,
    author="Jeferson-Peter (Jeferson Peter)",
    author_email="jeferson.peter@pm.me",
    description=DESCRIPTION,
    url='https://github.com/Jeferson-Peter/dynamic-i18n',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['Python', 'I18N', 'Translation', 'Dynamic Class', 'Flatten Json'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

# Setting up
