FROM python:3.12-slim
# run as root
USER root

RUN apt-get update \
    #  && apt install mongodb \
    && apt-get install -y python3-pip python3-dev libpq-dev

WORKDIR /flask-app

COPY ./requirements.txt /flask-app/requirements.txt


#RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt



COPY . /flask-app

ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]


# run as non-root

# CMD [ "python3", "main.py" ]