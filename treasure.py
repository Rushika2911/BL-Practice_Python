def binary_search(treasure_ids, target_id):
    
    low = 0
    high = len(treasure_ids) - 1
    
    while low<high:
        mid=(low+high)//2
        if treasure_ids[mid]==target_id:
            return mid
        elif treasure_ids[mid]>target_id:
            high=mid-1
        else:
            low=mid+1
    return -1
