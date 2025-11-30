# Eth Wallet Watcher

Get ETH balance and most recent 5 on-chain transactions for any address.

## Usage

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Set `ETH_RPC` in your `.env` file (Infura/Alchemy or public endpoint).

2. Run the watcher:
   ```sh
   python wallet_watcher.py
   ```
   Input ETH address and receive:
   - Balance in ETH
   - Recent 5 transactions with details

---

**Technical Note:**
Iterates over recent blocks for demonstration. In production, integrate with Etherscan or similar APIs for efficient query.
