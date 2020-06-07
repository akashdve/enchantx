import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EnchantX", # Replace with your own username
    version="0.1",
    author="AkashD",
    author_email="akashdave555@gmail.com",
    description="An extension of PyEnchant Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akashdve/enchantx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)