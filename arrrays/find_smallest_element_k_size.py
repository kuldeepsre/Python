
 A = [2, 43, 5, 15]
n=len(A)
k=2
A.sort()
print(A[k-1])
# usinfg recursion
def smalest(k,A):
    A.sort()
    return A[k-1]

print("Smalleast elemt", smalest(k,A))

# using heap

