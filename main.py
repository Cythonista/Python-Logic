from Logic import Logic

def main():
    logic = Logic()

    # 1入力 1出力
    a = [0, 1]
    logic.summaryA(a, logic.NOT)
    logic.summaryA(a, logic.SNAND)

    # 2入力 1出力
    a = [0, 0, 1, 1]
    b = [0, 1, 0, 1]
    logic.summaryAB(a, b, logic.AND)
    logic.summaryAB(a, b, logic.OR)
    logic.summaryAB(a, b, logic.NAND)
    logic.summaryAB(a, b, logic.NOR)
    logic.summaryAB(a, b, logic.XOR)
    logic.summaryAB(a, b, logic.XNOR)

    # 3入力 1出力
    a = [0 ,0, 0, 0, 1, 1, 1, 1]
    b = [0 ,0, 1, 1, 0, 0, 1, 1]
    c = [0 ,1, 0, 1, 0, 1, 0, 1]
    logic.summaryABC(a, b, c, logic.TAND)
    logic.summaryABC(a, b, c, logic.TOR)


if __name__ == '__main__':
    main()
