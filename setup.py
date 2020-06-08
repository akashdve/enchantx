import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EnchantX",
    version="0.1",
    author="AkashD",
    author_email="akashdave555@gmail.com",
    description="An extension of PyEnchant Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akashdve/enchantx",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    platforms="Posix; MacOS X; Windows",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        "GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["pyenchant>=3.0.1"],
)