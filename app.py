<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/hello2')
def hello2():
    return "Hello World2"

@app.route('/hello3')
def hello3():
    return "Hello World3.2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Ensure the app runs on port 80
=======
from flask import Flask
import psycopg2
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError

app = Flask(__name__)

# Azure Key Vault details
KEY_VAULT_NAME = 'hello-world-kv-2'
SECRET_NAME = 'your-secret-name'

# Function to retrieve secret from Azure Key Vault
def get_secret(secret_name):
    # Create a SecretClient
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=f"https://{KEY_VAULT_NAME}.vault.azure.net/", credential=credential)
    
    try:
        secret = secret_client.get_secret(secret_name)
        return secret.value
    except ResourceNotFoundError:
        raise Exception(f"Secret '{secret_name}' not found in Azure Key Vault '{KEY_VAULT_NAME}'")


# Azure PostgreSQL connection details
DB_HOST = 'helloworld-db.postgres.database.azure.com'
DB_NAME = 'helloworld-db'
DB_USER = 'helloworldadmin'
DB_PASSWORD = 'Efecenk2486'

# Connect to the Azure PostgreSQL database
connection = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

@app.route('/hello')
def hello():
    # Example SQL query
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM todo")
        result = cursor.fetchall()

    return str(result)

@app.route('/hello2')
def hello2():
    return "Hello World2"

# Merged HelloWorld3
@app.route('/hello3')
def hello3():
    return "Hello World3.2"

# Close the database connection when the application terminates
@app.teardown_appcontext
def close_connection(exception):
    if connection is not None:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> ae2b84c724d8cc3f73037beef4abd2ca3c50de2a
