from setuptools import setup

setup(
    name="deadOrNot",
    version="0.1",
    install_requires=["colorama", "urllib3", "termcolor"],
    py_modules=["deadOrNot"],
    entry_points={"console_scripts": ["deadOrNot=deadOrNot"]},
)
