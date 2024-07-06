FROM python:3.12.1

WORKDIR /var/www

COPY requierments.txt .

RUN pip install -r requierments.txt

COPY api2..py .

CMD [ "fastapi", "run", "api2..py"]


