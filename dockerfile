FROM python:3.12

COPY . .

RUN  pip intall -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] 