import setuptools

setuptools.setup(
    entry_points={
        "console_scripts": [
            "skopy=skopy.command:command"
        ]
    },
    include_package_data=True,
    install_requires=[
        "celery",
        "click",
        "mahotas",
        "numpy",
        "pandas",
        "scikit-image",
        "sqlalchemy",
        "sqlalchemy-utils"
    ],
    name="skopy",
    packages=[
        "skopy",
        "skopy.commands"
    ],
    version="0.1.0"
)
