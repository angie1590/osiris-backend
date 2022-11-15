# osiris-backend

## Docker

Run the command

docker build .

docker-compose build

## Linting with flake8 
docker-compose run --rm app sh -c "flake8"

## Testing with Django test suite
docker-compose run --rm app sh -c "python manage.py test"

## Create django app
docker-compose run --rm app sh -c "django-admin startproject app ."

## Run app
docker-compose up