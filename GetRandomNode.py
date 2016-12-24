# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.listLen=1

        self.head=head

        node=head
        while node.next is not None:
            node=node.next
            self.listLen+=1






    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """

        position=randint(1,self.listLen)

        if position==1:
            return self.head

        i=1

        node=self.head
        while node.next is not None:
            node=node.next

            i+=1
            if i==position:
                return node.val


for i in range(2,5):
    print randint(1,2)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()