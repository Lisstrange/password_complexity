"""Shim for local package installation in editable mode."""

# import setuptools

from setuptools import setup, find_packages
setup(
   name='password_comp',
   version='0.1.0',
   description='Model to predict password frequency',
   author='Lisovik Nikita',
   author_email='nikita.a.lisovik@gmail.com',
   packages=find_packages(),  #find all packages   
   # We can commit this setup and use setup config instead
)

# setuptools.setup()
