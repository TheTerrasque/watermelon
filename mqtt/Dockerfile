FROM eclipse-mosquitto
ADD files/* /mosquitto/config/
ARG mqtt_password
RUN /usr/bin/mosquitto_passwd -b /mosquitto/config/mosquitto.passwd watermelon "${mqtt_password}"