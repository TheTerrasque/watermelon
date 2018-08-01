FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app/rest-backend

ADD docker /app/rest-backend/docker/
ADD requirements.txt /app/rest-backend/
RUN ["/bin/bash", "/app/rest-backend/docker/setup.sh"]

ADD . /app/rest-backend

CMD ["/bin/bash", "/app/rest-backend/docker/run.sh"]