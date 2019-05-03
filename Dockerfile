#install debian and python
FROM python:3.7.2-slim
# Add variables SERVER
ENV SERVER=$SERVER
#get git
RUN apt-get update -y
RUN apt-get install git -y
#clone project
RUN git clone http://gitlab.ntlbss.com/autotests/ms-api-app.git /project
#go to project and load dependencies
WORKDIR /project
RUN pip3 install -r requirements.txt

#run tests on threads
CMD ["pytest", "-nauto"]