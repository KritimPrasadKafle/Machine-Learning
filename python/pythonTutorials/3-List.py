courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)

#Accessing
print(courses[0])

print(courses[3])

print(courses[-1])

#Slicing
print(courses[0:2])

print(courses[:2])

print(courses[2:])

#Methods
courses.append('Art')
print(courses)

print(courses.index('Art'))

courses.insert(0,'Hello')

print(courses)

courses_2 = ['Art', 'Education']

courses.insert(0, courses_2)
print(courses_2)

print(courses)
courses.append(courses_2)
print(courses)
courses.extend(courses_2)
print(courses)


courses.remove('Math')
print(courses)

courses.pop()
print(courses)

check1 = ['hello', 'hey']
check2 = ['ho', 'yes', 'and']

check1.insert(2, check2)
print(check1)

check1.pop()
print(check1)
courses1  = ['History', 'Math', 'Physics', 'CompSci']

courses1.sort()
print(courses1)
print(courses1)
courses1.reverse()
print("Reverse",courses1)

check22 = ['hehh', 'aaa', 'yyy', 'dddd', 'ooo']

check22.sort(reverse=True)
print(check22)

num10 = [1,3,4,56]
print(sum(num10))

print('Art' in check22)



# sorted_courses = sorted(courses)

# print(sorted_courses)


for item in enumerate(check22, start = 1):
    print(item)

print(check22)

course_str = ', '.join(check22)
print(course_str)


new_list = course_str.split(' - ')
print(new_list)

# new_list = check22.split(' - ')
# print(new_list)

hello = ['fkjdsf-fsjkjsdf', 'dskjdfs-rejk', 'fsdjk-']
hello_str1 = ', '.join(hello)
print(hello_str1)

hello_str2 = hello_str1.split(' - ')
print(hello_str2)
# hello_str = hello.split(' - ')

# print(hello_str)