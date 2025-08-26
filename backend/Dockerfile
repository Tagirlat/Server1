FROM python:3.13-slim

COPY src src

RUN pip install -r src/req.txt

CMD ["uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "80"]