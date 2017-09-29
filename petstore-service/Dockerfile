FROM nodesource/trusty
MAINTAINER Inns, Nicholas
RUN apt-get update && \
    apt-get -y install curl
RUN sudo npm install -g mountebank
ADD config.json .
EXPOSE 2525
EXPOSE 80
CMD mb --mock --debug --loglevel=debug --log mb.log --configfile config.json

