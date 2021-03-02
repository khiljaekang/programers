def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

#################################################################################################

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
##################################################################################################    

name = ['a', 'b']
value = [1, 2] 
for n, v in zip(name, value):  #파이썬에서 zip()은 내장함수로 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환을 해주는 역할을 한다.  


    print(n, v)


# collections.Counter 


import collections

lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']

print(collections.Counter(lst))  #Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})


##collections.Counter()는  요소의 갯수가 많은 것 부터 출력해준다.

print(collections.Counter({'가': 3, '나': 2, '다': 4}))  # Counter({'다': 4, '가': 3, '나': 2})

## collections.Counter 예제 (3)
## '값=개수' 입력값으로 함

c = collections.Counter(a=2, b=3, c=2)
print(collections.Counter(c))  #Counter({'b': 3, 'c': 2, 'a': 2})
print(sorted(c.elements()))    #['a', 'a', 'b', 'b', 'b', 'c', 'c']



dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

##################################################################################################
a = {1: 'a'}
a[2] = 'b'
print(a)  # {1: 'a', 2: 'b'}

###################################################################################################

grade = {'pey': 10, 'julliet': 99}

print(grade['pey'])#10

print(grade['julliet'])#99

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
# print(a.keys()) #dict_keys(['name', 'phone', 'birth'])


for k in a.keys():     
    print(k)                #name, phone, birth
    


