# --------------------------------------------------
# File Name : 12_Class_JTP.py
# Problem   : Big Wallet
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------


class BigWallet:
    # Initialize the wallet with given bank notes types
    def __init__(self, bank_notes):
        self.wallet = {}
        for bank_note in bank_notes:
            self.wallet[bank_note] = 0

    # Check if the note is valid
    def valid_note(self, bank_note):
        return bank_note in self.wallet

    # Add bank notes to the wallet
    def add(self, bank_note, amount):
        if self.valid_note(bank_note):
            self.wallet[bank_note] += amount

    # Calculate the total amount in the wallet
    def total(self):
        return sum(self.wallet.values())

    # Compare two wallets, return True if the current wallet is less than the rhs wallet
    def __lt__(self, rhs):
        return self.total() < rhs.total()
