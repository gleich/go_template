FROM golang:1.14.6-alpine3.12

WORKDIR /usr/src/app
COPY . .
RUN go mod download

CMD ["go", "run", "main.go"]
