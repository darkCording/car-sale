"""
*
*   queue functions
*
"""

class queue:

    def __init__(self, queList):
        self.queList = queList
    # import new element
    def enqueue(self,element):
        self.queList.append(element)

    # remove element under FIFO method
    def dequeue(self):
        if not self.queList:
            deq = "List is empty"
        else:
            deq = self.queList.pop(0)

        return deq
    # delete an element
    def delete(self,key):
        el_del=self.queList.remove(key)

        return el_del
    # show next element
    def displayNext(self, i):
        return self.queList[i]
    # show all elements
    def display(self):
        print(self.queList)
