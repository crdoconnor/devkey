import codecs
import os
import re
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()

long_description = "\n" + "\n".join([read('PROJECT.txt'),
                                     read('docs', 'quickstart.rst')])

setup(name="keycom",
      version="0.1",
      description="A tool for running a suite of custom project commands with one key.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
#          'Programming Language :: Python :: 3',
#          'Programming Language :: Python :: 3.1',
#          'Programming Language :: Python :: 3.2',
#          'Programming Language :: Python :: 3.3',
      ],
      keywords='development environment tool',
      author='Colm O\'Connor',
      author_email='colm.oconnor.github@gmail.com',
      url='https://keycom.readthedocs.org/',
      license='MIT',
      install_requires=['argcomplete>=0.8.1'],
      packages=find_packages(exclude=["contrib", "docs", "tests*"]),
      package_data={},
      entry_points=dict(console_scripts=['k=keycom:interpreter.interpreter',]),
      zip_safe=False,
)
