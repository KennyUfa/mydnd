# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).

## Running the Project with Docker

This project includes Docker configurations to simplify the setup and execution of the application. Follow the steps below to build and run the project using Docker Compose.

### Prerequisites

- Ensure Docker and Docker Compose are installed on your system.
- Docker version: Ensure compatibility with `python:3.12-slim` and `node:22.13.1-slim` base images.

### Build and Run Instructions

1. Clone the repository and navigate to the project root directory.
2. Build and start the services using Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. Access the services:
   - Backend: `http://localhost:8000`
   - Frontend: `http://localhost`

### Exposed Ports

- Backend: `8000`
- Frontend: `80`
- Database: Not exposed externally.

### Notes

- The backend service depends on the database service to be running.
- The frontend service is built using Node.js and served via Nginx.

For further details, refer to the respective `Dockerfile` and `docker-compose.yaml` files.