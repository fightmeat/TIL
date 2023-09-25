def onetwofour(q):
    number = ''
    reminder = '412'  # list와 동일한 표현
    while q:
        q, r = divmod(q, 3)
        number = reminder[r] + number
        if not r: 
            q -= 1
    return number

if __name__ == "__main__":
    num = int(input("숫자 입력  "))
    for i in range(1, num+1):
        print(" %d : %s" % (i, onetwofour(i)))