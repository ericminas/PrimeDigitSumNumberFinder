import json
import sys


def getDigits(number):
    num_str = str(number)
    digits = [int(digit) for digit in num_str if digit.isdigit()]
    return digits


def isSavedPrime(number):
    with open("primenumbers.json", "r") as file:
        data = json.load(file)
        if "primenumbers" in data:
            if number in data["primenumbers"]:
                return True
    return False


def areDigitsPrime(digits):
    for d in digits:
        if not isSavedPrime(d):
            return False
    return True


def isDigitSumPrime(digits):
    sum = 0
    for d in digits:
        sum += d

    return isSavedPrime(sum)


def isNumberReachable(digits, number):
    # multiple of digit
    for d in digits:
        if number % d == 0:
            return True

    for d1 in digits:
        for d2 in digits:
            if (number - d1) < 0:
                return False
            if (number - d1) % d2 == 0:
                return True

    return False


def digitsSatisfyAdditionProperty(digits):
    # get the highest digit
    highestDigit = max(digits)

    for i in range(highestDigit, highestDigit + 50):
        if not isNumberReachable(digits, i):
            return False
    return True


def checkNumber(number, additionProp):
    isPrime = isSavedPrime(number)
    digits = getDigits(number)
    requirements = areDigitsPrime(digits) and isDigitSumPrime(digits)

    if requirements:
        if additionProp:
            return (
                number,
                "prime" if isPrime else "not-prime",
                "strong" if number < 100 else "not strong",
                "addition property fulfilled"
                if digitsSatisfyAdditionProperty(digits)
                else "addition property not fulfilled",
            )

        return (
            number,
            "prime" if isPrime else "not-prime",
            "strong" if number < 100 else "not strong",
        )


def printResult(result):
    if result is not None:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python finder.py start end primeonly")
    else:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            primeonly = (sys.argv[3]) == 1 or str(sys.argv[3]).lower() == "true"
            additionProp = (sys.argv[4]) == 1 or str(sys.argv[4]).lower() == "true"
        except ValueError:
            print(
                "Please enter valid integer values for start and end and 0/1 for primeonly."
            )

    # summary
    print(
        "starting at: ",
        start,
        "\nup to: ",
        end,
        "\nusing only prime numbers" if primeonly else "using all numbers.",
        "\n"+("" if additionProp else "not ") + "checking addition property.",
        "\n"
    )

    if primeonly:
        with open("primenumbers.json", "r") as file:
            data = json.load(file)

            numbers = data["primenumbers"]
            for number in numbers:
                if start <= number and number <= end:
                    printResult(checkNumber(number, additionProp))

    else:
        for number in range(start, end):
            printResult(checkNumber(number, additionProp))
