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
    for i in range(10,1,-1) :
        print("hola")

if __name__ == '__main__':
    main()

