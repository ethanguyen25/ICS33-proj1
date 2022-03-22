import goody
from collections import defaultdict


def read_ndfa(file : open) -> {str:{str:{str}}}:
#    dict1, dict2, sett = {}, {}, set()
#    for line in file:
#        ss = line.rstrip("\n").split(";")
#        print("SS", ss)
#        if len(ss) == 1:
#            dict1[ss] = {}
#        else:
#            for x in range(1,len(ss) + 1,2):
#                value = ss[x+1]
#                dict2[ss[x]] = sett.add(value)
#                dict1[ss[0]] = dict2

    dic = {}
    for line in file:
        a = line.rstrip().split(';')
        dic2 = defaultdict(set)
        start = a.pop(0)
        while len(a)>=2:
            dic2[a.pop(0)].add(a.pop(0))
        dic[start] = dict(dic2)
    return dic
               
               
   


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    pass
#     print(ndfa)
#     s = "  "
#     lis = []
#     for k, v in ndfa.items():
#         for values in v.values():
#             lis.append(values)
#             s += k + " transitions: " + str(list(v) + [values]) + "\n  "
# #     print("S",s )
#     return s
   

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:

    """
    {'end': {}, 'start': {'1': {'start'}, '0': {'start', 'near'}}, 'near': {'1': {'end'}}}
    
    ['start', ('1', {'start'}), ('0', {'start', 'near'}), ('1', {'end', 'start'}), ('1', {'start'}), 
        ('0', {'start', 'near'}), ('1', {'end', 'start'})]
    """
#      
#     lis = [state]
#     sett = set()
#     s = {state}
#     print(s)
#     for x in inputs:
#         starting = [z for z in s]
#         for y in starting: 
#             if y in ndfa:
#                 if x in ndfa[y]:
#                     s = s.union(ndfa[y][x])
#         lis.append((x,s))
     
    lis = [state]
    sett = set()
    s = {state}
    copy = s.copy()
    s = set()
    for x in inputs:
        starting = [z for z in copy]
        for y in starting: 
            if y in ndfa:
                if x in ndfa[y]:
                    s = s.union(ndfa[y][x])
                    copy = s.copy()
        lis.append((x,s))
        if s == set():
            break
        s = set()
    return lis
                    


def interpret(result : [None]) -> str:
    s = f"Start state = {result[0]}" + "\n"
    result.pop(0)
    for x in result:
        s += f"  Input = {x[0]}; new possible states = {sorted(x[1])}" + "\n"
    s += f"Stop state(s) = {sorted(x[1])}" + "\n"
    return s





if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
