FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD rest-backend /app/rest-backend
ADD mqtt /app/mqtt
ADD docker /app/docker
RUN ["/bin/bash", "/app/docker/setup.sh"]
CMD ["/bin/bash", "/app/docker/start.sh"]