Overview
========

Welcome to the Weather ETL Project! This project uses Apache Airflow to create an ETL pipeline that fetches weather data from Open-Meteo API and stores it in a PostgreSQL database.

Project Contents
================

Your project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs:
    - `etlweather.py`: This DAG implements a weather data ETL pipeline that:
        - Extracts current weather data from Open-Meteo API
        - Transforms the data into a structured format
        - Loads the data into PostgreSQL database
- Dockerfile: Contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience.
- docker_compose.yml: Defines the Docker Compose configuration for the project, including PostgreSQL database setup.
- include: Contains any additional files that you want to include as part of your project.
- packages.txt: Lists OS-level packages needed for your project.
- requirements.txt: Lists Python packages needed for your project:
    - apache-airflow-providers-http (for HTTP API connections)
- plugins: Contains custom or community plugins for your project.
- airflow_settings.yaml: Local-only file to specify Airflow Connections, Variables, and Pools.

Project Setup
============

1. **Prerequisites**
   - Docker Desktop installed
   - Astro CLI installed
   - Git (for version control)

2. **Required Connections**
   - Open-Meteo API (HTTP connection)
   - PostgreSQL database connection

3. **Database Schema**
   The project uses a PostgreSQL database with the following schema:
   ```sql
   CREATE TABLE weather_data (
       id SERIAL PRIMARY KEY,
       latitude FLOAT NOT NULL,
       longitude FLOAT NOT NULL,
       temperature FLOAT NOT NULL,
       windspeed FLOAT NOT NULL,
       winddirection FLOAT NOT NULL,
       weathercode INT NOT NULL,
       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

Deploy Your Project Locally
===========================

Start Airflow on your local machine by running 'astro dev start'.

This command will spin up five Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- DAG Processor: The Airflow component responsible for parsing DAGs
- API Server: The Airflow component responsible for serving the Airflow UI and API
- Triggerer: The Airflow component responsible for triggering deferred tasks

When all five containers are ready, you can access:
- Airflow UI at http://localhost:8080
- Postgres Database at localhost:5432/postgres
  - Username: postgres
  - Password: postgres

Useful Commands
==============

```bash
# Start the development environment
astro dev start

# Stop the development environment
astro dev stop

# Add Open-Meteo API connection
astro dev run airflow connections add open_meteo_api --conn-type http --conn-host https://api.open-meteo.com

# Check DAG status
astro dev run airflow dags list

# Trigger DAG manually
astro dev run airflow dags trigger weather_etl_pipeline

# View DAG logs
astro dev run airflow dags show weather_etl_pipeline
```

Contact
=======

For any issues or questions, please reach out to the project maintainers.
