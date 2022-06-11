def quick_sort(L) -> list:
    A, B = [], []
    if len(L) > 1:
        for x in L[1:]:
            if x <= L[0]:
                A.append(x)
            else:
                B.append(x)

        return quick_sort(A) + [L[0]] + quick_sort(B)
    else:
        return L

print(quick_sort([3,7,9,34,12,8]))

