import Queue

def maximumSubsequenceSum(lst):


    thisSum=0
    maxSum=0

    for i in lst:
        thisSum+=i

        if thisSum>maxSum:
            maxSum=thisSum
        elif thisSum<0:
            thisSum=0

    return maxSum


class TreeNode:
    def __init__(self, left,right,val):
        self.left=left
        self.right=right
        self.val=val

def BFS(root):
    if root==None:
        return
    lst=[root]

    while lst:
        newLst=[]
        for node in lst:
            if node.left is not None:
                newLst.append(node.left)
                print node.left.val
            if node.right is not None:
                newLst.append(node.right)
                print node.right.val
        lst=newLst

def BFS(root):
    if root==None:
        return

    que=Queue()

    que.put(root)

    while not que.empty():
        node=que.get()
        print node.val
        if node.left!=None:
            que.put(node.left)
        if node.right!=None:
            que.put(node.right)

'''
delete the node with value=nodeVal
root is the root of the tree
'''
def deleteBinarySearchTreeNode(root, nodeVal):

    if root==None:
        return
    if root.val<nodeVal:
        deleteBinarySearchTreeNode(root.right,nodeVal)
    elif root.val>nodeVal:
        deleteBinarySearchTreeNode(root.left,nodeVal)
    elif root.left!=None and root.right!=None:
        root.val=findBSTMin()
        deleteBinarySearchTreeNode(root.right,root.val)
    elif root.left!=None:
        root=root.left
    else:
        root=root.right



def findBSTMin(node):
    while node.left!=None:
        node=node.left

    return node.val


def percolateUp(newVal,heap):

    location=len(heap)

    heap.append(0)

    while location/2>0 and heap[location/2]>newVal:

        heap[location]=heap[location/2]
        location=location/2


    heap[location]= newVal

def deleteMin(heap):
    hole=1

    replaceVal=heap[-1]

    while hole*2<=len(heap)-1:
        if hole*2==len(heap)-1:
            heap[hole]=heap[hole*2]
            hole=hole*2
        else:
            if heap[hole*2]<heap[hole*2+1]:
                heap[hole]=heap[hole*2]
                hole*=2
            else:
                heap[hole]=heap[hole*2+1]
                hole=hole*2+1
    heap[hole]=replaceVal
    heap.pop()



def selectionSort(lst):

    for i in range(1, len(lst)):

        tmp=lst[i]
        j=i-1
        while tmp<lst[j] and j>=0:
            lst[j+1]=lst[j]
            j-=1

        lst[j+1]=tmp


        print lst


def shellSort(lst):
    gap=len(lst)/2
    while gap>0:

        for i in range(2*gap-1,len(lst),gap):
            tmp=lst[i]
            j=i-gap
            while tmp<lst[j] and j>=0:
                lst[j+gap]=lst[j]
                j=j-gap
            lst[j+gap]=tmp
        gap/=2






def heapSort(a):

    for i in range(len(a)/2-1, -1, -1):
        perculateDown(a, i,len(a)-1 )


    for i in range(len(a)-1,0,-1):
        print a, a[0],a[i]
        tmp=a[0]
        a[0]=a[i]
        a[i]=tmp
        perculateDown(a, 0, i-1)



def leftChild(i):
    return 2*i+1



def perculateDown(lst,i,n):

    tmp=lst[i]
    while leftChild(i)<=n:

        if leftChild(i)+1<=n and lst[leftChild(i)+1]>lst[leftChild(i)]:
            newChild=leftChild(i)+1
        else:
            newChild=leftChild(i)


        if lst[newChild]>tmp:
            lst[i]=lst[newChild]
            i=newChild
        else:
            break



    lst[i]=tmp


def mergeSort(lst):
    mergeSortHelper(lst, 0, len(lst)-1)

def mergeSortHelper(lst, left, right):
    if right>left:
        center=(left+right)/2
        mergeSortHelper(lst, left, center)
        mergeSortHelper(lst, center+1, right)
        merge(lst,left,center+1, right)


def merge(lst, left, right, rightEnd):

    newLst=[]
    p1=left
    p2=right
    while p1<=right-1 and p2<=rightEnd:
        if lst[p1]<lst[p2]:
            newLst.append(lst[p1])
            p1+=1
        else:
            newLst.append(lst[p2])
            p2+=1
    if p1>right-1:
        newLst+=lst[p2:rightEnd+1]
    else:
        newLst+=lst[p1:right]

    i=left
    for x in newLst:
        lst[i]=x
        i+=1


def quicksort(lst):
    smaller=[]
    same=[]
    larger=[]

    if len(lst)>1:
        pivot=lst[0]
        same.append(pivot)
        for x in lst[1:]:
            if x<pivot:
                smaller.append(x)
            elif x>pivot:
                larger.append(x)
            else:
                same.append(x)
        quicksort(smaller)
        quicksort(larger)

        i=0
        for x in smaller:
            lst[i]=x
            i+=1
        for x in same:
            lst[i]=x
            i+=1
        for x in larger:
            lst[i]=x
            i+=1



def quickSelect(lst,k):
    quickSelectHelper(lst,0,len(lst)-1, k )
    print lst[k-1]
    print sorted(lst)[k-1]



def quickSelectHelper(lst, left, right,k):
    if right-left<=1:
        if(lst[right]<lst[left]):
            swap(lst, right, left)

    else:
        pivot=median(lst, left, right)
        i=left
        j=right-1

        while True:
            i+=1
            while lst[i]<pivot:
                i+=1
            j-=1
            while lst[j]>pivot:
                j-=1
            if i<j:
                swap(lst, i, j)
            else:
                break

        swap(lst, i, right-1)

        if k<i+1:
            quickSelectHelper(lst, left, i-1,k )
        elif k>i+1:
            quickSelectHelper(lst, i+1,right, k)




def median(lst,left, right ):
    center=(left+right)/2
    if lst[left]>lst[center]:
        swap(lst, left,center)
    if lst[left]>lst[right]:
        swap(lst, left, right)
    if lst[center]>lst[right]:
        swap(lst, center, right)

    swap(lst, center, right-1)
    return lst[right-1]


def swap(a, i, j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp



#lst=[39,7,21,4,2,5,7,1,9,3,0]
lst=[1,2,3,37,2,15,27,38]

for x in range(1, len(lst)+1):
    quickSelect(lst,x)














