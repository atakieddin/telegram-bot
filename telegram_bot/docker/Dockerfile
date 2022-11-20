FROM python:3.9-slim-buster as base_layer
RUN apt-get update && apt-get install gcc musl-dev -y
WORKDIR /workspace


# Setup the python packages
FROM base_layer as package_layer
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY telegram_bot telegram_bot

# perform linting
COPY .pylintrc .pylintrc
RUN black telegram_bot
RUN pylint telegram_bot
CMD [ "python3", "-m" , "telegram_bot.__main__"]
