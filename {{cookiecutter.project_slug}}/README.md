# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

---

## 🚀 Prerequisites

Make sure you have the following installed:

- [Python 3.11](https://www.python.org/downloads/)
- [Docker and Docker Compose](https://www.docker.com/)
- [Git](https://git-scm.com/)

---

## ⚙️ Project Setup

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Initialize pre-commit

```bash
pre-commit install
```

### Configure environment

...

## Initialize the database

Run migrations to prepare the database:

```bash
alembic upgrade head
```

---

## 🏃 Running the Application

### Locally

```bash
uvicorn app.main:app --reload
```

Access the API at: [http://127.0.0.1:{{cookiecutter.network_container_port}}](http://127.0.0.1:{{cookiecutter.network_container_port}})

### With Docker

```bash
docker-compose up --build
```

Access the API at: [http://127.0.0.1:{{cookiecutter.network_container_port}}](http://127.0.0.1:{{cookiecutter.network_container_port}})

---

## 📚 API Documentation

Access the interactive documentation (OpenAPI):

- Swagger UI: [http://127.0.0.1:{{cookiecutter.network_container_port}}/docs](http://127.0.0.1:{{cookiecutter.network_container_port}}/docs)
- ReDoc: [http://127.0.0.1:{{cookiecutter.network_container_port}}/redoc](http://127.0.0.1:{{cookiecutter.network_container_port}}/redoc)

---

## 📂 Project Structure

```plaintext
...
```

---

## 🧪 Tests

### Run tests

```bash
pytest
```

### Coverage report

```bash
pytest --cov=app --cov-report=term-missing
```

---
