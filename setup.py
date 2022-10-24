import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PYSF',
    url='https://github.com/awesomelewis2007/PYSF/',
    author='awesomelewis2007',
    packages=['PYSF'],
    install_requires=[''],
    version="0.1",
    license='GNU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='A project similar to Metasploit but made in python and not just exploits.'
)
