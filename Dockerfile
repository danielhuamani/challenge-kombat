FROM python:3.9.7

RUN apt-get -y update
RUN pip install --upgrade pip
RUN mkdir /www
WORKDIR /www
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

COPY requirements/local.txt local.txt
RUN pip3 install -r local.txt
EXPOSE 80