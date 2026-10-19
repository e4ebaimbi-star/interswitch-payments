FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup --system portal && adduser --system --ingroup portal portal
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/server.js ./server.js
COPY --from=build /app/web ./web
USER portal
EXPOSE 3000
ENTRYPOINT ["node"]
CMD ["server.js"]
