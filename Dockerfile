FROM debian:jessie
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    git \
    python-pip \
    python \
    python-mysqldb \
    emacs

RUN mkdir /data/ && \
    cd /opt/ && \
    git clone https://github.com/politeauthority/simple-callback-server.git && \
    cd simple-callback-server && \
    pip install -r requirements.txt && \
    git config --global alias.co checkout && \
    git config --global alias.br branch && \
    git config --global alias.ci commit && \
    git config --global alias.st status && \
    git config --global alias.unstage 'reset HEAD --'

ENV SCS_MYSQL_HOST="Host"
ENV SCS_MYSQL_USER="User"
ENV SCS_MYSQL_PASS="Pass"
ENV SCS_MYSQL_PORT=3306
ENV SCS_MYSQL_NAME="stocky"
ENV SCS_BASE_LOGGING_DIR='/data/logs'
ENV SCS_BUILD="dev"
ENV SCS_APP_DATA_PATH="/data/"
ENV TZ=America/Denver

VOLUME /opt/simple-callback-server/
VOLUME /data/

EXPOSE 80
