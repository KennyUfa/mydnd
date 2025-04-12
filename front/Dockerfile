# syntax=docker/dockerfile:1

# Build stage
FROM node:22.13.1-slim AS builder

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY --link front/package.json front/package-lock.json ./front/
RUN cd front && npm ci

# Copy application files
COPY --link front ./front

# Build the application
RUN cd front && npm run build

# Production stage
FROM nginx:stable-alpine AS production

# Copy built application from builder stage
COPY --from=builder /app/front/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]