from setuptools import setup, find_packages

setup(
    # Basic package information
    name='atlasreign_datamanager',
    version='0.0.0',
    packages=find_packages(),

    # Metadata
    author='RAJ PATEL',
    author_email='rajpatel@atlasreign.com',
    description='Data Merger: A Python package for merging data from two tables in a MySQL database. The service '
                'reads a configuration file that specifies the details of the merge operation, such as the names of '
                'the tables, the keys to join on, the type of join, and the output file name. Easy to use and highly '
                'flexible, Data Merger simplifies the process of merging data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rajpatel-atlasreign/data_merger_atlas_reign',

    # Dependencies
    install_requires=[
        'pymysql',
        'sqlalchemy',
        'pandas'
    ],

    # Entry points
    entry_points={
        'console_scripts': [
            'data_merge_service = data_merge_service.main:main',
        ],
    },

    # Classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],

    # Python version requirement
    python_requires='==3.10.*',  # Specific to Python 3.10
)
