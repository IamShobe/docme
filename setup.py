from setuptools import setup, find_packages

__version__ = "0.4.2"

requirements = [
    "pyyaml"
]

setup(
    name='docme',
    version=__version__,
    description="Auto documentation generating",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    license="MIT",
    author="Elran Shefer",
    author_email="elran777@gmail.com",
    keywords="doc",
    install_requires=requirements,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*",
    entry_points={
        "console_scripts": [
            "docme = docme.cli:main"
        ],
    },
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={'': ['*.xls', '*.xsd', '*.json', '*.css', '*.xml', '*.rst']},
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
)