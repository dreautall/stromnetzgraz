import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stromnetzgraz",
    author="dreautall",
    author_email="michael@online-net.eu",
    description="Python client library for Stromnetz Graz API",
    keywords="stromnetz graz,power,api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dreautall/stromnetzgraz",
    project_urls={
        "Documentation": "https://github.com/dreautall/stromnetzgraz",
        "Bug Reports": "https://github.com/dreautall/stromnetzgraz/issues",
        "Source Code": "https://github.com/dreautall/stromnetzgraz",
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    package_data={"": ["*.crt"]},
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pyjwt"],
    extras_require={
        "dev": ["check-manifest"],
        # 'test': ['coverage'],
    },
)
