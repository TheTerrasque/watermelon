FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app/streamer
RUN ["/bin/bash", "/app/streamer/docker/apt.sh"]
RUN ["/bin/bash", "/app/streamer/docker/build.sh"]
CMD ["/bin/bash", "/app/streamer/docker/run.sh"]