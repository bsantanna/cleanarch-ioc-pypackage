# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

This project is based on [Clean Architecture IoC Project](https://bsantanna.github.io/cleanarch-ioc-pypackage/).

---

## 🚀 Quick Start

Execute the following command to build container images:

```bash
docker compose build
```

After building the images, run the following command to start the application:

```bash
docker compose up
```

Access the API at: [http://127.0.0.1:{{cookiecutter.network_mapped_port}}](http://127.0.0.1:{{cookiecutter.network_container_port}})

---

## ⚙️ Development Environment Setup

### Create a virtual environment

Create a virtual environment to isolate the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

After activating the virtual environment, install the dependencies:

```bash
pip install -r requirements.txt
```

### Run tests

After installing the dependencies, run the tests to make sure everything is working as expected:

```bash
make test
```

### Initialize pre-commit

If you plan to contribute to the codebase, it is recommended to install the pre-commit hooks:

```bash
pre-commit install
```

---

## 🏃 Running the Application

### Locally

```bash
uvicorn app.main:app --reload
```

Access the interactive documentation (OpenAPI):

- Swagger UI: [http://127.0.0.1:{{cookiecutter.network_container_port}}/docs](http://127.0.0.1:{{cookiecutter.network_container_port}}/docs)

---

## 📂 Project Structure

```plaintext
/
├── alembic
├── app
│   ├── application
│   ├── core
│   ├── domain
│   ├── infrastructure
│   ├── interfaces
│   ├── middleware
├── tests
    ├── integration
    ├── unit
```

---
