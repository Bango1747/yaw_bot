from setuptools import setup, find_packages

setup(
    name="yaw_bot",
    version="0.1.0",
    description="Yaw bot Isaac Lab project",
    package_dir={"": "source/yaw_bot"},
    packages=find_packages(where="source/yaw_bot"),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.10",
)