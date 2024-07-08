FROM python:3.12.2-slim-bookworm

WORKDIR /var/www

COPY /fast1/requirements.txt .

RUN pip install -r requirements.txt

COPY fast1.

CMD ["fastapi", "main.py"]





