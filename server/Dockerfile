FROM debian
ADD . /server
WORKDIR /server
RUN apt-get update
RUN apt-get -y install pkg-config build-essential libfuse-dev libcurl4-openssl-dev libxml2-dev mime-support automake libtool locales
RUN ./pifs/autogen.sh
RUN ./pifs/configure
RUN cd ./pifs
RUN make
RUN make install
RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

EXPOSE 80
