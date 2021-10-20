FROM python:3.10
WORKDIR /usr/src
RUN pip --no-cache-dir install bottle
COPY app.py .
ENTRYPOINT [ "python3", "app.py" ]
