import heapq
from random import randint

#class for different types of sorts
class Sort:

    def isSorted(A,p,q):
        for i in range(p,q - 1):
            if A[i+1] < A[i]:
                return False
        return True

    def HeapTest(A, i):
        if i > (len(A) - 3) // 2:
            return True

        if(A[i] >= A[2 * i + 1] and A[i] >= A[2 * i + 2] and Sort.HeapTest(A, 2*i+1) and Sort.HeapTest(A, 2 * i + 2)):
            return True
        return False

    def eleCheck(A):
        for i in A:
            if not isinstance(i, type(A[0])):
                return False
        return True
            

    #pre condition: An Array of integers with length >= 2
    #post condition: A sorted Array of integers from least to greatest
    #invariant a[j] >= a[j - 1]
    def InsertionSort(A):
        #precondition
        #assert(len(A) >= 2)
        for j in range(1,len(A)):
            #precondition
            assert(isinstance(A[j-1], int))
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
            #loop invariant plus post condition
            assert(A[j] >= A[j - 1])
        return A

    #pre condition: A is a nonempty array of similar elements and p, q, and r are indices into the array where p <= q and p < r.
    #the subarrays A[p...q] and A[q + 1..r] are sorted
    #post condition: The subarray A[p...r-1] is sorted
    def Merge(A,p,q,r):
        assert(p <= q and p < r and Sort.isSorted(A,p,q) and Sort.isSorted(A,q+1,r) and Sort.eleCheck(A)) #precondition
        n1 = q - p + 1 #length of left array
        n2 = r - q  #length of right array
        L = [0] * (n1) #left array
        R = [0] * (n2) #right array
        
        #copies data to L
        for i in range(0, n1):
            L[i] = A[p + i]
        #copies the data to R
        for j in range(0, n2):
            R[j] = A[q + j + 1]

        i = 0 #left index
        j = 0 #right index
        k = p #sorted index

        #Invariant: A[p...k] is sorted
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            assert(Sort.isSorted(A, p, k)) #invariant
            k += 1
        #gets the remaining elements of L
        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1

        #gets the remaning elements of R
        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1
        assert(Sort.isSorted(A, p, r)) # postcondition

    #pre-condition: A is a non-empty array of similar elements where p <= r
    #post-condition: A[p...r] is sorted
    def MergeSort(A, p, r):
        assert(len(A) > 0 and p <= r and Sort.eleCheck(A)) #pre condition
        if p < r:
            q = (p + r) // 2
            Sort.MergeSort(A, p, q)
            Sort.MergeSort(A, q + 1, r)
            Sort.Merge(A, p, q, r)
        assert(Sort.isSorted(A,p,r)) #post condition
        return A


    #Pre-condition: A is a nonempty array of similar elements and there is at least one element in between A[p] and A[r] and p < r
    #Post-COndition: All elements in A[p...i] <= A[r] and A[r...len(A)-1] >= A[r]
    def Partition(A, p, r):
        assert(len(A) > 0 and p < r and Sort.eleCheck(A)) #precondition
        x = A[r] #pivot position
        i = p - 1 #index of the snaller element

        #Loop Invariant: A[p...i] <= A[r] and A[i + 1...j - 1] >= A[r]
        for j in range(p, r):
            #moves i by one, swaps A[i] and A[j] so that every value to left of pivot is smaller
            #thus meaning every value to right of pivot will end up being larger
            if A[j] < x:
                i = i + 1
                A[i], A[j] = A[j], A[i]
            for k in range(p,i):
                assert(A[k] <= A[r]) #invariant
            for m in range(i + 1, j):
                assert(A[m] >= A[r]) #invariant
        A[i + 1], A[r] = A[r], A[i + 1]

        for y in range(p,i):
            assert(A[y] <= A[r]) #post condition
        for z in range(r, len(A)):
            assert(A[z] >= A[r]) #postcondition
        return i + 1

    #Pre-condition: A is a non empty array of similar elements
    #Post Condition: A[p...r] is sorted
    def QuickSort(A, p, r):
        assert(len(A) > 0 and Sort.eleCheck(A)) #pre condition
        if p < r:
            q = Sort.Partition(A, p, r)
            Sort.QuickSort(A,p,q-1)
            Sort.QuickSort(A, q + 1, r)
        assert(Sort.isSorted(A,p,r)) #post condition
        return A

    #Pre-Condition: A is a non empty array of similar elements where n >= 0 and i >= 0 and i <= n
    #Post condition: The tree at root A[i] is a heap
    def MaxHeapify(A, i, n):
        assert(i >= 0 and i <= n and n >= 0 and Sort.eleCheck(A))
        l = 2 * i #left node
        r = 2 * i + 1 #right node
        #if statements to get largest node in A
        if(l <= n and A[l] > A[i]):
            largest = l
        else:
            largest = i
        if(r <= n and A[r] > A[largest]):
            largest = r
        #repeats until largest node is found
        if(largest != i):
            A[i], A[largest] = A[largest], A[i]
            Sort.MaxHeapify(A, largest, n)
            

    #Pre-condition: A is a non-empty array of similar elements
    #Post-condition: A[0] is the root of the tree and it is a heap
    def BuildMaxHeap(A, n):
        assert(len(A) > 0 and Sort.eleCheck(A) and n >= 0) #precondition
        #Loop invariant: The tree at root A[i] is a heap
        for i in range(n//2, -1, -1):
            Sort.MaxHeapify(A,i,n)

    #pre-condition: A is a non-empty array of similar elements where n > 0
    #post-condition: A[0...n] is sorted
    def HeapSort(A, n):
        assert(len(A) > 0 and n > 0 and Sort.eleCheck(A)) #precondition
        Sort.BuildMaxHeap(A,n)
        for i in range(n,0, -1):
            A[0], A[i] = A[i], A[0]
            Sort.MaxHeapify(A,0,i-1)
        assert(Sort.isSorted(A,0,n))  #post condition
        return A

    #pre condition: A is a non-empty array of similar elements
    #post-Condition: A[0...len(A)] is sorted
    def SelectionSort(A):
        assert(len(A) > 0 and Sort.eleCheck(A)) #pre-condition
        #loop invaariant: A[0...i] is sorted
        for i in range(len(A)):
            minIndex = i
            #Loop Invariant: A[minIndex] is the min value in A[i..j]
            for j in range(i + 1, len(A)):
                if(A[minIndex] > A[j]):
                    minIndex = j
                #for x in range(i,j + 1):
                    #assert(A[x] >= A[minIndex]) #inner loop invariant
            A[i], A[minIndex] = A[minIndex], A[i] 
            assert(Sort.isSorted(A, 0, i)) #outer loop invariant
        assert(Sort.isSorted(A, 0, len(A))) #postcondition
        return A
#b = [9, 5, 5, 7, 4, 9]
#b = ['a', 'c', 'b', 'e']
#b = []
#for i in range(0, 100):
    #b.append(randint(0,10))
#print(min(b))
#b = [3, 2, 5,4,8,7,2,2,3,4,1,3]
#for i in b:
    #print(b)
#print(Sort.HeapSort(b,len(b) - 1))
#Sort.MaxHeapify(b, 0, len(b) -1)
#heapq.heapify(b)
#for i in b:
    #print(i)
#print(Sort.HeapTest(b,0))
#print(Sort.eleCheck(b))
#print(Sort.SelectionSort(b))
#print(Sort.MergeSort(b,0,len(b)-1))
#print(Sort.QuickSort(b,0,len(b)-1))
#print(Sort.Partition(b, 0, len(b) - 1))
