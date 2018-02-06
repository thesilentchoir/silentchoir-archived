# The Silent Choir Project

Welcome to the Silent Choir. Our goal is to uncover patterns of harassment and abuse by connecting survivors.
If you have been the victim of abuse in the workplace, at school, at home, anywhere at all, and would like to share your story on a safe platform, on your own terms, please join us.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python >= 3.4
* Pip
* Virtualenv
* Posgres


### Dev Setup for Mac Users

You can use Homebrew to install Python 3.x. It will also install Pip 3.x.

```
$ brew install python3
```

Install Virtualenv, a dependency management tool that creates isolated Python environments.

```
$ python3 -m pip install --user virtualenv
```

Create the virtual environment.

```
$ python3 -m virtualenv env
```

Activate the virtual environment.

```
$ source env/bin/activate
```

Install packages.

```
$ pip install -r requirements.txt
```

Copy the `.env` file from a teammate and add it to your project directory.

Install Postgres and create the database in the Postgres interactive command propmp.

```
>> CREATE DATABASE <database_name>;
```

Verify you can run the application.

```
$ python3 manage.py runserver
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
