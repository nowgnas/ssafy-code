'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=1959&orderBy=FIRST_REG_DATETIME&selectCodeLang=JAVA&select-1=2&pageSize=10&pageIndex=1


2
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3


'''


def compare(big: list, small: list):
    result = 0
    for item in range(len(big)-len(small)+1):
        maxNum = 0
        for idx in range(len(small)):
            maxNum += big[item+idx] * small[idx]
        if result < maxNum:
            result = maxNum
    return result


n = int(input())
for index in range(n):
    res = 0
    a, b = map(int, input().split())
    if a > b:
        bigArray = list(map(int, input().split()))
        array = list(map(int, input().split()))
        res = compare(bigArray, array)
        print(f'#{index+1} {res}')

    elif a < b:
        array = list(map(int, input().split()))
        bigArray = list(map(int, input().split()))
        res = compare(bigArray, array)
        print(f'#{index+1} {res}')
