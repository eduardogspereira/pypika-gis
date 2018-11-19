import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="pypika-gis",
    version="0.0.6",
    author="Eduardo G. S. Pereira",
    author_email="edu_vcd@hotmail.com",
    description="SpatialTypes functions for extend PyPika with GIS",
    url="https://github.com/eduardogspereira/pypika-gis",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=('pypika gis postgis mysql sql query builder'),
    install_requires=required
)
