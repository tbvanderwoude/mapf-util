import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mapf-util",
    version="0.0.1",
    author="Thom van der Woude",
    author_email="tbvanderwoude@student.tudelft.nl",
    description="MAPF utility classes used by other packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tbvanderwoude/mapf-util",
    project_urls={
        "Bug Tracker": "https://github.com/tbvanderwoude/mapf-util/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
