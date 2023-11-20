import time

#two same arrays beacuse quick sort and insertion sort are inplace algorithms
A = [4, 7, 3, 8, 1, 9, 12, 32, 16]
B = [4, 7, 3, 8, 1, 9, 12, 32, 16]

#function returning pivotes index
def partition(A, p, r):
    pivot = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1

def quick_sort(A, p, r):
    if p <= r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

#quick_sort(A, 0, 8)
#Q = partition(A, 0, 8)
#print(A)

#print(Q)

def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j>= 0 and key<A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

#insersion_sort(A)
#print(A)

def improved_sort(A,p,r,k):
    if p<r:
        q = partition(A,p,r)
        if r-p > k and q-p-2>k:
            improved_sort(A,p,q-1,k)
            improved_sort(A,q+1,r,k)
        else:
            insertion_sort(A)


for k in range(1,len(A)):

    s_time = time.perf_counter()
    quick_sort(A,0,8)
    e_time = time.perf_counter()
    elaps_time = e_time - s_time

    is_time = time.perf_counter()
    improved_sort(B,0,8,k)
    ie_time = time.perf_counter()
    ielaps_time = ie_time - is_time

    if ielaps_time < elaps_time:
        print(k)

