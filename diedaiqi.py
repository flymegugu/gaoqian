class myiterator:
    def __init__(self,limit):
        self.limit=limit
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current+=1
            return result
        else:
            raise StopIteration
        
if __name__=='__main__':
    iterator =myiterator(10)
    for item in iterator:
        print(item)