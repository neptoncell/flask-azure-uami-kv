from flask import Flask
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
import os

app = Flask(__name__)

@app.route("/")
def index():
    key_vault_name = os.getenv("KEY_VAULT_NAME")
    secret_name = os.getenv("SECRET_NAME")
    kv_uri = f"https://{key_vault_name}.vault.azure.net/"

    credential = ManagedIdentityCredential()  # utilise UAMI si configurée
    client = SecretClient(vault_url=kv_uri, credential=credential)

    secret = client.get_secret(secret_name)
    return f"Le secret est : {secret.value}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
