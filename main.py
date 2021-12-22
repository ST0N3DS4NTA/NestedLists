if __name__ == '__main__':
    lst = []
    lowestGrade = None
    for i in range(int(input())):
        newList = []
        name = input()
        score = float(input())
        lst.append([name, score])

    for i in range(len(lst)):
        if lowestGrade is None or lst[i][1] < lowestGrade:
            lowestGrade = lst[i][1]
            print(lowestGrade)
