from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension


hello1_extension = Extension(
    'src.hello_world',
    ['src/hello_world.pyx']
)

hello2_extension = Extension(
    'src.hello_world2',
    ['src/hello_world2.pyx']
)

setup(
    name='testing_cython',
    version='0.0.1',
    packages=find_packages(),
    author='Julián Cortés',
    author_email='pity7736@gmail.com',
    description='Async postgres data access layer',
    keywords='async asyncpg DAL',
    url='https://github.com/pity7736/gideon-db',
    ext_modules=cythonize([hello1_extension, hello2_extension])
)
