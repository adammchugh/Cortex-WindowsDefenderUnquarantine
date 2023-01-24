FROM python:3.11.0-slim
LABEL maintainer=ghislain.bernard@gmail.com

WORKDIR /analyzer

COPY template template
RUN pip install --no-cache-dir --requirement template/requirements.txt

ENTRYPOINT ["template/template.py"]
