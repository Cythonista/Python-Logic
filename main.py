from Logic import Logic

def main():
    logic = Logic()
    
    a = 0
    b = 1

    y = logic.AND(a, b)
    print(y)

    y = logic.OR(a, b)
    print(y)

    y = logic.NOT(a)
    print(y)

    y = logic.NAND(a, b)
    print(y)

    y = logic.SNAND(a)
    print(y)

    y = logic.NOR(a, b)
    print(y)

    y = logic.XOR(a, b)
    print(y)

    y = logic.XNOR(a, b)
    print(y)


if __name__ == '__main__':
    main()
