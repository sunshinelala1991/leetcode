# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        anode=head

        if anode is None:
            return head

        i=1

        fl=[]
        rl=[]
        el=[]


        if m==1:
            rl=[head]
        elif m>1:
            fl=[head]

        while anode.next is not None:
            anode=anode.next
            i+=1
            if i<m:
                fl.append(anode)
            elif i>=m and i<=n:
                rl=[anode]+rl
            elif i>n:
                el.append(anode)

        for i in range(len(rl)-1):
            rl[i].next=rl[i+1]
        if len(el)!=0:
            rl[-1].next=el[0]
        else:
            rl[-1].next=None

        if len(fl)!=0:
            fl[-1].next=rl[0]
            return fl[0]
        else:
            return rl[0]



