#각각 입력받기
#무조건 문자열로 인식해서 수식 사용시 형변환 필수!
a=int(input("a의 나이는?"))
b=int(input("b의 나이는?"))

print(a,b)

#공백(기호 등) 기준으로 2개의 입력값으로 인식하기
c, d = input("입력해봐라 : ").split(",")
c=int(c)
d=int(d)

print('a는 {}살이고, b는 {}살이다.'.format(c,d))