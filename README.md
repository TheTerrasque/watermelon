# watermelon
Next-generation web backend for streaming community radio.  Django providing REST API.

## Up-and-running instructions:

Note: docker and docker-compose isn't required, but it's the easiest way to get the environment set up

1. Clone with --recursive to get submodules
2. On first docker run, start first DB, then REST, then the others
 - docker-compose up -d db
 - docker-compose up -d rest
 - docker-compose up

There will be an admin interface at http://<docker-ip>:80/admin and if an "admin" account doesn't exist, it will be created with password "admin"