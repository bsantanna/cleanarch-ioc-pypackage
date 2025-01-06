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
cookiecutter gh:bsantanna/cleanarch-ioc-pypackage
```

Follow the prompts to fill in the project details.

#### Initialization inputs

- `authors`: Your Name or Your Team
- `distribution_list_email`: Your email address
- `python_version`: The version of Python to use (default: 3.11)
- `base_image`: The base Docker image for Python (default: python:3.11-slim)
- `cache_image`: The Docker image for the cache service (default: redis:alpine)
- `cache_hostname`: The hostname for the cache service (default: localhost)
- `cache_port`: The port number for the cache service (default: 6379)
- `database_image`: The Docker image for the database service (default: postgres:16)
- `database_hostname`: The hostname for the database service (default: localhost)
- `database_name`: The name of the database (default: your_database_name)
- `database_password`: The password for the database (default: postgres)
- `database_port`: The port number for the database service (default: 5432)
- `database_username`: The username for the database (default: postgres)
- `network_container_port`: The port number exposed by the container (default: 8000)
- `network_mapped_port`: The port number mapped to the host (default: 18000)
- `network_name`: The name of the Docker network (default: your_network_name)
- `project_name`: The name of your project (default: Your Project Name)
- `project_slug`: A URL-friendly version of the project name (default: automatically generated from `project_name`)
- `project_description`: A brief description of your project (default: A brief description of your project)
- `sonar_token`: The token for SonarQube (default: your_sonar_token)
- `sonar_url`: The URL for SonarQube (default: http://your_sonar_url)
- `version`: The version of your project (default: 0.1.0)

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

