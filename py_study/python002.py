import numpy as np

# 문제 1
print('makit "code" lab')
print("she's gone")
print('====================================')
# 문제 2
a = 10
b = 20
c = a + b
print('a와 b의 합은', c)
print('====================================')
# 문제 3
b = 'makit '
print(a * 3)
print(b * 3)
print('====================================')

# 문제4
a = ['메이킷', '우진', '시은']
print(a)
print(a[0])
print(a[1])
print(a[2])
print('====================================')

# 문제5
a = ['메이킷', '우진', '제임스', '시은']
print(a[0], a[1])
print(a[1:4])
print(a[2:4])
print(a[0:4])
print('문제 5====================================')

# 문제 6
a = ['우진', '시은']
b = ['메이킷', '소피아', '하워드']
print(a + b)
print(b)
print('====================================')

# 문제 7
print(a)
print(b + a)
print('================ extend() ====================')
b.extend(a)
print(b)

# 문제 8
a = np.array([[1,2,3], [4,5,6]])
print("original :\n", a)

a_transpose = np.transpose(a)
print("Transpose: \n", a_transpose)
print('====================================')

# 문제 9
b = np.array([[1,2,3], [4,5,6]])
print("Original :\n", a)

b_reshape = np.reshape(a, (3, 2))
print("reshape: \n", b_reshape)
print('====================================')



