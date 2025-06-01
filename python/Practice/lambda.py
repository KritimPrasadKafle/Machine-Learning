def square(x):
    return x**2

answer = square(4)
print(answer)

s = lambda x : x**2
answer1 = s(2)
print(answer1)

#list comprehension

answer = []
def filteration(x):
    n = len(x)
    for i in range(n):
        if i % 2 == 0:
            answer.append(i)
    return answer

ans = [1,2,3,4,5,6,7,8,9,0]
print(filteration(ans))



answer = list([lambda x: i for i in range(1,x) if x%2==0])
print(answer[1,2,3,4])


a = [3, 4, 5]
b = [i for i  in a  if i > 4]

#Or (filter is this case; map could also be more appropriate in other cases)
b = filter(lambda x: x > 4, a)


def is_stop_sign(sign):
    return sign.color == 'red' and sign.sides == 8

if is_stop_sign(sign):
    stop()