# Running the Project with Docker

To run this project using Docker, follow the steps below:

## Prerequisites

- Ensure Docker and Docker Compose are installed on your system.
- Verify that the `requirements.txt` file is present in the project root directory.

## Environment Variables

- The `db` service requires the following environment variables:
  - `POSTGRES_USER`: Database username (default: `user`)
  - `POSTGRES_PASSWORD`: Database password (default: `password`)
  - `POSTGRES_DB`: Database name (default: `app_db`)

## Build and Run Instructions

1. Build and start the services using Docker Compose:

   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://localhost:8000`.

## Exposed Ports

- `app` service: 8000 (mapped to host `8000`)
- `db` service: Not exposed to the host system.

## Notes

- The application code is mounted as a volume for live updates during development.
- The `db` service uses a persistent volume to store database data.

For further details, refer to the Docker Compose file and the `Dockerfile` provided in the project.