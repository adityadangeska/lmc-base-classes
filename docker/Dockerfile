FROM ubuntu:14.04

# Update the repo info
RUN apt-get update

# Install and configure supervisor
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

# Change installation dialogs policy to noninteractive, otherwise
# debconf raises errors: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d

# Install base deb packages
RUN apt-get install -y --force-yes \
                        apt-transport-https \
                        bind9-host \
                        build-essential \
                        git \
                        language-pack-en \
                        mosh \
                        perl \
                        perl-modules \
                        psmisc \
                        python \
                        python-dev \
                        python-pip \
                        rsync \
                        screen \
                        software-properties-common \
                        tmux \
                        vim \
                        wget

# Remove some packages from the base template
RUN apt-get -y purge postfix

# Upgrade pip to latest
RUN pip install --upgrade pip

# Installing ansible
RUN add-apt-repository -y ppa:ansible/ansible
RUN apt-get update
RUN apt-get install -y ansible

# Install other deb packages
RUN apt-get install -y --force-yes \
                        aptitude \
                        ftp \
                        gawk \
                        gfortran \
                        git-core \
                        language-pack-en-base \
                        libatk1.0-dev \
                        libatlas-base-dev \
                        libboost-python-dev \
                        libcairo2-dev \
                        libevent-dev \
                        libf2c2-dev \
                        libffi-dev \
                        libfontconfig1-dev \
                        libfreetype6-dev \
                        liblapack-dev \
                        libpng12-dev \
                        libpq-dev \
                        libssl0.9.8 \
                        lsof \
                        manpages \
                        man-db \
                        ntpdate \
                        python-cairo-dev \
                        tcpdump \
                        telnet \
                        tzdata \
                        unzip \
                        xauth \
                        zlib1g-dev

# Install mysql
RUN apt-get install -y mysql-client-core-5.6 \
                       mysql-client-5.6 \
                       mysql-server-5.6

# Add tango ppa for latest tango core
RUN add-apt-repository ppa:lmc-cam-ska/tango
RUN apt-get update

# Install tango core packages
RUN apt-get install -y tango-common \
                       liblog4tango5v5 \
                       liblog4tango-dev \
                       liblog4tango-doc \
                       libtango-dev \
                       libtango-doc \
                       libtango9

# Start mysql & install tango database packages
RUN service mysql start && apt-get install -y \
                       tango-accesscontrol \
                       tango-db \
                       tango-starter \
                       tango-test

# Pip install tango support packages
RUN pip install enum34 \
                "ipython<6.0" \
                fandango \
                jsonschema \
                mock \
                numpy \
                pytest \
                tango-simlib

# Pip install itango cli
RUN pip install itango \
                "six>=1.9.0" \
                tango-admin

# Install virtual monitor
RUN apt-get install -y xvfb

# Configure virtual monitor env variable
ENV DISPLAY=:1.0

# Provide TANGO admin utilities (tango_admin, Starter, etc.)
COPY tango_register_device /usr/local/bin/
RUN chmod 755 /usr/local/bin/tango_register_device \
 && ln -s /usr/lib/tango/* /usr/local/bin/

# Add user
RUN useradd -ms /bin/bash tango-cs \
 && echo tango-cs:tango | chpasswd \
 && echo "tango-cs ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/tango-cs \
 && chmod 0440 /etc/sudoers.d/tango-cs

# Create mount point, so we can create more files here when inside container,
# with external volume mounted
RUN mkdir /home/tango-cs/src \
 && chown -R tango-cs:tango-cs /home/tango-cs

# Start the container as tango-cs user and in home directory
USER tango-cs
WORKDIR /home/tango-cs

# Expose connection for TANGO DB
ENV ORB_PORT=10000
ENV TANGO_HOST=127.0.0.1:${ORB_PORT}
EXPOSE ${ORB_PORT}

# Configure supervisord
COPY supervisord.conf /etc/supervisor/conf.d/
RUN mkdir /var/tmp/supervisord.child

# Start supervisor as deamon
CMD ["/usr/bin/supervisord", "--configuration", "/etc/supervisor/supervisord.conf"]