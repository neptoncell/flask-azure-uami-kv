from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

keyvault_name = "kv-flask-demo"
secret_name = "sahbi"
KVUri = f"https://{keyvault_name}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

@app.route("/")
def index():
    try:
        secret = client.get_secret(secret_name)
        secret_value = secret.value
    except Exception as e:
        secret_value = f"Erreur lors de la lecture du secret : {e}"
    return f"Le secret est : {secret_value}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
