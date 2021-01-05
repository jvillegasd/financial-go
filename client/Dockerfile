FROM node:alpine

LABEL Author="Johnny Villegas"
LABEL version="1.0"

RUN mkdir -p /client
WORKDIR /client

COPY package*.json ./
RUN npm install --quiet --no-optional

CMD ["npm", "run", "serve"]