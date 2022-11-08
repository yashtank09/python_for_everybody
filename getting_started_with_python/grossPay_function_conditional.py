def computepay(h, r):
    payout = 0
    if h > 40:
        payout = (40 + (h - 40) * 1.5) * r
    else:
        payout = h * r
    return payout


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(float(hrs), float(rate))
print("Pay", p)
