import os
from os.path import join
from setuptools import setup,Extension
from Cython.Build import cythonize
directory_path = os.path.dirname(
    os.path.abspath(__file__)
)

ext_data = {
    'abasepy11':{
        'sources':[join(directory_path,'abasepy11','base.py')]
    }
}

extensions = []

for name,data in ext_data.items():
    sources = data['sources']
    include = data.get('include',[])

    obj = Extension(
        name,
        sources=sources,
        include_dirs=include
    )

    extensions.append(obj)


setup(
    name="abasepy11",
    version="0.0.1",
    install_requires=[
        "pip","setuptools"
    ],
    ext_modules=cythonize(extensions)
)