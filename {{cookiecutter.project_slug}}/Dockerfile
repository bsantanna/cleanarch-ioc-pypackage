FROM {{cookiecutter.base_image}}

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT={{cookiecutter.network_container_port}}

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    &&  pip install --no-cache-dir -r requirements.txt \

CMD ["/bin/bash", "-c", "python -m uvicorn app.main:app --host ${HOST} --port ${PORT}"]
