import conda.cli
conda.cli.main('conda', 'install',  '-y', 'numpy')
conda.cli.main('conda', 'install',  '-y', 'pandas')
conda.cli.main('conda', 'install', '-y', 'ta-lib')
conda.cli.main('conda', 'install', '-y', 'scikit-learn')
conda.cli.main('conda', 'install', '-c', 'flask-sqlalchemy=2.0')
