import timeit


def sieve_of_eratosthenes(min_integer, max_integer):
    sieve = [True for x in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(min_integer, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes


def find_largest_palindrome(primes):
    max_palindrome = [0, 0, 0]
    x = 0
    for i in range(len(primes)):
        for j in range(len(primes) - x):
            temp = primes[j] * primes[i]
            if temp > max_palindrome[0] and str(temp) == str(temp)[::-1]:
                max_palindrome = [temp, primes[j], primes[i]]
        x += 1
    return max_palindrome


def main():
    start = timeit.default_timer()
    primes = sieve_of_eratosthenes(10000, 99999)
    max_palindrome = find_largest_palindrome(primes)
    stop = timeit.default_timer()
    print("The largest number-palindrome, which is the product of two prime five-digit is: {} \n"
          "It is the product of {} and {}\n"
          "Computing takes: {} seconds".format(max_palindrome[0], max_palindrome[1], max_palindrome[2], stop - start))


main()
