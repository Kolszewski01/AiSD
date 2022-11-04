#1 ZAD
def numbers(n: int):
    if n < 0:
        return
    print(f'n: {n}')
    numbers(n - 1)

#2 ZAD
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

#3 ZAD
def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    return number * power(number, n - 1)

#4 ZAD
def reverse(txt: str) -> str:
    if txt == '':
        return ''
    return reverse(txt[1:]) + txt[0]

#5 ZAD
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return factorial(n - 1) * n

#6 ZAD
def prime(n: int, x: int):
    if n == 1:
        return False
    if x == 1:
        return True
    if n % x == 0:
        return False
    else:
        return prime(n, x - 1)



#9 ZAD
def remove_duplicates(txt: str) -> str:
    if len(txt) == 1:
        return txt[0]
    if txt[0] != txt[1]:
        return txt[0] + remove_duplicates(txt[1:])
    else:
        return remove_duplicates(txt[1:])



def main() -> None:
    numbers(5)
    print(fib(5))
    print(power(5, 5))
    print(reverse('PiS'))
    print(factorial(6))
    print(prime(23, 13))
    print(remove_duplicates("łup"))


main()