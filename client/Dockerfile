
FROM node:alpine

RUN mkdir -p /client
WORKDIR /client

COPY package*.json ./
RUN npm install --quiet --no-optional

CMD ["npm", "run", "serve"]