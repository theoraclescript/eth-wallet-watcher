from web3 import Web3
import os
from dotenv import load_dotenv
load_dotenv()

# Use Infura or Alchemy/mainnet on a public endpoint
def get_web3():
    ETH_RPC = os.getenv('ETH_RPC', 'https://mainnet.infura.io/v3/YOUR_INFURA_KEY')
    return Web3(Web3.HTTPProvider(ETH_RPC))

def get_eth_balance_and_txs(address: str):
    w3 = get_web3()
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.fromWei(balance_wei, 'ether')
    # Use 'eth_get_transaction_by_address' (API not natively in web3.py) or etherscan as fallback
    # For portfolio demo, print last 5 known transactions blockwise
    latest = w3.eth.block_number
    txs = []
    checked = 0
    for n in range(latest, latest-5000, -1):  # Scan last 5000 blocks to find recent txs
        block = w3.eth.get_block(n, full_transactions=True)
        for tx in block.transactions:
            if tx['from'].lower() == address.lower() or tx['to'] and tx['to'].lower() == address.lower():
                txs.append({
                    "hash": tx['hash'].hex(),
                    "from": tx['from'],
                    "to": tx['to'],
                    "value": w3.fromWei(tx['value'], 'ether'),
                    "block": tx['blockNumber']
                })
                if len(txs) >= 5:
                    break
        if len(txs) >= 5:
            break
        checked += 1
    return float(balance_eth), txs

if __name__ == "__main__":
    wallet = input("Enter an Ethereum address: ").strip()
    balance, txs = get_eth_balance_and_txs(wallet)
    print(f"Balance: {balance} ETH\nLast 5 Transactions:")
    for t in txs:
        print(f"Block {t['block']}: {t['from']} -> {t['to']} | Amount: {t['value']} ETH | Hash: {t['hash']}")
