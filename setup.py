#Basic setup for the package.

from setuptools import setup, find_packages

setup(
    name="linvulnscan",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'run_scan=linvulnscan:run_scan',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for scanning Linux vulnerabilities and testing privilege escalation vectors.",
    url="https://github.com/yourusername/linvulnscan",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)

