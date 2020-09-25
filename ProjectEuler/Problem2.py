def main():
    res = []
    ant = 0
    value = 1
    while(value < 4000000):
        aux = ant
        ant = value
        value += aux
        #print(value)
        if value%2 == 0 and value<4000000:
            res.append(value)
        


    #print(res)
    print(sum(res))

 __name__ == '__main__':
    main()


