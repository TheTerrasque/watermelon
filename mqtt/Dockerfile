FROM eclipse-mosquitto
ADD files/* /mosquitto/config/
RUN /bin/sh /mosquitto/config/build.sh
CMD ["/bin/ash", "/mosquitto/config/run.sh"]