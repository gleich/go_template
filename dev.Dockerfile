FROM golang:1.15

# Meta data:
LABEL maintainer="project_author_email"
LABEL description="project_description"

# Copying over all the files:
COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["make", "local-test"]
