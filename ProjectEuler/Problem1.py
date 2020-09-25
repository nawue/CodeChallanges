def main():
    res = []
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            res.append(i)
    
    print(sum(res))

if __name__ == '__main__':
    main()

