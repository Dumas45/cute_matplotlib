import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cute_matplotlib-dumas45",
    version="0.0.1",
    author="Dumas45",
    # author_email="author@example.com",
    description="Helper functions for matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dumas45/cute_matplotlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
