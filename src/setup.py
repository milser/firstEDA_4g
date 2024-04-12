from setuptools import setup, find_packages

setup(
    name='edas_tatmil',
    version='0.1',
    packages=find_packages(),
    # Metadatos adicionales del proyecto
    author='Tatiana Cazorla y Rubén Serrano',
    description='Tu EDA mas sencillo',
    url='https://github.com/milser/edas_tatmil',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Lista de clasificaciones de compatibilidad con Python, SO, etc.
    ],
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "importlib",
        "tabulate",
    ],
)
