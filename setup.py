import io
import os

from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup


def setup_version() -> str:
    version_prefix = "1.0"
    version = os.environ.get("BUILD_NUMBER") if bool(os.environ.get("TEAMCITY_VERSION")) else "SNAPSHOT"
    # return version_prefix + "." + version
    return "1.0.7"



extensions = [
    Extension(
        "_youtokentome_cython",
        [
            "youtokentome/cpp/yttm.pyx",
            "youtokentome/cpp/bpe.cpp",
            "youtokentome/cpp/utils.cpp",
            "youtokentome/cpp/utf8.cpp",
        ],
        extra_compile_args=["-std=c++11", "-pthread", "-O3"],
        language="c++",
    )
]

with io.open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"),
        encoding="utf-8",
) as f:
    LONG_DESCRIPTION = "\n" + f.read()

setup(
    name="youtokentome",
    version=setup_version(),
    packages=find_packages(),
    description="Unsupervised text tokenizer focused on computational efficiency",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/vkcom/youtokentome",
    python_requires=">=3.6.0",
    install_requires=["Cython>=0.29.21", "setuptools>=50.3.2"],
    entry_points={"console_scripts": ["yttm = youtokentome.yttm_cli:main"]},
    author="Ivan Belonogov",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Cython",
        "Programming Language :: C++",
    ],
    ext_modules=cythonize(extensions),
)
