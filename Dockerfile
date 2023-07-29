FROM python:latest
WORKDIR /root/Project/Docker
COPY . .
RUN pip install --upgrade pip
COPY requirments.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ENTRYPOINT 8080
CMD ["python", "/root/Project/Docker/main.py"]

