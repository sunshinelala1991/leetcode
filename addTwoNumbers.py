class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ll1=0
        list1=[]
        node1=l1
        while node1 is not None:
            list1.append(node1.val)
            ll1+=1
            node1=node1.next

        ll2=0
        node2=l2
        list2=[]
        while node2 is not None:
            list2.append(node2.val)
            ll2+=1
            node2=node2.next



        if ll1>ll2:
            dif=ll1-ll2

            result=list1[:dif]
            for x,y in zip(list1[dif:],list2):
                result.append(x+y)

        else:
            dif=ll2-ll1

            result=list2[:dif]
            for x,y in zip(list1,list2[dif:]):
                result.append(x+y)

        nresult=[]

        for x in result:
            nresult.append(ListNode(x))

        for y in range(len(nresult)-1):
            nresult[y].next=nresult[y+1]

        return nresult[0]








