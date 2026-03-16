import random
from collections import defaultdict
class MarkovChain:
    def __init__(self,order=1):
        self.order=order; self.transitions=defaultdict(lambda:defaultdict(int))
    def train(self,data):
        for i in range(len(data)-self.order):
            state=tuple(data[i:i+self.order]); next_val=data[i+self.order]
            self.transitions[state][next_val]+=1
    def generate(self,length,start=None):
        if start is None: start=random.choice(list(self.transitions.keys()))
        state=start; result=list(state)
        for _ in range(length):
            if state not in self.transitions: break
            nexts=self.transitions[state]
            total=sum(nexts.values())
            r=random.randint(1,total); cum=0
            for val,count in nexts.items():
                cum+=count
                if cum>=r: result.append(val); state=tuple(result[-self.order:]); break
        return result
if __name__=="__main__":
    random.seed(42)
    mc=MarkovChain(order=2)
    text="the cat sat on the mat the cat ate the rat"
    words=text.split()
    mc.train(words)
    generated=mc.generate(10)
    assert len(generated)>=3
    assert all(isinstance(w,str) for w in generated)
    # Character-level
    mc2=MarkovChain(order=3)
    mc2.train(list("abracadabra"*10))
    chars=mc2.generate(20)
    print(f"Word chain: {' '.join(generated[:8])}")
    print(f"Char chain: {''.join(chars[:15])}")
    print("All tests passed!")
