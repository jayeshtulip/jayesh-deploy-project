# Existing lines
FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 👇 Add this to copy the model folder from app/model/
COPY app app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
