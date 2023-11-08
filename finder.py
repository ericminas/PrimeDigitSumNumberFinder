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


def checkNumber(number):
    isPrime = isSavedPrime(number)
    digits = getDigits(number)
    requirements = areDigitsPrime(digits) and isDigitSumPrime(digits)

    if requirements:
        return (
            number,
            "prime" if isPrime else "not-prime",
            "strong" if number < 100 else "not strong",
        )


def printResult(result):
    result = checkNumber(number)
    if result is not None:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python finder.py start end primeonly")
    else:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            primeonly = (sys.argv[3]) == 1 or str(sys.argv[3]).lower() == "true"
        except ValueError:
            print(
                "Please enter valid integer values for start and end and 0/1 for primeonly."
            )

    # summary
    print(
        "starting at: ",
        start,
        "up to: ",
        end,
        "using only prime numbers" if primeonly else "using all numbers",
    )

    if primeonly:
        with open("primenumbers.json", "r") as file:
            data = json.load(file)

            numbers = data["primenumbers"]
            for number in numbers:
                if start <= number and number <= end:
                    printResult(checkNumber(number))

    else:
        for number in range(start, end):
            printResult(checkNumber(number))
