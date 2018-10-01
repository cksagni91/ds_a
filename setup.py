"""
Pythonish makefile for the project
"""

from distutils.cmd import Command
import subprocess
from setuptools import setup, find_packages

__version__ = "0.1"


class CodeCheck(Command):
    """Custom setup.py command to run code checking tools"""
    user_options = []

    def initialize_options(self):
        """Initialize options for this command"""
        pass

    def finalize_options(self):
        """Finalize options for this command"""
        pass

    def run(self):
        """Execute command and raise exception in case of failure"""
        return_value = subprocess.call('./codecheck.sh')
        if return_value:
            raise Exception('Code is not pure!')


setup(
    name="DSA",
    version=__version__,

    packages=find_packages(where=".", exclude=["tests", "tests.*"]),

    include_package_data=True,
    exclude_package_data={"": ["*.txt"]},

    install_requires=[],

    setup_requires=["setuptools-pep8", "setuptools-lint"],

    author="Chandan Kumar",
    author_email="chandanagni91@gmail.com",
    description="Python package containing algo and ds implementation",
    long_description="Python package containing algo and ds implementation",

    project_urls={
        "Source Code": "https://github.com/cksagni91/ds_a.git",
    },

    test_suite="tests",
    cmdclass={'code_check': CodeCheck}
)
