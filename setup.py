from setuptools import setup, find_packages

setup(
    name="egeaML",
    version="0.1.0",
    author="Andrea Giussani",
    author_email="andrea.f.giussani@gmail.com",
    description=("A python library used in support of the Book"
                 "'Applied Machine Learning with Python' (2019)"),
    url="https://github.com/andreagiussani/Applied_Machine_Learning_with_Python",
    license="BSD",
    packages=find_packages(),
    install_requires=['xgboost==0.82', 'pandas==0.23.1', 'scikit-learn==0.20.4',
                      'seaborn==0.9.0', 'catboost==0.16.2'],
    include_package_data=True,
    classifiers=("Programming Language :: Python :: 3"),
)
