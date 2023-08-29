FROM alpine:3.18.3

MAINTAINER Lars Gustavsson (lars@vingpin.se)

EXPOSE 8122
RUN     apk update \
    &&  apk add bash bind-tools busybox-extras curl \
                iproute2 iputils jq mtr \
                net-tools nginx openssl \
                python3 py3-pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
 
COPY api.py .
COPY templates ./templates
CMD [ "python", "./api.py" ]

