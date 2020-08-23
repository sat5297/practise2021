ar = {0:0, 1:1}

def hashi(num):

    if num in ar:
        return ar[num]
    ar[num]=max(num, (hashi(num//2)+hashi(num//3)+hashi(num//4)))

    return ar[num]

while True:
    try:
        n = int(input())
        print(hashi(n))
    except:
        break
       
      
link :: https://www.hackerearth.com/practice/algorithms/dynamic-programming/state-space-reduction/practice-problems/algorithm/bytelandian-gold-coins/description/
