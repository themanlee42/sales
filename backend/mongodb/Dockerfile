FROM mongo:latest

COPY ./my-mongo-config.conf /etc/mongo/mongo.conf
COPY ./init-scripts/ /docker-entrypoint-initdb.d/

EXPOSE 27017
