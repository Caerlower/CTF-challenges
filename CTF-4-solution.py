from algosdk import transaction, account, util
from algosdk.v2client import algod
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get private key and address from environment variables
private_key = os.getenv("PRIVATE_KEY")
address = account.address_from_private_key(private_key)
print("Address:", address)

# Get Algorand client parameters from environment variables
algod_token = os.getenv("TESTNET_ALGOD_TOKEN")
algod_url = os.getenv("TESTNET_ALGOD_URL")
algod_port = os.getenv("TESTNET_ALGOD_PORT")

# Initialize Algorand client
algod_client = algod.AlgodClient(algod_token, algod_url)

# Get suggested transaction parameters
suggested_params = algod_client.suggested_params()

