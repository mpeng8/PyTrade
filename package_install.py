import conda.cli
conda.cli.main('conda', 'install',  '-y', 'numpy')
conda.cli.main('conda', 'install',  '-y', 'pandas')
conda.cli.main('conda', 'install', '-c','quantopian', 'ta-lib=0.4.9')
conda.cli.main('conda', 'install', '-y', 'scikit-learn')
conda.cli.main('conda', 'install', '-c', 'sqlalchemy=1.1.9')
