#if item in memo retrieve it, otherwise calculate it

def fibonacci_memoization(num, memo={}):
    if num == 0:
        memo[0] = 0
    if num == 1:
        memo[1] = 1
    #print(memo)
    if num in memo:
        return memo[num]
    else:
        memo[num] = fibonacci_memoization(num - 2, memo) + fibonacci_memoization(num - 1, memo)
        return memo[num]
    
    
    
