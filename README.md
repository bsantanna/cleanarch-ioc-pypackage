# Clean Architecture IoC Project Base

This project implements a clean architecture scaffolding with prototype classes for the following tech stack:

- FastAPI for RESTful API
- PostgreSQL database with SQLAlchemy ORM for data persistence
- Alembic for database migrations
- Python Dependency Injector for Inversion of Control
- Pytest for unit testing
- Testcontainers for integration testing
- Redis for caching
- Docker compose with setup for integrated development environment
- Pre-commit for code quality

Clean Architecture is a software design pattern that emphasizes the separation of concerns by organizing code into layers with distinct responsibilities. It aims to create systems that are easy to maintain, test, and evolve by keeping the business logic and application rules independent of external frameworks, databases, and user interfaces. The architecture typically includes layers such as Entities, Use Cases, Interface Adapters, and Frameworks and Drivers, each serving a specific purpose. By adhering to these principles, Clean Architecture helps in creating robust, scalable, and adaptable systems.

Dependency injection (DI) is a design pattern used to implement Inversion of Control (IoC) in software development, which helps to decouple the creation of object dependencies from their usage. By injecting dependencies into a class rather than having the class create them itself, DI promotes loose coupling and enhances code modularity. This separation of concerns makes the codebase more maintainable and testable, as it allows for easier swapping of implementations and facilitates unit testing by enabling the use of mock objects.

This project is based on the example from [python-dependency-injector](https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html) and contains a simple user entity with endpoints to manipulate user entity.

## Features

- **clean Architecture with FastAPI**: Ensures a clean separation between the core logic and external dependencies.
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
cookiecutter gh:bsantanna/clean-ioc-pypackage
```

Replace the prompts with proper values.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Cookiecutter](https://www.cookiecutter.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Python Dependency Injector](https://python-dependency-injector.ets-labs.org/)
- [Redis](https://redis.io/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Testcontainers](https://testcontainers.org/)
- [Docker](https://www.docker.com/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Pre-commit](https://pre-commit.com/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

## Support

If you find this project useful, please consider giving it a star on GitHub!

