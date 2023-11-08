# {{ cookiecutter.project_name }}

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
- python3.9
- pip
- virtualenv or venv

```
Give examples
```

### Installing

the easiest way to bootstrap is to use the `Makefile`

```
git clone {{ cookiecutter.gitlab_url }}
cd {{ cookiecutter.project_slug }}
make install
```

if you want to only install the created package

```
pip install {{ cookiecutter.project_slug }}
```


## Running the tests

in the activated virtualenv run `pytest tests`

but you can also use `invoke tests`

if you used the bootstrap via Makefile you can use `make test` which is independent of the
virtual environment.


### Checking for Code-quality

run the linters in the venv wich `invoke code-quality`


or `make check`

### pre-coommit hooks

these need to be installed manually if used. 
the dependencies are not bootstrapped either.

## Deployment

Add additional notes about how to deploy this on a live system


## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **{{ cookiecutter.author }}** 


## License


## Built with

- [flit-cookiecutter]()
- [README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
