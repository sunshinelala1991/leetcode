
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator=iterator

        self.buffer=None



    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.buffer!=None:
            return self.buffer
        else:
            if self.iterator.hasNext():
                x=self.iterator.next()
                self.buffer=x
                return x
            else:
                return None




    def next(self):
        """
        :rtype: int
        """
        if self.buffer!=None:
            x=self.buffer
            self.buffer=None
            return x
        else:
            return self.iterator.next()



    def hasNext(self):
        """
        :rtype: bool
        """
        if self.buffer!=None:
            return True
        else:
            return self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].