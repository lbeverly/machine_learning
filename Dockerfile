FROM python:3.5

COPY requirements.txt /requirements.txt
RUN echo 'deb http://mirrors.ocf.berkeley.edu/debian/ jessie-backports main' > /etc/apt/sources.list.d/backports.list \
	&& apt-get update \
	&& apt-get install -y ca-certificates curl build-essential libncurses-dev libreadline-dev \
		libsqlite3-dev libssl-dev zlib1g-dev xz-utils automake autoconf bison flex \
		libffms2-3 libpostproc52 libpostproc-dev mp4v2-utils libmp4v2-2 ffmpeg \
	&& easy_install pip \
	&& pip install -r /requirements.txt
	

