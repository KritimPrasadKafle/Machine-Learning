import os

os.chdir('/home/kritim/Documents')

print(os.getcwd())

# for f in os.listdir():
#     # print(f)
#     # print(os.path.splitext(f))
#     f_name, f_ext = os.path.splitext(f)
#     # print(file_name.split('-'))

#     f_title, f_course, f_num = f_name.split('-')
#     print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

s = 'dsffdsfdf             '
j = s.join(',')
print(j)
print(len(s))
print(len(s.strip()))

import random 
s = random.randrange(2,12,2)


print(s)