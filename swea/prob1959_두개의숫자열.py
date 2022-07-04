'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=1959&orderBy=FIRST_REG_DATETIME&selectCodeLang=JAVA&select-1=2&pageSize=10&pageIndex=1

'''


def compare(big: list, small: list):
    for item in range(len(big)-len(small)+1):
        maxNum = 0
        for idx in range(len(small)):
            maxNum += big[]

    pass


def main():
    n = int(input())
    for index in range(n):
        a, b = map(int, input().split())
        if a > b:
            bigArray = list(map(int, input().split()))
            array = list(map(int, input().split()))
            compare(bigArray, array)

        elif a < b:
            array = list(map(int, input().split()))
            bigArray = list(map(int, input().split()))
            compare(bigArray, array)


if __name__ == '__main__':
    main()
