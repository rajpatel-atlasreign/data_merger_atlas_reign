from setuptools import setup, find_packages

setup(
    name='data_merger',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'pymysql',
        'sqlalchemy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'data_merge_service = data_merge_service.main:main',
        ],
    },
)
