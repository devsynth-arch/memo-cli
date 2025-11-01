
from setuptools import setup, find_packages

setup(
    name="memo-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Save and run your favorite shell commands.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/memo",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "memo = memo.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
