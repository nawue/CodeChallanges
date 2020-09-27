# 
# 
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

def valid(n):
    for i in range(1,21):
        if n % i != 0:
            return False
    return True


def main():
    solve = False
    n = 2000000
    while not solve:
        if valid(n):
            solve = True
        else:
            n+=1
    return print(n)

if __name__ == '__main__':
    main()


    
