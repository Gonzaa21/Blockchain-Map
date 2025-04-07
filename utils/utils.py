def transaction_input() -> dict:
    id = input(f"\033[90mTu nombre o ID: \033[0m").strip()
    recipient = input(f"\033[90mDestinatario: \033[0m").strip()
    amount = float(input(f"\033[90mMonto a transferir: \033[0m"))

    return {
        "from": id,
        "to": recipient,
        "amount": amount
    }