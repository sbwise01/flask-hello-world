FROM scratch
LABEL maintainer="brad@foghornconsulting.com"

ADD rootfs.tar.xz /

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache py2-pip curl \
    && pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

ENV FLASK_APP app.py
RUN mkdir /app
COPY app.py /app

VOLUME /app
EXPOSE 5000

# Cleanup
RUN rm -rf /.wh /root/.cache /var/cache /tmp/requirements.txt

WORKDIR /app
CMD ["/usr/bin/flask", "run", "--reload", "-h", " 0.0.0.0"]
