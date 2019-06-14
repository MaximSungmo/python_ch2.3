# 심볼 테이블 내용확인
g_a = 1
g_b = 'symbol'
print(globals())
# 변수를 선언해주는 경우 symbol table이 **.py(module)에 생성된다.
# globlas를 통해서 symbol_table을 확인할 수 있다. 맨 뒤에 cached 된 것을 확인.


def f():
    l_a = 2
    l_b = 'table'
    print(locals())
#
# for i in range(10):
#     g_c = 3
#     g_d = 'python'
#     print(locals())

f()

# symbol table로 관리되는 건 객체가 확장이 가능하다는 것으로 볼 수 있다.


# 1. 정의된 함수
# 함수 내에서 변수를 선언하면 함수 내에 symbol table이 있다는 것이다.
f.k = 'hello'
# 함수 내 symbol table을 확인하기 위하여 변수명.__dict__로 확인.
print(f.__dict__)

# 2. 클래스 객체에도 symbol table이 존재
class MyClass:
    x = 10
    y = 2
    def test(self):
        test = 1

# 클래스 내 symbol table에 접근하여 내용 확인
MyClass.z = 1
print(MyClass.__dict__)

num = int(1)
print(globals())

# 내장 함수는 symbol table이 없다. 확장이 불가하다.
# ex) pow.__dict__ / print.__dict__

# 내장클래스는 symbol table이 있지만 확장이 불가하다
# str.z = 10 # TypeError: can't set attributes of built-in/extension type 'str'
print(str.__dict__)

# 내장클래스로 생성된 객체는 symbol table이 없고 확장이 불가하다.
# print(g_a.__dict)

# 객체를 인스턴스로 받아서 인스턴스에 symbol table 가능, 확장이 가능 
o = MyClass()
o.z = 101
print(o.__dict__)
print(MyClass.__dict__)