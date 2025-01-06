FROM {{cookiecutter.base_image}}

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["/bin/bash", "-c", "python -m uvicorn app.main:app --host 0.0.0.0 --port {{cookiecutter.network_container_port}} --reload"]
