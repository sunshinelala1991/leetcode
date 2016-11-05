# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head ==None:
            return head

        anode=head

        reList=[head]

        while anode.next !=None:
            anode=anode.next
            reList=[anode]+reList

        for i in range(len(reList)-1):
            reList[i].next=reList[i+1]

        reList[-1].next=None

        return reList[0]

