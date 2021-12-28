import io
from importlib.machinery import SourceFileLoader
from pathlib import Path
from setuptools import find_packages, setup


def requirements_from_file(file_path):
    with open(file_path) as f:
        install_requirements = [
            line.strip()
            for line in f.readlines()
            if line.strip() and not line.startswith(('#', '-r'))
        ]
    return install_requirements


version = SourceFileLoader(
    'version', str(Path('.', 'toolset', 'version.py').resolve())
).load_module('version')

requirements_path = Path(__file__).parent.joinpath('requirements')
project_requirements_path = Path(requirements_path, 'all.txt')
test_requirements_path = Path(requirements_path, 'test.txt')

project_requirements = requirements_from_file(project_requirements_path)
test_requirements = requirements_from_file(test_requirements_path)

print(test_requirements)

extras = {
    'test': test_requirements,
    'dist': 'twine',
}

setup(
    name='toolset',
    version=version.__version__,
    description='Dev Toolset',
    long_description=io.open('README.rst', 'r', encoding='utf-8').read(),
    author='Oleksandr Kuznietsov',
    packages=find_packages(),
    include_package_data=True,
    install_requires=project_requirements,
    tests_require=test_requirements,
    extras_require=extras,
    zip_safe=False,
    entry_points={
        'console_scripts': ['toolset = toolset.tasks:toolset.run']
    },
    classifiers=[
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
    ],
    platforms=['macOS', 'POSIX', ],
    python_requires='>=3.10.0',
)
