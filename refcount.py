import sys

# 레퍼런스 늘리기
x = object()
print(type(x))
# x만들 때 1번, 파라미터로 넘어가서 x 다시 부를 때 한번 총 2번 호출
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(y))

# 레퍼런스 값 줄이기, symbol table을 아예 날려버림
# del은 심볼테이블에서 이름을 삭제한다.
del x
print(sys.getrefcount(y))
# print(sys.getrefcount(x))

print(globals())

