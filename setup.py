# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='qtpy_led',
      version='0.0.1',
      description='Simple LED widget for QyPt',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/crash8229/qtpy_led',
      author='crash8229',
      author_email='mu304007@gmail.com',
      license='MIT',
      packages=['qtpy_led'],
      install_requires=['numpy', 'pyautogui', 'QtPy'],
      zip_safe=False)
