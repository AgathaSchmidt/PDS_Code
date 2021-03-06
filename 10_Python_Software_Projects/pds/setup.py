from setuptools import setup

setup(
    name='pds',
    version='0.0.1dev1',
    description="Programming Data Science",
    author="Philipp Kienscherf",
    author_email="philipp.kienscherf@wiso.uni-koeln.de",
    packages=["pds"],
    install_requires=['pandas', 'scikit-learn', 'click'],
    entry_points={
        'console_scripts': ['pds=pds.cli:main']
    }
)
