from flask import Flask
import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.keyvault.secrets.aio import SecretClient

app = Flask(__name__)

keyvault_name = "kv-flask-demo"
secret_name = "sahbi"
KVUri = f"https://{keyvault_name}.vault.azure.net"

async def get_secret():
    async with DefaultAzureCredential() as credential:
        async with SecretClient(vault_url=KVUri, credential=credential) as client:
            secret = await client.get_secret(secret_name)
            return secret.value

@app.route("/")
def index():
    secret_value = asyncio.run(get_secret())
    return f"Le secret est : {secret_value}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
