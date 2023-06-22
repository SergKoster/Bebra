# a = input('введи строику: ')
# def str_str(str):
#     for i in str:
#         count = 0
#         for j in str:
#             if i == j:
#                 count +=1
#
#         print(count)
#
# str_str(a)
#
# def counter(s):
#     for i in set(s):
#         o_counter = 0
#         count = 0
#         for j in s:
#             if i == j:
#                 count += 1
#         print(i, count)

def counter(s):
    sums = {}
    for i in s:
        sums[i] = sums.get(i, 0) + 1
    for i, count in sym.items():
        print(i, count)