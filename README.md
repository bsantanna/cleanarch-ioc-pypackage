# Hexagonal Architecture Project Base

This project implements a hexagonal architecture scaffolding with prototype classes for relational database PostgreSQL and OpenSearch NoSQL. The hexagonal architecture, also known as ports and adapters architecture, aims to create loosely coupled application components that can be easily connected to their software environment through ports and adapters.

## Features

- **Hexagonal Architecture with FastAPI**: Ensures a clean separation between the core logic and external dependencies.
- **PostgreSQL Integration**: Prototype classes for relational database operations.
- **OpenSearch Integration**: Prototype classes for NoSQL operations.
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
cookiecutter gh:bsantanna/hexagonal-pypackage
```

Replace the prompts with proper values.

### Running the Application

To run the application, use the following commands:

```bash
# Activate the conda environment
conda activate dev

# Install dependencies
pip install -r requirements.txt

# Copy reference .env_example
cp .env_example .env

# Run the application
docker-compose up -d --build
```

Verify application is up and running accessing builtin docs endpoint: [http://localhost:18080/docs](http://localhost:18080/docs)

### Running Tests

To run the unit tests, use the following command:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [OpenSearch](https://opensearch.org/)
- [Cookiecutter](https://www.cookiecutter.io/)

## Support

If you find this project useful, please consider giving it a star on GitHub!

