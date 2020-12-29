from setuptools import setup, find_packages


def setup_package():
    metadata = dict(
        name="friends",
        version="0.1.0",
        description="friends",
        packages=find_packages(),
        package_data={
            "friends": ["json/*"]
        },
        include_package_data=True,
        install_requires=[]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
