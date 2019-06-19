from setuptools import setup

VERSION = ""

with open("VERSION", "r+") as f:
    content = f.read()
    ver = str(content).strip().split(".")
    ver[2] = str(int(ver[2]) + 1)
    VERSION = ".".join(ver)
    f.seek(0)
    f.write(VERSION)


setup(
    name="petpy",
    version=VERSION,
    description="Petrophysics utilities",
    url="https://example.com/",
    author="Agile Scientific",
    author_email="matt@agilescientific.com",
    license="Apache 2",
    packages=["petpy"],
    install_requires=["numpy"],
)
