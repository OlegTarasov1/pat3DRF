FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv

RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

COPY ./pet2 .

EXPOSE 8000

CMD ["./venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]