
def merge(A, B) -> list:
    C = []
    while A and B:
        if A[0] < B[0]:
            C.append(A[0])
            A = A[1:]
        else:
            C.append(B[0])
            B = B[1:]
    C += A + B
    return C


print(merge([0,2,4,6,8],[1,3,5]))


def merge_sort(L) -> list:
    if len(L) > 1:
        return merge(merge_sort(L[:len(L)//2]), merge_sort(L[len(L)//2:]))
    else:
        return L

print(merge_sort([3,7,9,34,12,8]))

# złożoność czasowa O(n log n) n - szer tabl., log n - wysokość tabeli
