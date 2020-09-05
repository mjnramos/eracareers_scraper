# Eracareers Scraper

![Stable: 1](https://img.shields.io/badge/Stable-1-green.svg)
![MIT license](https://img.shields.io/badge/License-MIT-green "MIT License")

Eracareers [site](www.eracareers.pt) is a repository for Portuguese scientific
jobs. Unfortunately, the website offers few search options. This project
scrapes all the opportunities on Eracareers and sets the new opportunities
apart.


## Table of contents

* [Install](#install)
  * [Requirements](#requirements)
  * [Installation](#instalation)
* [Usage](#usage)
  * [Direct usage](#directusage)
  * [Cron](#cron)
* [Contributing](#contributing)
  * [Contributors](#contributors)
* [License](#license)


## Install

### Requirements

This project was tested with Python3 (v3.6.9) and the following libraries:
* BS4 (a.k.a. BeautifulSoup; v4.9.1)
* JSON (v2.0.9)
* Pandas (v1.1.1)
* Requests (v2.24.0)


## Usage

### Direct usage

1. `git clone` this repository
~~~
git clone https://github.com/mjnramos/eracareers_scraper.git
~~~

2. Run the scraper script
~~~
python3 scraper.py
~~~

3. Do whatever you want with the outputted file file (by default:
  `new_jobs.csv`)

**Usage notes**:
* If you already had an `--output` file, it will be overwritten!
* If you want to load all the opportunity jobs, delete the database file (by
  default: `all_opportunities.json`).


### Cron

You may want to install this script to run automatically by your system at a
specified date and time. Follow your system instructions to save the usage
command as a cron command.


## Contributing

For contributing to this project, please check [contributing](CONTRIBUTING.md)
documentation.

**No tests are available yet... sorry for that...**


### Contributors

* [Miguel Ramos](https://github.com/mjnramos/)


## License

This application is distributed under the terms of the
[MIT license](LICENSE.md).
