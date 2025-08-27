FROM python:3.13-slim

COPY backend/src/req.txt

RUN pip install -r backend/src/req.txt


COPY src backend/src



CMD ["python", "main.py"]