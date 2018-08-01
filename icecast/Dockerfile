FROM python:3.7-slim
WORKDIR /app
ADD files/* /app/
RUN ["/bin/bash", "/app/setup.sh"]
CMD ["/bin/bash", "/app/run.sh"]

