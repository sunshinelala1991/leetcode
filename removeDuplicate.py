# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode

        """



        if head is None or head.next is None:
            return head

        smallhead=ListNode(0)
        largehead=ListNode(0)

        small=smallhead
        large=largehead

        anode=head

        print anode.val

        if anode.val<x:
            small.next=anode
            small=small.next
        else:
            large.next=anode
            large=large.next

        while anode.next is not None:
            anode=anode.next
            print anode.val
            if anode.val<x:
                small.next=anode
                small=small.next
            else:
                large.next=anode
                large=large.next

        print 'done'
        large.next=None
        small.next=largehead.next
        print 'done'
        return smallhead.next


if __name__=="__main__":
    listNode1=ListNode(2)
    listNode2=ListNode(1)
    listNode1.next=listNode2
    s=Solution()
    listNode= s.partition(listNode1,2)
    print listNode.val
    print listNode.next.val
    print listNode.next.next








