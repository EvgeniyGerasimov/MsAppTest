FROM python:3.7.2-slim

RUN apt-get update -y
RUN apt-get install git -y
RUN git clone https://github.com/EvgeniyGerasimov/MsAppTest.git /project
WORKDIR /project
RUN pip3 install -r requirements.txt

CMD ["pytest", "-n4"]