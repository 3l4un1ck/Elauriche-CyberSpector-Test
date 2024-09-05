# Dockerfile for Vue.js frontend
FROM node:21

WORKDIR /app

COPY package*.json ./

RUN npm install --legacy-peer-deps && npm install --save-dev @vue/cli-service --legacy-peer-deps

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]