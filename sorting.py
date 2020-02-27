def sort_list(li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li
    
    
def sort_list(li):
    for i in range(len(li)):
        swaps = 0
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                swaps += 1
                li[i], li[j] = li[j], li[i]
        if swaps == 0:
            break
    return li
