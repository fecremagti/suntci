from web3 import Web3

# It's a good practice to use environment variables for sensitive information
import os
private_key = os.getenv('MY_PRIVATE_KEY')

# Ensure that you have the HTTPProvider URL in an environment variable or a config file
node_url = os.getenv('NODE_URL', 'http://localhost:8545')
web3 = Web3(Web3.HTTPProvider(node_url))

# Check if the connection to the node is successful
if not web3.isConnected():
    print("Failed to connect to the Ethereum node.")
else:
    # Define the transaction with only the necessary fields
    tx = {
        'to': '0x0123456789012345678901234567890123456789',
        'value': web3.toWei(1, 'ether'),  # Convert value to wei for clarity
        'gas': 2000000,
        'gasPrice': web3.toWei(20, 'gwei'),  # Convert gas price to wei for clarity
        'nonce': web3.eth.getTransactionCount(web3.eth.account.privateKeyToAccount(private_key).address),
    }

    # Sign the transaction
    signed_tx = web3.eth.account.signTransaction(tx, private_key)

    # Send the transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction sent! Hash: {tx_hash.hex()}")
