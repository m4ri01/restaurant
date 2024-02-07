FROM node:14 AS builder
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install  
COPY . .
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
ARG PORT=80
EXPOSE ${PORT}
CMD ["nginx", "-g", "daemon off;"]