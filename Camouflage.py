import collections

def solution(clothes):
    answer = 1
    kind = []
    
    for a, b in clothes:
        kind.append(b)
        
    kind = collections.Counter(kind)
    
    for i in kind.values():
    	answer *= (i + 1)
    
    return answer - 1


from collections import Counter
def solution(clothes):
    counter_each_category = Counter([cat for _, cat in clothes])
    all_possible = 1
    
    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)

    return all_possible - 1