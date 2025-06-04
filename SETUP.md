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
├── Dockerfile          # Container configuration
├── include/            # Additional files for DAGs
├── packages.txt        # System-level dependencies
├── plugins/            # Custom Airflow plugins
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── tests/              # Test files
└── venv/               # Python virtual environment
```

## Key Files and Their Purposes

1. **airflow_settings.yaml**
   - Contains Airflow configuration settings
   - Defines environment variables and connections

2. **Dockerfile**
   - Defines the container environment for Airflow
   - Specifies base image and dependencies

3. **requirements.txt**
   - Lists Python package dependencies
   - Used for installing required Python packages

4. **packages.txt**
   - Lists system-level dependencies
   - Used for installing required system packages

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

# Deploy to Astro
astro deploy

# Check Astro version
astro version

# View available commands
astro --help
```

## Notes

- The project is set up with a Python virtual environment (`venv/`)
- Docker is required for local development
- Make sure to activate the virtual environment before running Astro commands
- Keep the `requirements.txt` updated with any new dependencies 