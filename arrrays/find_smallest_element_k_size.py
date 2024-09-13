import heapq

A = [2, 43, 5, 15]
n = len(A)
k = 2
A.sort()
print(A[k - 1])


# usinfg recursion
def smalest(k, A):
    A.sort()
    return A[k - 1]


def ksmallest(K, A):
    max_heap = []
    for num in A:
        heapq.heappush(max_heap, -num)
    print(max_heap)
    # If the size of the max heap exceeds K, remove the largest element
    if len(max_heap) > K:
        heapq.heappop(max_heap)
    print(max_heap)
    # Return the Kth smallest element (top of the max heap, negated)
    return -max_heap[0]


print("smallest", smalest(k, A))
print("Smalleast using heap elemt", ksmallest(k, A))

# using heap
def kth_smallest_sliding_window(arr, k):
    # We use a max-heap to track the k smallest elements.
    # Python has a min-heap by default, so we push negative values to simulate a max-heap.
    max_heap = []

    # Traverse the array and add elements to the heap
    for num in arr:
        # Push the negative of the current number to simulate a max-heap
        heapq.heappush(max_heap, -num)

        # If the heap exceeds size k, pop the largest element (which is the smallest in negative)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # The root of the max-heap (smallest element in negative) will be the k-th smallest
    return -max_heap[0]


# Example usage:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"The {k}th smallest element is {kth_smallest_sliding_window(arr, k)}")