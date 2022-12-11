def solution(A, K, L):
    if K+L > len(A):
        return -1
    sum = []
    count = 0
    sum[0] = A[0]
    for i in A:
        sum[count] = sum[count-1] + i
        count += 1

    max = -1
    x = 0
    y = 0
    count_P = 0
    while count_P + K - 1 < len(A):
        if count_P > 0:
            x = sum[count_P + K - 1] - sum[count_P - 1]
        else:
            x = sum[count_P + K - 1]
        count_Q = count_P + K
        while count_Q + L - 1 < len(A):
            if count_Q > 0:
                y = sum[count_Q + L - 1] - sum[count_Q - 1]
            else:
                y = sum[count_Q + L - 1]

            if x + y > max:
                max = x + y
    return max