from setuptools import setup

setup(name='jlem',
      version='0.1',
      description='Jupyter lab extension manager',
      packages=['jlem'],
      entry_points = {
          'console_scripts': ['jlem=jlem.main:main']
      },
      install_requires=['jupyterlab'])
