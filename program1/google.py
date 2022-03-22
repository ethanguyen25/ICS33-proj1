import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    return {(fq[:x]) for x in range(1,len(fq) + 1)}


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    count = 0
    keys = {(new_query[:x]) for x in range(1,len(new_query) + 1)}
    maxi = max(keys, key = len)
    for x in keys:
        if x not in prefix:
            prefix[x] = {maxi}
        else:
            prefix[x].add(maxi)
    
    for y in prefix:
        if y == maxi:
            count += 1
    
    query[maxi] += count
    
    return 
    


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    lis = []
    q,p = defaultdict(int), defaultdict(set)
    for line in open_file:
        l = line.rstrip("\n").split(" ")
        lis.append(tuple(l))
    sett = set(lis)
    for x in lis:
        
        string = list(filter(lambda string: string == x, lis))
        q[x] = len(string)
        
        ap = sorted(list(all_prefixes(x)))
        for y in ap:
            z = ap.index(y)
            while z < len(ap):
                p[y].add(ap[z])
                z += 1
    copy = p.copy()
    to_delete = set()
    for k,v in copy.items():
        for values in v:
            if values not in sett:
                to_delete.add(values)
    for delete in to_delete:
        for k,v in copy.items():
            if delete not in sett:
                p[k].discard(delete)
    return (p,q)
    

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return "".join(f"  {k} -> {d[k]}" + "\n" for k in sorted(d, key = key, reverse = reverse))

def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    if a_prefix not in prefix:
        return []
    return [(que) for que in sorted(prefix[a_prefix],key=lambda x:(-query[x],x))[:n] if a_prefix in prefix ]
    



# Script

if __name__ == '__main__':
    # Write script here 
    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
