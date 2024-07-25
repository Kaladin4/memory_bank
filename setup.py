from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="memory-bank",
    version="0.1.0",
    author="Francisco Garófalo Jerez",
    author_email="dalinargarofalo@gmail.com",
    description="A simple Python library for managing chat message history in langchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kaladin4/memory_bank",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        "langchain-core",
    ],
    extras_require={
        "dev": [
            "langchain-anthropic",
            "python-dotenv",
        ],
    },
)
