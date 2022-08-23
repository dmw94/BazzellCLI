from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'BazzellCLI',
    version = '1.0.0',
    author = 'dmw94',
    license = 'GPLv3',
    description = 'BazzellCLI brings IntelTechniques Search Tools to the command line.',
    url = 'https://github.com/dmw94/BazzellCLI',
    py_modules = ['bazzellCLI'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        bazzellCLI=bazzellCLI:cli
    '''
)