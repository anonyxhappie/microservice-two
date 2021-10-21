FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /common /code1 /code2 /code3
RUN pip install --upgrade pip

RUN apt-get update -y
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

COPY rabbitmq-install.sh .
RUN chmod +x rabbitmq-install.sh
RUN /bin/sh rabbitmq-install.sh

RUN git clone https://github.com/anonyxhappie/microservice-one
RUN git clone https://github.com/anonyxhappie/microservice-two
RUN git clone https://github.com/anonyxhappie/microservice-three
RUN pip install -r /microservice-one/requirements.txt

COPY rabbitmq-start.sh .
RUN chmod +x rabbitmq-start.sh

EXPOSE 8000 8001 8002 5672 15672

CMD [ "/rabbitmq-start.sh" ]
