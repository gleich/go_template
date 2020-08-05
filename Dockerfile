FROM golang:1.14.6-alpine3.12

# Meta data:
LABEL maintainer="matthewgleich@gmail.com"
LABEL description="PROJECT_DESCRIPTION"

# Copying over all the files:
COPY . /usr/src/app
WORKDIR /usr/src/app

# Installing dependencies/
RUN go mod download

CMD ["go", "run", "main.go"]
