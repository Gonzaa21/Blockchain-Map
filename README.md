# 🔗 Map Blockchain

Blockchain prototype built in Python that simulates transactions and integrates procedurally generated token maps using Perlin noise. Each transaction is stored in a mined block, and each block includes a unique map hash to enhance security and identity.

> The project used this submodule: [generator-token-maps](https://github.com/Gonzaa21/generator-token-maps)

## 🚀 Features

- Custom blockchain implementation using linked lists.
- Block mining with proof-of-work (adjustable difficulty).
- Transaction management with sender, recipient, and amount.
- Procedural map generation (token) with Perlin noise.
- Each block includes a unique map hash for validation.
- Blockchain integrity validation on every run.

## 🛠️ Project Structure
```
Map-blockchain/
├── blockchain/
│   ├── blockchain.py
│   └── miner.py
├── generator_code/
│   ├── generator.py
│   ├── hash_utils.py
│   └── config.json
├── models/
│   └── block.py
├── utils/
│   └── utils.py
├── main.py
├── requirements.txt
└── README.md
```

# 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gonzaa21/Blockchain-Map.git
   cd Map-blockchain
   ```

2. Create a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```