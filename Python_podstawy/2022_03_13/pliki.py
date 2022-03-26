# f = open("readme.txt")
#
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line.rstrip())
#
# for line in f:
#     print(line.rstrip())
# f.close()


with open("readme.txt") as f: # close() automatycznie
    # for line in f:
    #     print(line.rstrip())
    all_lines = f.readlines()
    print(all_lines)
    print(f.name)
    print(f.encoding)


