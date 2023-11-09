# PrimeDigitSumNumber Finder
A program that finds all numbers up to a given max_value, that fulfill the following criteria:
1. The digits of the number are all prime numbers
2. The sum of the digits is a prime number as well

The number is a string prime-digit-prime-number, if it is less than 100 and or the number is a prime.

An additional property is:
Whether the digits of the number can be used to get all numbers bigger than the highest digit.
Example: 23 -> 2,3. 

2 and 3 can be used to create 4 (2+2), 5 (3+2), 6 (3+3), 7(2+2+3), ....

The exact check is whether the digits can create the next 50 numbers. If that is the case, we expect them to be able to create all higher numbers.

## Usage
```python finder.py start end primeOnly additionProp```
with:
| argument name | description |
|---------------|-------------|
| start         | The first number that should be checked (inclusive) |
| end           | The last number that should be checked (inclusive) |
| primeOnly     | Whether only prime numbers should be checked (1, true.lower()) |  
| additionProp  | Whether the number should have the addition propert (described above) (1, true.lower()) |
