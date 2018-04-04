# The Silent Choir Project

Welcome to the Silent Choir. Our goal is to uncover patterns of harassment and abuse by connecting survivors.
If you have been the victim of abuse in the workplace, at school, at home, anywhere at all, and would like to share your story on a safe platform, on your own terms, please join us.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python >= 3.4
* Pip
* Virtualenv
* Postgres


### Dev Setup for Mac Users

You can use Homebrew to install Python 3.x. It will also install Pip 3.x.

```
$ brew install python3
```

Install Virtualenv, a dependency management tool that creates isolated Python environments.

```
$ python3 -m pip install --user virtualenv
```

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ pipenv install

$ pipenv shell

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Prod

```sh

```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details