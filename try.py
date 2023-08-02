items = ['gari', 'Beans', 'rice', 'cocoa', 'zoli']
ORDER = ['asc', 'desc']
# i want to do sorting using max and min

# i want to follow best practices


def sort(_list, reverse=None):
    new_list = []
    if reverse:
        for iteration in _list:
            # get current max
            current_max = max(_list)
            new_list.append(current_max)
            # remove this max from the _list
            _list.remove(current_max)
        return new_list
    else:
        for iteration in _list:
            current_min = min(_list)
            # add min to our new list 
            new_list.append(current_min)
            # remove from the other list 
            _list.remove(current_min)
        return new_list
    

def descending(_list):
    return sort(_list, reverse=True)


def ascending(_list):
    return sort(_list)
    

def do_sort(_list: list=None, order_by=None):
    """
        pythonic way is to have your function do one thing at a time
    """
    if _list is None:
        _list = items
    if (order_by == 'asc'):
        return ascending(_list)
    elif(order_by == 'desc'):
        return descending(_list)
    
desc_items = do_sort(items,ORDER[1])
desc_slice = desc_items[::2]
asc_item = do_sort(desc_items, ORDER[0])
print(asc_item)
asc_item[::2] = desc_slice
print(asc_item)
