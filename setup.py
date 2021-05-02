from setuptools import setup, find_packages

config = {
  "name": "naturalinput",
  "description": "Description goes here.",
  "author": "Nickunj Chopra (NerdvanaNC)",
  "url": "the project URL",
  "download_url": "probably git repo or smth",
  "author_email": "nickunjchopra@gmail.com",
  "version": "0.1",
  "install_requires": ['pytest'],
  "packages": find_packages(exclude=('tests', 'docs')),
  "scripts": []
}

setup(**config)