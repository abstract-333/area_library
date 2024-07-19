from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Area Python package"
LONG_DESCRIPTION = (
    "Area Python package to get area on different area_library using visitor pattern"
)

setup(
    name="area_library",
    version=VERSION,
    author="Bashar Hasan",
    author_email="<basharhasan74@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    tests_require=[
        "pytest==8.2.2",
        "pluggy==1.5.0",
        "iniconfig==2.0.0",
    ],
    test_suite="tests",
    keywords=[
        "python",
        "area",
        "shape",
        "triangle",
        "circle",
        "pi",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
