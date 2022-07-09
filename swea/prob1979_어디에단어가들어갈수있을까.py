'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=1979&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



2
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
6 2
1 0 0 1 0 1
1 1 0 1 1 0
1 0 1 1 1 1
0 1 1 0 1 1
0 1 1 1 0 0
0 0 0 0 1 1
'''


def solution(n, k):
    table = []
    check = '1' * k
    preZero = '0' + check
    rearZero = check + '0'
    bothZero = '0' + check + '0'
    result = 0
    verticalCheck = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        lst = list(map(str, input().split()))
        table.append(lst)

    for ver in range(n):
        for hor in range(n):
            verticalCheck[ver][hor] = table[hor][ver]

    for line1, line2 in zip(table, verticalCheck):
        lineToString = ''.join(line1)
        lineToString2 = ''.join(line2)

        if bothZero in lineToString:
            result += lineToString.count(bothZero)
        # 011과 110과 0110 구분 가능해야 함

        if preZero in lineToString or rearZero in lineToString:
            result += 1
        if preZero in lineToString2 or rearZero in lineToString2:
            result += 1

    return result


n = int(input())
for test in range(n):
    n, k = map(int, input().split())
    result = solution(n, k)
    print(f'#{test+1} {result}')
