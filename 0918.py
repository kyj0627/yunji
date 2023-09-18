""" num = input("숫자 입력") 
print("number", int(num))
 """

""" a = 12
print(type(a))
a= 12.01
print(type(a))
a="a"
print(type(a))
a="abcd"
print(type(a))
a = [3,2,1]
print(type(a)) """

""" a=65
print(int(a))
print(str(a))
print(hex(a))
print(oct(a))
print(chr(a))
print(ord("A")) """

#문자표현 : 숫자 코드로 매핑, 숫자 ↔ 문자 변환 표현

""" print(pow(2,2))
print(pow(2,6))
print(pow(3,4)) """

#print(divmod(10,3))
#print(round(3.14)) 
""" a = (3,5,7)
b=list(a)
c=tuple(b)

print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) """

""" for i  in range(2,7):
    print(i)

for i in range(6):
    print(i)
for i in range(1, 20, 3):
    print(i) """


""" a = [3, 5, 6, 9]
print(max(a))
print(min(a))
print(sum(a))

print(abs(-3))
print(abs(3.0))
print(abs(-3.0))

a = [5,3,1,9,4]
print(sorted(a))
print(sorted(a, reverse=True))

a = [5, 3.14, False, 9, "string"]
print(enumerate(a))
print(*enumerate(a)) """

""" a= [True, True, False]
b = [True, True, True]
print(any(a))
print(all(a))
 """

""" a= 20
b=23
c="a는 {}, b는 {}, {}".format(a, b, "python") """

""" a=3
print(globals())
print(locals())
print(drive(a)) """

""" add = lambda a, b : a + b
sub = lambda a, b : a-b
mul = lambda a, b: a * b
div = lambda a, b : a /b
print(add(2, 3)) 
print(sub(2, 3)) 
print(mul(2, 3)) 
print(div(2, 3))  """


""" def function(parameter):
    return result

def add_numbers(x, y):
    return x + y

result = add_numbers(4, 5)
print(result)
 """
""" def greet(name):
    print(name)
    print("Hello, " + name + ". How are you?")
greet("python") """

""" def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
sub(3, 5)
mul()
div() """

""" def is_even(n):
    if n % 2 = 0:
        print("짝수")
    else: 
        print("홀수")

num = input ("숫자 입력 : ")
is_even(int(num)) """

""" def reverse_strung(msg)
    return msg[::-1]
in_str = input("문자열 : ")
print(reverse_string(in_str)) """

""" def sub(a,b) :
    return int(a) - int(b)

def mul(a,b) :
    return int(a) = int(b)
def div(a,b) : 
    return int(a) / int(b)

a = input("a를 입력하세요")
b = input("b를 입력하세요")

print("더ㅓ하기: =, add(a,b)")
print("빼기: ", sub(a,b))
print("곱하기 :" ,mul (a,b))
print("나누기:" div(a, b))
 """

""" def calc(a, b):
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) = int(b))
    print(int(a) / int(b))

a = input("a를 입력하세요")
b = input("b를 입력하세요")

calc(a,b)


def sum_num(num):
    return sum(num)

nums = []

for i in range(1, 6):
    innum = int(input(f"{i} 번째 숫자 입력: "))
    nums.append(innum)

print(sum_num(nums))
 """
