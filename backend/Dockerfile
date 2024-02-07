FROM python:3.11.4
# set build argument for DOCKER_ENV, default is "production"
ARG DOCKER_ENV=production

WORKDIR /backend

COPY requirements.txt /backend/

# upgrade pip
RUN pip install --upgrade pip

# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the current directory contents into the container at /backend
COPY ./app /backend/app

EXPOSE 8080

# conditionally use Gunicorn with or without --reload based on DOCKER_ENV
CMD if [ "$DOCKER_ENV" = "development" ]; then gunicorn -b 0.0.0.0:8080 --reload --access-logfile - --error-logfile - 'app:create_app()'; else gunicorn -b 0.0.0.0:8080 --access-logfile - --error-logfile - 'app:create_app()'; fi

