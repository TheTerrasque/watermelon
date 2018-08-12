FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD demosauce /app/streamer/demosauce
ADD docker/build /app/streamer/docker/build
RUN ["/bin/bash", "/app/streamer/docker/build/setup.sh"]
RUN ["/bin/bash", "/app/streamer/docker/build/build.sh"]
ADD . /app/streamer
CMD ["/bin/bash", "/app/streamer/docker/run.sh"]