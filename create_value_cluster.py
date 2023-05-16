
def create_cluster(arr: list, limit: int):
    """Create cluster list of n preceding values and n exceeding values"""
    response = []
    for idx in range(1, len(arr)+1):
        start_idx = idx
        head = arr[start_idx:start_idx+limit]
        if idx == 0:
            tail = [0]*limit
        else:
            tail = arr[:start_idx-1]
        try:
            tail_values = tail.reverse()
            tail_values = tail[:limit]
        except TypeError as e:
            len_tail = len(tail)
            remaining = limit - len_tail
            tail_values = [0]*remaining+tail
        if len(tail_values) < limit:
            len_tail = len(tail)
            remaining = limit - len_tail
            tail_values = [0]*remaining+tail
        if len(head) < limit:
            len_head = len(head)
            remaining = limit - len_head
            head = [0]*remaining+head
        response.append(head+tail_values)
    return response

#create_cluster([1,2,3,4,5,6,7,8,9]*1000, 30)