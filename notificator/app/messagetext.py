def SendCode(code):
    return f"Your code to verify your transaction: {code}"

def SuccessfullyMoneyTransfer(recipientId, Amount):
    return f"The transaction was completed successfully! Recipient: {recipientId} | Amount: {Amount}"

def UnsuccessfullyMoneyTransfer(recipientId, Amount):
    return f"The transaction was completed unsuccessfully! Recipient: {recipientId} | Amount: {Amount}"