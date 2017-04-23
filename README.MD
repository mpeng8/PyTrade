# PyTrade

PyTrade is a website trading application that provides stock data visualization and predictive models of stock market trends based on SPY (S&P 500, or Standard & Poor’s 500), DJI (Dow Jones Industrial Average), and NDX (NASDAQ - 100).

PyTrade serves as a platform for both professional investors and newcomers to manage their stock holdings, educate them about the historical background of markets, and provide suggestions about trading strategies based on PyTrade’s validated models of stock markets. Additionally, PyTrade aims to become a valid source of information for investors to learn about future market trends by developing a high performance model of stock markets.

## Table of Contents

- [Release Notes](#release-notes)
   - [New software features for this release](#new-software-features-for-this-release)
   - [Bug fixes made since the last release](#bug-fixes-made-since-the-last-release)
   - [Known bugs and defects](#known-bugs-and-defects)
- [Install Guide](#install-guide)
   - [Prerequisites](#prerequisites)
     - [Python](#python)
     - [TA-Lib](#ta-lib)
   - [Dependent libraries that must be installed](#dependent-libraries-that-must-be-installed)
   - [Download instructions](#download-instructions)
   - [Installation of actual application](#installation-of-actual-application)
   - [Run instructions](#run-instructions)
   - [Troubleshooting](#troubleshooting)
- [Authors](#authors)


## Release Notes

Stuff
### New software features for this release
### Bug fixes made since the last release
### Known bugs and defects



## Install Guide

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

#### Python
PyTrade uses [Python 2.7.12](https://www.python.org/downloads/release/python-2712/). There are two ways to install Python.

##### Install Python from Python Software Foundation
To download and install Python from Python Software Foundation, please go to Python Software Foundation download page. [HERE](https://www.python.org/downloads/)

##### Install Python from Anaconda(RECOMMEND)
[Anaconda](https://www.continuum.io/anaconda-overview) is the leading open data science platform powered by Python. To download Anaconda, please go to Anaconda download page. [HERE](https://www.continuum.io/downloads)

#### TA-Lib

numpy

panda

#### sklearn

### Dependent libraries that must be installed

Since PyTrade's real-time stock data comes from [quandl](https://www.quandl.com), PyTrade currently relies on a third-party plugin to make API calls.  

* [Allow-Control-Allow-Origin](https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi/related?hl=en-US)

### Download instructions


A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

### Installation of actual application

PyTrade does not require any additional installation. After you have downloaded PyTrade repository, you are ready to run PyTrade.

### Run instructions
To run PyTrade on your localhost server, run the following command in your terminal.

If your system is Mac or Linux, use the following command
```
$python run.py
```

If your system is Windows, use the following command
```
python run.py
```

### Troubleshooting
```
'python' is not recognized as an internal or external command, operable program or batch file.
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Authors

* **Mengyi Peng** - *Stock Price Visualization development* - [PurpleBooth](https://github.com/mpeng8/PyTrade)
* **Xinmin Shi** - *AWS Set-up*
* **Mingjun Xie** - *stuff* -[PurpleBooth](https://github.com/mpeng8/PyTrade)
* **Yihan Zhou** - *Stuff* - [PurpleBooth](https://github.com/mpeng8/PyTrade/tree/mongazer)
