from setuptools import setup

from milkshakelang import __version__

with open("README.md", mode="r", encoding="utf-8") as fp:
    long_description = fp.read()


setup(
    name="milkshakelang",
    version=__version__,
    description="The MilkShake Programming Language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dani El-Ayyass",
    author_email="dayyass@yandex.ru",
    license_files=["LICENSE"],
    url="https://github.com/dayyass/milkshakelang",
    packages=["milkshakelang"],
    entry_points={
        "console_scripts": [
            "milkshakelang = milkshakelang.__main__:main",
        ],
    },
)
