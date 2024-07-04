import json

with open('config.json', 'r') as f:
    config = json.load(f)

connection_params = config['postgres.connections'][0]
host = connection_params['host']
port = connection_params['port']
database = connection_params['database']
user = connection_params['user']
password = connection_params['password']


conn = psycopg2.connect( # type: ignore
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)