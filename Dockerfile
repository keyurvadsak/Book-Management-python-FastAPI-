FROM python:3.14

WORKDIR /Book_Management

COPY . /Book_Management

RUN pip install -r requirement.txt

EXPOSE 3000

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","3000"]

