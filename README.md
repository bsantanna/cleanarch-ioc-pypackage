# Hexagonal Architecture IoC Project Base

This project implements a hexagonal architecture scaffolding with prototype classes for relational database PostgreSQL.

The hexagonal architecture, also known as ports and adapters architecture, aims to create loosely coupled application components that can be easily connected to their software environment through ports and adapters.

This project is based on the example from [python-dependency-injector](https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html) and contains a simple user entity with endpoints to manipulate this entity.

## Features

- **Hexagonal Architecture with FastAPI**: Ensures a clean separation between the core logic and external dependencies.
- **PostgreSQL Integration**: Prototype classes for relational database operations.
- **Docker Support**: Easily containerize your application.
- **Environment Configuration**: Manage different environments using configuration files.
- **Unit Testing**: Pre-configured unit tests to ensure code quality.

## Usage

### Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [Cookiecutter](https://www.cookiecutter.io/)

### Initialize conda environment

```bash
conda create -n dev python=3.11
```

### Initialize project

Setup Cookiecutter:

```bash
conda activate dev
conda install cookiecutter
```

Initialize project using cookiecutter CLI:

```bash
cookiecutter gh:bsantanna/hexagonal-ioc-pypackage
```

Replace the prompts with proper values.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Python Dependency Injector](https://python-dependency-injector.ets-labs.org/)
- [Cookiecutter](https://www.cookiecutter.io/)

## Support

If you find this project useful, please consider giving it a star on GitHub!

