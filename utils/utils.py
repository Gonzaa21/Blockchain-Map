def transaction_input() -> dict:
    id = input(f"\033[90mName or ID: \033[0m").strip()
    recipient = input(f"\033[90mAdressee: \033[0m").strip()
    amount = float(input(f"\033[90mAmount to transfer: \033[0m"))

    return {
        "from": id,
        "to": recipient,
        "amount": amount
    }