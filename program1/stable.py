import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    mw_dict = dict()
    for line in open_file:
        a = line.rstrip().split(';')
        mw_dict[a[0]] = [None,[i for i in a[1:]]]
#     print(mw_dict)
    return  mw_dict


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    return ''.join([f"  {i} -> {d[i]}"+'\n' for i in sorted(d,key=key,reverse=reverse)] )


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
#     a = order.index(p1)
#     b = order.index(p2)
    return p1 if order.index(p1) < order.index(p2) else p2


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(i,men[i][0]) for i in men}


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men_copy = {i:j for i,j in men.items()}
    unmatched = {i for i in men.keys()}
    if trace:
        print("\nWomen Preferences (unchanging) \n", dict_as_str(read_match_preferences(women), None, False))
    while bool(unmatched):
        if trace:
            print("Men Preferences (changing) \n", dict_as_str(read_match_preferences(men_copy), None, False))
            print("unmatched men = ", unmatched)
        this_man = unmatched.pop()
        this_man_pref = men_copy[this_man][1].pop(0)
        if women[this_man_pref][0] == None:
            women[this_man_pref][0] = this_man
            men_copy[this_man][0] = this_man_pref
        else: # if the woman does have a match, now check to see if the match is top pref
            if women[this_man_pref][1].index(women[this_man_pref][0]) > women[this_man_pref][1].index(this_man) :
                # before .index : the womans list of pref
                # after  .index: trying to find current mans index and compare to her match
                # if the index of this_man is lower (she likes him more) then do some ops
                unmatched.add(women[this_man_pref][0])
                women[this_man_pref][0] = this_man
            else: # meaning she prefers her current match more than this new man
                unmatched.add(this_man)
                
    return {(j[0],i) for i,j in women.items() }
  


  
    
if __name__ == '__main__':
    pref_m = goody.safe_open('Pick the file name containing the preferences for men: ', 'r', 'Could not find that file')
    pref_w = goody.safe_open('Pick the file name containing the preferences for women: ', 'r', 'Could not find that file')
    a = read_match_preferences(pref_m)
    b = read_match_preferences(pref_w)
    print()
    print("Men Preferences")
    print(dict_as_str(a, None, False))
    print()
    print("Women Preferences")
    print(dict_as_str(b, None, False))
    trace = prompt.for_bool("Produce Trace of Algorithm[True]: ",default=True)
    print(make_match(a, b, trace))
    
    
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
