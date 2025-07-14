from setuptools import setup, find_packages

setup(
    name="space-odyssey",
    version="1.0.0",
    description="A space-themed endless runner game built with Kivy",
    author="SpaceOdyssey Team",
    packages=find_packages(),
    install_requires=[
        "kivy>=2.1.0",
    ],
    entry_points={
        'console_scripts': [
            'space-odyssey=main:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)