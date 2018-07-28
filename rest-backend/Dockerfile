FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app/rest-backend
RUN ["/bin/bash", "/app/rest-backend/docker/setup.sh"]
CMD ["/bin/bash", "/app/rest-backend/docker/run.sh"]