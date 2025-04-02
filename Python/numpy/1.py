import numpy as np
# import time
# import sys
# # a = np.array([1,2,3])
# # print(a[0])
# # print(a[1])
#
# #
# # l = range(1000)
# # print(sys.getsizeof(5)*len(l))
# #
# # array = np.arange(1000)
# # print(array.size*array.itemsize)
# #
# # SIZE = 1000
# #
# # l1 = range(SIZE)
# #
# # l2 = range(SIZE)
# #
# # a1 = np.arange(SIZE)
# # a2 = np.arange(SIZE)
# #
# # start = time.time()
# #
# # result = [(x+y) for x,y in zip(11,12)]
# # print("Python list took: ", (time.time()-start)*1000)
# # start = time.time()
#
# a1 = np.array([1,2,3])
# a1 = np.array([4,5,6])
#
# print(a1+a2)
#
# result = a1+a2
# print("numpy took :", (time.time()-start)*1000)
#

#
# import numpy as np
#
# a = np.array([5,6,9])
# print(a[0])
#
# a = np.array([[1,2],[3,4],[5,6]])
# print(a.ndim)
#
# print(a.itemsize)
#
# print(a.dtype)
#
# a = np.array([[1,2], [3,4], [5,6]], dtype = np.float64)
# print(a.itemsize)
# print(a.dtype)
#
# print(a)
#
# b = np.array([[1,2],[3,5],[6,9]], dtype = complex)
# print(b.dtype)
# print(b.shape)
#
#
# s = np.zeros((3,4))
# print(s)
#
# s = np.ones((4,5))
# print(s)
#
# d = range(5)
# print(d)
# print(d[0])
#
# print(np.arange(1,5))
#
#
# print(np.linspace(1,5,10))

# a = np.array([[1,2,3],[2,5,4]])
# print(a.shape)
#
# print(a.reshape(6,1))
#
# print(a.ravel())
# print(a)
#
# print(a.min())
# print(a.max())
#
# print(a.sum())
#
# print(a.sum(axis=0))
#
# print(a.sum(axis=1))
#
# # print(a.sqrt())
# print(np.sqrt(a))
#
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# print(a)
# print(b)
#

#
# import numpy as np
# n = [6,7,8]
# print(n[0:2])
# print(n[-1])
#
# b = np.array([6,7,5])
# print(b[0:2])
#
#
#
# a = np.array([[1,2,3],[6,7,8],[9,3,2]])
#
#
# print(a)
#
# print(a[1,2])
#
# print(a[0:2,2])
#
# print(a[:,1:3])
#
# a = np.array([[6,5,7], [2,3,4], [9,3,5]])
#
# print(a)
#
# for row in a:
#     print("Row:",row)
#
# print(a.ravel())
#
# # for i in a.flat:
# #     print(i)
#
# a = np.arange(6).reshape(3,2)
# b = np.arange(6,12).reshape(3,2)
#
# print(a)
#
# s = np.arange(4,9,1, dtype=int)
# print("SSS:", s)
#
# print("sssss",np.vstack((a,b)))
#
# print("sssss",np.hstack((a,b)))

s = np.arange(12).reshape(3,4)
# print(s)

# for row in s:
#     for col in row:
#         print(col)

# for row in s.flatten():
#     print(row)

# for x in np.nditer(s, order='C'):
#     print(x)

# for x in np.nditer(s, order='F'):
#     print(x)

# for x in np.nditer(s, order='F', flags=['external_loop']):
#     print(x)

for x in np.nditer(s, op_flags=['readwrite']):
    x[...]=x*x

print(s)
print(x)
