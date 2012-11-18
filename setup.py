from distutils.core import setup, Extension

phpunserialize = Extension(
    "pakker.php._unserialize",
    sources=["pakker/php/_unserialize.c"])

setup(
    name="pakker",
    packages=["pakker", "pakker.php", "pakker.tests"],
    version="0.1",
    ext_modules=[phpunserialize])
