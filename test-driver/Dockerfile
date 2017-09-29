# Owned by Veritas Ltd.
# Creted as part of MCDMP-RAILS project
# maintainer DL-VTAS-Eagle@veritas.com

FROM centos:centos7
MAINTAINER MCDMP Eagle Team <DL-VTAS-Eagle@veritas.com>

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y update

RUN yum install -y \
    openssh-server \ 
    passwd \
    python34 \
    python34-pip \
    curl

RUN yum clean all

RUN pip3 install requests
EXPOSE 80
EXPOSE 2525
EXPOSE 3000

CMD python3 python_tests.py           
