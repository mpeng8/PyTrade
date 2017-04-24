# PyTrade

PyTrade is a website trading application that provides stock data visualization and predictive models of stock market trends based on SPY (S&P 500, or Standard & Poor’s 500), DJI (Dow Jones Industrial Average), and NDX (NASDAQ - 100).

PyTrade serves as a platform for both professional investors and newcomers to manage their stock holdings, educate them about the historical background of markets, and provide suggestions about trading strategies based on PyTrade’s validated models of stock markets.

Additionally, PyTrade aims to become a valid source of information for investors to learn about future market trends by developing a high performance model of stock markets.

## Table of Contents

- [Release Notes](#release-notes)
   - [New software features for this release](#new-software-features-for-this-release)
   - [Bug fixes made since the last release](#bug-fixes-made-since-the-last-release)
   - [Known bugs and defects](#known-bugs-and-defects)
- [Install Guide](#install-guide)
   - [Prerequisites](#prerequisites)
     - [Python](#python)
     - [TA-Lib](#ta-lib)
     - [NumPy](#numpy)
     - [pandas](#pandas)
     - [scikit-learn](#scikit-learn)
     - [flask-sqlalchemy](#flask-sqlalchemy)
   - [Dependent libraries that must be installed](#dependent-libraries-that-must-be-installed)
   - [Download instructions](#download-instructions)
   - [Installation of actual application](#installation-of-actual-application)
   - [Run instructions](#run-instructions)
   - [Troubleshooting](#troubleshooting)
- [Authors](#authors)


## Version 0.9.0 Release Notes
This is the beta release of our website. The notes will introduce main features, bug fixes and known bugs that still need to be fixed.
### New software features for this release
1. Register or login to an account in PyTrade website
2. User-friendly dashboard
3. User connections (following and unfollowing users, viewing user profile)
4. Stock information searching
5. Add and remove stock from stock list
6. Interactive stock price visualization
7. Stock price prediction and suggestions for selling or buying stocks

### Bug fixes made since the last release
1. Javascript and plugin:  the crossover website information request using Allow-Control-Allow-Origin from google chrome plugin.
2. Stock list table paging: now the stock list table can be displayed with 10, 25, 50 ,100 entries per page as they want, and when searching for new stocks
3. Stock searching: When searching for stock information, the stock name can be auto-completed.
4.  Email, username, password validation for new user registration
### Known bugs and defects
1. Some stocks can not be fetched from Quandl, because of invalid stock name or insufficient data.
2. Extensively searching for stocks symbol will report errors and the stock names cannot be auto-completed.
3. Javascript 500 error: the menu toggle function cannot be used in stock information page.
4. Hosting website on cloud is under construction
5. Website security check still needed for implementing connection of the banking account
6. Machine learning model optimization is still under improvement

## Install Guide

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

#### Python
PyTrade uses [Python 2.7.12](https://www.python.org/downloads/release/python-2712/). We recommend installing Python from Anaconda
[Anaconda](https://www.continuum.io/anaconda-overview) is the leading open data science platform powered by Python. To download Anaconda, please go to Anaconda download page. [HERE](https://www.continuum.io/downloads)

After you have installed Anaconda, you can run the following command in your terminal to install required packages
```
$ python package_install.py
```
Then, you can skip the following sections.

#### TA-Lib
TA-Lib is a Python package that PyTrade uses to perform technical analysis of financial market data.

To install from Anaconda, type the following command into your terminal:
```
conda install -c quantopian ta-lib=0.4.9
```
To install from PyPI, type the following command into your terminal:
```
$ pip install TA-Lib
```
Or checkout the [sources](https://pypi.python.org/pypi/TA-Lib), and type the following command into your terminal:
```
$ python setup.py install
```

#### NumPy
NumPy is a Python package for scientific computations.

To install from Anaconda, type the following command into your terminal:
```
conda install -c anaconda numpy=1.12.1
```

To install from a Linux package manager, type the following command into your terminal:
```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```

For other installation methods or other systems, please checkout [NumPy Download Page](https://www.scipy.org/install.html)

#### pandas

To install from Anaconda, type the following command into your terminal:
```
conda install -c anaconda pandas=0.19.2
```
To install from PyPI, type the following command into your terminal:
```
pip install pandas
```
For other installation methods or other systems, please checkout [pandas Download Page](http://pandas.pydata.org/pandas-docs/stable/install.html)

#### scikit-learn

To install from Anaconda, type the following command into your terminal:
```
conda install scikit-learn
```
To install from PyPI, type the following command into your terminal:
```
pip install -U scikit-learn
```
For other installation methods or other systems, please checkout [scikit-learn Download Page](http://scikit-learn.org/stable/install.html)

#### flask-sqlalchemy
To install from Anaconda, type the following command into your terminal:
```
conda install -c anaconda sqlalchemy=1.1.9
```

To install from PyPI, type the following command into your terminal:
```
pip install SQLAlchemy
```
For other installation versions, please checkout [SQLAlchemy Index of Packages](https://pypi.python.org/pypi/SQLAlchemy)

### Dependent libraries that must be installed

Since PyTrade's real-time stock data comes from [quandl](https://www.quandl.com), PyTrade currently relies on a third-party plugin to make API calls.  

* [Allow-Control-Allow-Origin](https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi/related?hl=en-US)

### Download instructions

To download PyTrade, type the following command in your terminal:
```
git clone https://github.com/mpeng8/PyTrade.git
```

### Installation of actual application

PyTrade does not require any additional installation. After you have downloaded PyTrade repository, you are ready to run PyTrade.

### Run instructions
To run PyTrade on your localhost server, run the following command in your terminal.

```
$ python run.py
```

### Troubleshooting
```
'python' is not recognized as an internal or external command, operable program or batch file.
```
This typically means that your Python path is not declared. We suggest following the instructions [here](https://docs.python.org/2/using/windows.html#excursus-setting-environment-variables).

```
talib/common.c:8:22: fatal error: pyconfig.h: No such file or directory
#include "pyconfig.h"
^
compilation terminated.
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```
This typically means that you need the Python headers, and should run
something like:

```
$ sudo apt-get install python3-dev
```

```
func.c:256:28: fatal error: ta-lib/ta_libc.h: No such file or directory
compilation terminated.
```
This typically means that it can't find the underlying TA-Lib library, a dependency which needs to be installed.

```
Command C:\Python27\python.exe -c "import setuptools, tokenize;__file__='c:\\users\\jon\\appdata\\local\\temp\\pip_build_jon\\numpy\\setup.py';exec(compile(getattr(tokenize, 'open', open(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record c:\users\jon\appdata\local\temp\pip-qnynnf-record\install-record.txt --single-version-externally-managed

--compile failed with error code 1 in c:\users\jon\appdata\local\temp\pip_build_jon\numpyStoring

debug log for failure in C:\Users\jon\pip\pip.log
```

This typically means that wheel(.whl file) is not supported. You may try run something like:

```
pip install wheel
pip install numpy‑1.9.1+mkl‑cp27‑none‑win32.whl
```

```
Command /usr/bin/python -c "import setuptools, tokenize;__file__='/tmp/pip_build_reihaneh/sklearn/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-89YQB7-record/install-record.txt --single-version-externally-managed --compile failed with error code 1 in /tmp/pip_build_reihaneh/sklearn
Storing debug log for failure in /home/reihaneh/.pip/pip.log
```
This typically happens because your install command for scikit-learn is incorrect. Please re-check your install command

```
I got a 'Woops, there was an error making the request.' message popped out.
```
This typically means that the third-party plugin is not running correctly. You can just refresh the page.

```
error: The requested URL returned error: 401 while accessing
https://github.com/mpeng8/PyTrade.git
fatal: HTTP request failed
```
Note that you need to ensure the remote is correct. The repository you're trying to fetch must exist on GitHub, and the URL is case-sensitive.



## Authors

* **Mengyi Peng** - *Stock Price Visualization development*
* **Xinmin Shi** - *AWS Set-up*
* **Mingjun Xie** - *Database Design and development*
* **Yihan Zhou** - *Machine learning model implementation and optimization*
