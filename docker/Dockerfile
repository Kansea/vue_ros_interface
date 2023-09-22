FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
# ENV LANG en_US.UTF-8
ENV LANG ja_JP.UTF-8
ENV TZ=Asia/Tokyo


###################################################################
# System configure and install tools
###################################################################
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common locales sudo tzdata libpq-dev \
    build-essential curl wget vim cmake python3-dev python3-pip \
    && locale-gen ja_JP ja_JP.UTF-8 \
    && update-locale LC_ALL=ja_JP.UTF-8 LANG=ja_JP.UTF-8 \
    && add-apt-repository universe \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - \
    && rm -rf /var/lib/apt/lists/*


###################################################################
# Install Django
###################################################################
RUN pip3 install django uwsgi djoser psycopg2 redis rospkg \
    django-rest-framework django-cors-headers \
    django-webpack-loader channels["daphne"] channels_redis


###################################################################
# Install nodejs
###################################################################
RUN apt-get update && apt-get install -y nodejs


###################################################################
# Install VUE
###################################################################
RUN npm install -g @vue/cli axios --save vue-axios


###################################################################
# Add user and group
###################################################################
ARG UID
ARG GID
ARG USER_NAME
ARG GROUP_NAME
ARG WORKSPACE_DIR

RUN groupadd -g ${GID} ${GROUP_NAME}
RUN useradd -u ${UID} -g ${GID} -s /bin/bash -m ${USER_NAME}
RUN echo "${USER_NAME} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers && chmod 0440 /etc/sudoers && chmod g+w /etc/passwd

USER ${USER_NAME}

WORKDIR /app
