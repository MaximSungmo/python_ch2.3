# 레퍼런스 복사
import copy

a = 1
b = a

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = x

# 레퍼런스 복사하는 것은 동일한 레퍼런스 (동일 객체)
print(x)
print(y)
print(x is y)

# swallow copy(얕은 복사)
# copy를 시킨 경우에는 새로운 객체가 만들어지긴 하지만 참조하는 변수들은 동일하게 참조함
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.copy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])
print(x[1][2] is y[1][2])
# deep copy(깊은 복사)
# deepcopy를 시킨 경우에는 새로운 객체가 만들어지면서 참조중인 변수 모두 내용을 가져와서 copy함
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.deepcopy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])
print(x[1][2] is y[1][2])

# 깊은 복사는 복합 객체를 새롭게 생성하기 때문에 아래와 같은 예시에서는 불필요하다.
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])

