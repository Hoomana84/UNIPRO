FROM python:3.12.1

WORKDIR /var/www

COPY /fast1/sql_app/requirements.txt .

RUN pip install -r requirements.txt

COPY sql_app .

CMD ["fastapi", "run","main.py"]





