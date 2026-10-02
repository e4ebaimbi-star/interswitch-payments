# ================================================
# Dockerfile — Interswitch Merchant Portal
# Node.js + Express serving HTML/CSS/JS
# ================================================
# Base image: Node.js 20 on Alpine Linux (small and fast)
FROM node:20-alpine
# Set working directory inside the container
# All commands below run from here
WORKDIR /app
# Copy package.json FIRST (before source code)
# Why: Docker caches this layer. If package.json hasn't changed,
# the npm install layer below is reused on the next build.
COPY package.json .
# Install dependencies inside the container
# --production skips devDependencies — keeps the image lean
RUN npm install --production
# Now copy the application source code
# This is after npm install so code changes don't break the cache
COPY server.js .
COPY web/ ./web/
# Set the port as an environment variable
# Can be overridden at runtime: docker run -e PORT=8080
ENV PORT=3000

# Document which port the container listens on
# (documentation only — -p in docker run actually opens the port)
EXPOSE 3000
# Command to run when the container starts
# Array format (exec form) is recommended over shell form
CMD ["node", "server.js"]: Default command to run app. Must be last.

### Why Orde Matters
Docker builds inlayers and caches each layer. By copying packages *.json and running npm install BEFORE copying the full code, we avoid reinstalling dependencies on every code change, making rebuilds faster and smaller