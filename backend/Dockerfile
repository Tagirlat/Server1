FROM python:3.13-slim

COPY src/req.txt src/req.txt

RUN pip install -r src/req.txt


COPY src src



CMD ["python", "main.py"]