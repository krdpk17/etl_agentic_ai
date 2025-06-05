from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from datetime import datetime, timedelta
import requests
import json


#latituee and longitude of the city
LATITUDE = '51.5074' #london
LONGITUDE = '-0.1278' #london
POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1)
    }

## DAG

with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:

    @task()
    def extract_weather_data():
        #Extract the weather data from open meteo api using airflow connection
        http_hook = HttpHook(method='GET', http_conn_id=API_CONN_ID)

        #Build an API endpoint to get the weather data https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true
        endpoint = f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'
        response = http_hook.run(endpoint=endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch weather data: {response.status_code} {response.text}")
        
    @task()
    def transform_weather_data(weather_data):
        # Transform the extracted weather data to a more usable format
        current_weather = weather_data['current_weather']
        transformed_data = {
            'latitude': LATITUDE,
            'longitude': LONGITUDE,
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'],
            'weathercode': current_weather['weathercode']
        }
        return transformed_data
    
    @task()
    def load_weather_data(transformed_data):
        #Load the transformed weather data into postgres database
        postgres_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = postgres_hook.get_conn()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                       CREATE TABLE IF NOT EXISTS weather_data (
                       id SERIAL PRIMARY KEY,
                       latitude FLOAT NOT NULL,
                       longitude FLOAT NOT NULL,
                       temperature FLOAT NOT NULL,
                       windspeed FLOAT NOT NULL,
                       winddirection FLOAT NOT NULL,
                       weathercode INT NOT NULL,
                       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       );
                       """)
            cursor.execute("INSERT INTO weather_data (latitude, longitude, temperature, windspeed, winddirection, weathercode) VALUES (%s, %s, %s, %s, %s, %s)", (transformed_data['latitude'], transformed_data['longitude'], transformed_data['temperature'], transformed_data['windspeed'], transformed_data['winddirection'], transformed_data['weathercode']))

            conn.commit()
        finally:
            cursor.close()
            conn.close()

    ## DAG workflow - ETL pipeline
    weather_data = extract_weather_data()
    transformed_data = transform_weather_data(weather_data)
    load_weather_data(transformed_data)