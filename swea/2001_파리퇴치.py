'''https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=2001&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29

'''


def solution(n, m, table: list):
    # n이 15 이하이므로 완전 탐색이 가능하다
    sumList = []
    for idx1 in range(n-m+1):
        eachSum = 0
        for idx2 in range(n-m+1):
            for idx3 in range(m):
                for idx4 in range(m):
                    eachSum += table[idx1+idx3][idx2+idx4]
            sumList.append(eachSum)
            eachSum = 0
    return max(sumList)


t = int(input())
for item in range(t):
    n, m = map(int, input().split())
    table = []
    for idx in range(n):
        table.append(list(map(int, input().split())))
    result = solution(n, m, table)
    print(f'#{item+1} {result}')
