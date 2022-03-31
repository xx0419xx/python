#리스트 값 삭제 방법3가지

number =["pink","orange",1,4]
print(number)

#1. 요소값
number.remove(1)
print(number)

#2. 인덱스값
number.pop(2)
print(number)

#3. 그렇다
del(number[1])
print(number)