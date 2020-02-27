def search(li, num):
    start, end = 0, len(li)-1
    while start <= end:
        mid = (start+end)//2
        if li[mid] > num:
            end = mid-1
        elif li[mid] < num:
            start = mid+1
        else:
            return True
    return False
