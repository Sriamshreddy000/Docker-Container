FROM python:3.9-slim

WORKDIR /home

COPY script.py /home/
COPY data /home/data


RUN mkdir -p /home/data/output

CMD ["python", "/home/script.py"]




