import re

def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]

def getCheckSum(string):
    checkSum = 0
    rev = string[::-1]
    for i in range(1, len(rev), 2):
        digit = int(rev[i]) * 2
        if digit > 9:
            checkSum = checkSum + 1 + digit - 10
        else:
            checkSum = checkSum + digit
    for i in range(0, len(rev), 2):
        checkSum += int(rev[i])
    return checkSum

def getCardType(string):
    if (len(string) == 13 or len(string) == 16) and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and re.match(r"5[1-5]", string[:2]):
        return "Master Card"
    return "Invalid"

cards = [
    "4003600000000014",
    "5555555555554444",
    "5105105105105100",
    "4111111111111111",
    "4012888888881881",
    "378282246310005",
]

for card in cards:
    if isValidNumber(card) and getCheckSum(card) % 10 == 0:
        print(f"{card} - {getCardType(card)}")
    else:
        print(f"{card} - Invalid")
