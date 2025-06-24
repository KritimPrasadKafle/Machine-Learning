# with open('test.txt', 'r') as f:
#     pass

# print(f.closed)

# f = open('test.txt', 'r+')
# print(f.mode)

# f.close() #should have to close the file or else you end up leaking the info if we use  f = open() but with it will close automatically.


# with open('test.txt', 'r') as f:
#     # f_contents = f.read()
#     # print(f_contents)

#     # f_contents = f.readline()
#     # print(f_contents, end = '')


#     size_to_read = 100

#     f_contents = f.read(size_to_read)

#     while len(f_contents) > 0:
#         print(f_contents, end = '')
#         f_contents = f.read(size_to_read)

#     print(f.tell())

with open('test.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Rsdfsfdfds')

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('bronx.jpg', 'rb') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)