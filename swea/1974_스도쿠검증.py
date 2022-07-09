'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=1974&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


1
7 7 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''


def solution():
    result = 1
    checkEachTable = []
    checkVertical = [[0 for _ in range(9)] for _ in range(9)]
    for idx1 in range(9):
        # 가로 줄 체크
        line = list(map(int, input().split()))
        setLine = len(set(line)) == 9
        if not setLine:
            result = 0
        checkEachTable.append(line)
        for idx2 in range(9):
            checkVertical[idx2][idx1] = line[idx2]

    table = []
    for loop in range(0, 7, 3):
        for loop2 in range(0, 7, 3):
            threeBythree = []
            for loop3 in range(3):
                for loop4 in range(3):
                    threeBythree.append(
                        checkEachTable[loop+loop3][loop2+loop4])
            table.append(threeBythree)

    for ver, tab in zip(checkVertical, table):
        # 세로 줄 체크
        lineCheck = len(set(ver)) == 9
        lineCheck2 = len(set(tab)) == 9
        if not lineCheck or not lineCheck2:
            result = 0
            break

    return result


n = int(input())
for item in range(n):
    result = solution()
    print(f'#{item+1} {result}')
