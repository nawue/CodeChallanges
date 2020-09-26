# 
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
#

def palindromic(number):
    tam = len(str(number)) // 2
    if (len(str(number))) % 2 != 0:
        part1 = str(number)[:tam]
        part2 = str(number)[tam+1:]
    else:
        part1 = str(number)[:tam]       
        part2 = str(number)[tam:]

    if part1 == part2[::-1]:
        return True

    return False

def main():
    big = 0
    for i in range(999,1,-1):
        for j in range(999,1,-1):
            num = i * j
            if palindromic(num) and big < num:
                    big = num
                    
    return print(big)

if __name__ == '__main__':
    main()

