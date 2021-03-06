from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setup(
    name="medLayer",
    version="0.0.1",
    author="Duc Dang",
    author_email="vinhduc91@outlook.com",
    description="Medical events library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/medasmarathon/MeLayer",
    project_urls={
        "Bug Tracker": "https://github.com/medasmarathon/MeLayer/issues",
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    packages=find_packages(exclude=['example*', '*constant*']),
    python_requires=">=3.6",
    install_requires=[]
    )
