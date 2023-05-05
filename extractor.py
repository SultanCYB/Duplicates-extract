def d_extract(to_extract: "list or tuple"):
    ''' For extracting all instances of the duplicated element'''
    
    done = dict()
    for i in to_extract:
        done[i] = done.get(i, 0) + 1
    
    return [ value for value, count in done.items() if count > 1 ]
