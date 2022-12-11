# def my_func(i, j, k):
#   a, b, *c = range(i, j, k)
#   return a, b, c
#
#
# i, j, k = 6, 11, 2
#
# if __name__ == "__main__":
#   a, b, c = my_func(i, j, k)
#   print(a, b, c)
# def my_func(n):
#   x = 0
#   while n:
#     n //= 5
#     x += n
#   return x
#
# n = 120
#
# if __name__ == "__main__":
#   x = my_func(n)
#   print(x)
# x=10
# def func():
#     global x
#     x+=30
#     print(x)
# func()
# print(x)
#
# if True or True:
#     if False and True or False:
#         print('A')
#     elif False and False or True and True:
#         print('B')
#     else:
#         print('C')
# else:
#     print('D')
#
# var = 10
# def foo():
#   var = 15
# foo()
# print(var)

# for i in range(1,5,-1):
#     print('*'*i)

# t=(1,'abc',2+3j)
# print(type(t[2:3]))

# a=[3,4,9,0,1,12,5]
# b = a.sort()
# print(b)

# a = [(lambda x: x * 2)(x) for x in range(5)]
# print(a)

# def fun(d, e, a=9, b=1):
#     pass

# list = list(range(1,0,0))
# for i in list:
#     print(i)

# def my_func(num):
#   data = [0]
#   for i in range(1, num+1):
#     data.append(data[i >> 1] + int(i & 1))
#   return data
#
#
# num = 6
# print(my_func(num))

# l1 = []
# l2 = []
#
# if l1 is l2:
#     print("Same")
# else:
#     print("Different")

# circle_areas = [3.54773, 5.57778, 4.00014, 59.24241, 34.01344, 32.01013]
#
# result = list(map(round, circle_areas, range(1,3)))
# print(result)

# def my_func(s, z):
#   total = 0
#   len_str = len(s)

#   for x, y in z:
#     if x == 0:
#       total += y
#     else:
#       total -= y
#   total = total % len_str
#   print(s[total:] + s[:total])

# s = 'cutshort'
# z = [[0, 3], [1, 11]]

# if __name__ == "__main__":
#   my_func(s, z)

# def my_func(st):
#   l1 = [ch for ch in st if ch.isalpha()]
#   return ''.join(l1.pop() if ch.isalpha() else ch for ch in st)
#
#
# st = 'ab-cd-ef'
# print(my_func(st))