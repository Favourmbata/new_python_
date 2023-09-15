def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def three_way_Partition(A):
    start = mid = 0
    pivot = 1
    end = len(A) - 1

    while mid <= end:
        if A[mid]< pivot:
            swap(A,start,mid)
            start = start +1
            mid = mid +1
        elif A[mid] > pivot:
            swap(A,mid,end)
            end = end - 1
        else:
            mid = mid+1

if __name__ == '__main__':
    A = [0,1,2,2,1,0,0,2,0,1,1,0]
    three_way_Partition(A)
    print(A)