from setuptools import setup

setup(
    name = "json2run",
    version = "0.5",
    description = "A tool to launch experiments.",
    author="Tommaso Urli",
    author_email="tunnuz@gmail.com",
    license = "MIT",
    packages = ["json2run"],
    install_requires = [
        "pymongo>=3.0",
        "scipy",
        "numpy",
        "pandas",
        "argcomplete"
    ],
    scripts = ["./j2r", "./j2ranalyze"]
)
