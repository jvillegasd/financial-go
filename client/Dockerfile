# Stage 1 - Build
FROM node:lts-alpine3.16 as build
RUN mkdir /app
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json
RUN npm install --global pnpm
RUN pnpm install
COPY . /app
RUN pnpm run build

# Stage 2 - Run
FROM nginx:1.17.10-alpine as run
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
