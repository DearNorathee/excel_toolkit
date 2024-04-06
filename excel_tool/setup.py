from setuptools import setup, find_packages

setup(
    author= "Dear Norathee",
    description="package to help you automate Excel files' tasks",
    name="excel_tool",
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    requires=["xlwings"]

)