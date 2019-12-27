import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PiHole-api',
    version='2.0',
    description='A python3 wrapper for the pihole api that aims to eventually be a full replacement for the AdminLTE web panel',
    url='https://github.com/sfoerster/PiHole-api',
    author='Steven Foerster',
    author_email='sfoerster@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ),
)
