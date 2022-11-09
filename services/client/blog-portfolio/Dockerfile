FROM node:16.17-alpine

RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm ci && npm cache clean --force

COPY . .

RUN npm run build

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

EXPOSE 3000 

ENTRYPOINT ["npm", "run", "start"]