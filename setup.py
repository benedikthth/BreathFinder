from setuptools import find_packages, setup
setup(
    name='BreathFinder',
    packages=find_packages(include=['numpy', 'sklearn', 'scipy']),
    install_requires=[
          'numpy',
          'sklearn',
          'scipy'
    ],
    version='0.1.0',
    description='''Algorithm designed to find locations of
    individual breaths in a PSG''',
    author='Benedikt Holm Thordarson',
    license='MIT',
)
