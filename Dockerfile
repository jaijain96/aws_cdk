from python:3.11.11-bullseye

USER root

RUN apt-get update

# RUN mkdir /root/.aws

# COPY "Users/vk001/.aws/config" /root/.aws/config

# COPY "C:\Users\vk001\.aws/credentials" /root/.aws/credentials

RUN mkdir /home/setup_image

COPY setup.sh /home/setup_image/setup.sh

# RUN chmod +x /home/setup.sh

# RUN cat /home/setup_image/setup.sh

RUN /home/setup_image/setup.sh
# CMD ["bash","/home/setup.sh"]
# CMD ["bash", "/home/setup_image/setup.sh"]
