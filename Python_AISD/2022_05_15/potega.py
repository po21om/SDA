#
#
# def power(x, y) -> float:
#     if y > 1:
#         if y % 2:
#             return power((y-1)/2, (y+1)/2)
#         else:
#             return power(y/2, y/2)
#     else:
#         return x * y
#
#
# #print(power(2, 4))
#
#
# def pow_bin(x, y):
#     # print(bin(y))
#     # print(bin(y)[:1:-1])
#     for i,n  in enumerate(bin(y)[:1:-1]):
#         print(n)
#         if n and y > 1:
#             pow_bin(x, int(('0b'+'1'+'0'*i), 2))
#     return x*x
#
# print(pow_bin(2, 2))

def bin_pow(x, y):
    z = 1
    while y > 0:
        if y % 2:
            z *= x
        x *= x
        y //= 2
    return z


print(bin_pow(2, 4632))
