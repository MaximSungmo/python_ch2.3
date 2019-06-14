import sys

i1 = 10
i2 = 10
# 같은 객체인 지 확인, 변수는 같은 객체를 참조한다.
# 불변으로 상수풀이 운영이 되는 것으로 보임
print(hex(id(i1)), hex(id(i2)))

# 리스트는 다른 객체를 참조한다.
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

# 스트링변수는 같은 객체를 참조한다.
s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

# is (동일 레퍼런스 비교), == (동등성 비교)
print(i1 is i2)
print(l1 is l2)
print(s1 is s2)

# tuple 비교
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 is t2)
print(sys.getrefcount(t1), sys.getrefcount(t2))

# tuple을 생성자로 생성하여 동일성 비교, 새롭게 생성됨을 알 수 있음
t3 = tuple(range(1, 4))
print(t1 is t3)
print(sys.getrefcount(t3))

# 슬라이싱으로 동일한 tuple 생성하였으나 동일하지 않음 새롭게 생성된 객체임을 알 수 있음
t4 = (0, 1, 2, 3)[1:]
print(t1 is t4)

