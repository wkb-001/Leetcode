# -*- coding : utf-8 -*-
# @Time      : 2021/8/2714:33
# @Author    : wkb
class Find_max_numbers():
    def solution(self,n,k):
        max_1 = max(n)
        l = []
        if k==len(n):
            return n
        else:
            for i in range(0,len(n)):
                if n[i] == max_1:
                    for j in range(i,i+k,k):
                         l.append(n[j:j+k])
            return max(l)
n1 = Find_max_numbers()
print(n1.solution('12397687910369765436814',4))
