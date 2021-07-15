
def pair_sum(arr, k):

    if len(arr) < 2:
        return "Too small array"

    seen = set()
    output = set()

    for num in arr:
        d = k - num
        if d not in seen:
            seen.add(num)
        else:
            output.add((num,d))

    return output

a = [1,3,2,2]
print(pair_sum(a, 4))

