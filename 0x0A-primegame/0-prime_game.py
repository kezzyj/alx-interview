#!/usr/bin/python3
"""
	Function for playing a prime game
"""

def count_primes(nums):
    """
    check prime numbers between 1 and n
    Args:
        int : the number to calculate prime numbers up to
    Returns:
        int: the number of prime numbers between 1 and n
    """
    count = 0

    for i in range(2, nums + 1):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count
def isWinner(x, nums):
    """
    Determines the winner of a game of prime numbers.
    Args:
        num_rounds (int): the number of rounds to play
        num_list (list): the list of numbers n to play
    Returns:
        string: the winner of the game (Ben or Maria)
    """
    if not x or not nums:
        return None
    ben_score = 0
    maria_score = 0
    for i in range(x):
        prime_count = count_primes(nums[i])
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if ben_score == maria_score:
        return None
    winner = "Ben" if ben_score > maria_score else "Maria"
    return winner
