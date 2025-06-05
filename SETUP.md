# Astro Project Setup Documentation

## Installation Steps

1. **Docker Desktop Installation**
   - Docker Desktop was installed on macOS
   - Verified installation with `docker --version`
   - Docker version: 28.1.1

2. **Astro CLI Installation**
   - Installed Astro CLI using the command:
     ```bash
     curl -sSL https://install.astronomer.io | sudo bash -s -- v1.34.1
     ```
   - Verified installation with `astro version`
   - Astro CLI version: 1.34.1

3. **Project Initialization**
   - Initialized new Astro project using `astro dev init`
   - Project initialized in: `/Users/deepakkumar/coding/agenticai/etl_agentic_ai`

## Project Structure

```
.
├── .astro/              # Astro-specific configuration
├── .dockerignore        # Docker ignore rules
├── .git/                # Git repository
├── .gitignore          # Git ignore rules
├── airflow_settings.yaml # Airflow configuration
├── dags/               # Directory for Airflow DAGs
│   └── etlweather.py   # Weather ETL pipeline DAG
├── docker_compose.yml  # Docker Compose configuration
├── Dockerfile          # Container configuration
├── get-pip.py         # Python package installer
├── include/            # Additional files for DAGs
├── packages.txt        # System-level dependencies
├── plugins/            # Custom Airflow plugins
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── tests/              # Test files
└── venv/               # Python virtual environment
```

## Weather ETL Pipeline

### Overview
The project includes a weather ETL pipeline that:
- Extracts weather data from Open-Meteo API
- Transforms the data into a structured format
- Loads the data into PostgreSQL database

### Components

1. **Data Extraction**
   - Uses Open-Meteo API to fetch weather data
   - Requires HTTP connection with ID: `open_meteo_api`
   - Fetches current weather data for specified coordinates

2. **Data Transformation**
   - Processes raw API response
   - Extracts relevant weather metrics:
     - Temperature
     - Wind speed
     - Wind direction
     - Weather code
     - Location coordinates

3. **Data Loading**
   - Stores data in PostgreSQL database
   - Uses connection ID: `postgres_default`
   - Creates and maintains `weather_data` table
   - Implements proper transaction handling

### Database Schema
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

### Required Connections
1. **Open-Meteo API**
   - Connection ID: `open_meteo_api`
   - Type: HTTP
   - Host: https://api.open-meteo.com

2. **PostgreSQL**
   - Connection ID: `postgres_default`
   - Type: Postgres
   - Host: localhost
   - Port: 5432
   - Database: postgres
   - Username: postgres
   - Password: postgres

## Key Files and Their Purposes

1. **airflow_settings.yaml**
   - Contains Airflow configuration settings
   - Defines environment variables and connections

2. **Dockerfile**
   - Defines the container environment for Airflow
   - Specifies base image and dependencies

3. **requirements.txt**
   - Lists Python package dependencies
   - Currently includes:
     - apache-airflow-providers-http (for HTTP API connections)
   - Note: Many providers are pre-installed in Astro Runtime
   - Used for installing additional required Python packages

4. **packages.txt**
   - Lists system-level dependencies
   - Used for installing required system packages

5. **docker_compose.yml**
   - Defines the Docker Compose configuration
   - Sets up PostgreSQL database service
   - Configures networking and volumes

## Next Steps

1. **Local Development**
   - Start local development environment
   - Create and test DAGs locally

2. **DAG Development**
   - Create DAGs in the `dags/` directory
   - Implement data pipelines

3. **Testing**
   - Write tests in the `tests/` directory
   - Ensure DAGs work as expected

4. **Deployment**
   - Configure deployment settings
   - Deploy to Astro platform

## Useful Commands

```bash
# Start local development environment
astro dev start

# Stop local development environment
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

## Notes

- The project is set up with a Python virtual environment (`venv/`)
- Docker is required for local development
- Make sure to activate the virtual environment before running Astro commands
- Keep the `requirements.txt` updated with any new dependencies
- The weather ETL pipeline runs daily by default
- Database connections are managed through Airflow's connection interface
- Proper error handling and resource cleanup are implemented in the DAG

## References

- Weather ETL Pipeline Implementation: [@https://youtu.be/Y_vQyMljDsE](https://youtu.be/Y_vQyMljDsE) 