FROM python:3.12-slim
WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENTRYPOINT [ "python3", "app.py" ]
