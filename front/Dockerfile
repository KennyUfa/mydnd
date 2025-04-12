# syntax=docker/dockerfile:1

# Build stage
FROM node:22.13.1-slim AS builder

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY --link package.json package-lock.json ./
RUN npm ci

# Copy application files
COPY --link . .

# Build the application
RUN npm run build

# Production stage
FROM nginx:stable-alpine AS production

# Copy built application from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]