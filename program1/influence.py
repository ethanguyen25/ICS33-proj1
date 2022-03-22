import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    dict = defaultdict(set)
    for line in open_file:  #open the file 
        ss = line.rstrip("\n").split(";")  #strip the file
        if len(ss) == 2:  #if the list is greater than 1 meaning it has a friend
            dict[ss[0]].add(ss[1])  #add that friend to its value in the dict and vice versa
            dict[ss[1]].add(ss[0])
        if len(ss) == 1:  #if there is no friend, then the value is empty set
            dict[ss[0]]
    return dict


def graph_as_str(graph : {str:{str}}) -> str:
    s = "  "  #result is a multi-line string
    lis = []
    for k, v in sorted(graph.items()):  #loop through dict to grab keys and values
        for values in v:  #loop through values because it is a set
            lis.append(values)  #add values to a list
        s += (str(k) + " -> " + str(sorted(lis)) + "\n" + "  ")
        lis.clear()  #clear list so that it doesn't hold values
    return s.rstrip("  ")


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    inflDict = {}  #Influencer Dictionary
    removalCand = []  #Removal Candidates
    checker = []  #list of friends used to check 
    sett = set()  #what were supposed to return 
    for k, v in sorted(graph.items()):  #loops through dict to grab keys and values
        if len(v) >= 1:
            inflDict[k] = [len(v) - ceil(int(len(v))/2), len(v), k]  #creates inflDict w keys that have friends.
            removalCand.append((len(v) - ceil(int(len(v))/2), len(v), k))  #creates the removalCand list which can only contain nodes w friends.
        else:
            inflDict[k] = [-1, len(v), k]  #if node does not have friends then first index is -1

    while removalCand != []:  #condition: while the list still has tuples 
        mini = min(removalCand)  #the minimum valued tuple of the list
        del inflDict[mini[2]]  #delete it from the inflDict
        removalCand.remove(mini)  #remove the mini from the list of candidates
        for x, y in graph.items():  #this loop is to find the friends and add it to the checker list
            for z in y:
                if z == mini[2]:
                    checker.append(x)
        for elements in checker:  #this loop is to check the inflDict and removalCand list for those friends and decrement their first and second indexes by one
            if elements in inflDict:
                zero = int(inflDict[elements][0]) - 1 
                one = int(inflDict[elements][1]) - 1
                inflDict[elements] = [zero, one, elements]  #replaces it with new value
                for things in removalCand:
                    if things[2] == elements:
                            removalCand.remove(things)  #once found, it removes it
                removalCand.append((zero, one, elements))  #then you add the tuple with updated values
                removalCand = sorted(removalCand, key = lambda x: x[2])  #sort the removalCand list
            for stuff in removalCand:  #checks if the first index of any tuple is less than 0, then removes it
                if stuff[0] < 0:
                    removalCand.remove(stuff)
        checker.clear()  #clears checker so that the list of friends is unique
    
    for last in inflDict.keys():  #adds what's left of the inflDict to a set
        sett.add(last)
    
    return sett


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    dict1, dict2 = {}, {}
    sett = set()
    count = 0
    for nodes in graph.keys():
        if nodes in influencers:  #for all the nodes in influencers, it will have a value of True. 
            dict1[nodes] = True
        else:
            dict1[nodes] = False  #Else every other node will have a value of False.
    while True:
        dict2 = {i:j for i,j in dict1.items()}  #making an identical dictionary to later check if it is the same. 
        for k,v in dict1.items():  #loops through the dict1 and checks for values that equal False. 
            count = 0  #resets count to zero. 
            if v == False:  #if it is False, then find the number of friends needed to influence that node.
                num = ceil(int(len(graph[k]))/2)
                for i in graph[k]:  #looping through the set of values
                    if i in dict1:  #checking if the value is in our dict1
                        if dict1[i] == True:  #if the value is True then add to the count
                            count += 1
                            if count >= num:  #once/if the count is greater or equal to the num, then the value becomes True.  Then you start checking the next key.
                                dict1[k] = True
                                break
        if dict1 == dict2:  #if the dictionaries are equal that means there are no more changes.
             break
                
    for x in dict1:  #add the keys that are left, to a set and return the set. 
        if dict1[x] == True:
            sett.add(x)
    
    return sett                         
                                

    
    
    
            
    
if __name__ == '__main__':
#     
#     friend_file = safe_open('Enter file name containing the friendship graph', 'r', 'Could not find that file')
#     graph = read_graph(friend_file)
#     print('Graph: person -> [friends] \n' + graph_as_str(graph),end='')
#     trace = prompt.for_bool('Do you want to trace the Algorithm',default=True)
#     print('The influencers are  ',find_influencers(graph,trace))
#     
#     while True:
#         print(graph.values())
# # #         nodes = prompt.for_string("Pick any subset or enter 'done' ", default=None, is_legal=lambda x:(any(x in k for k in graph.values()) or x=='done' ), error_message='Node does not exist')
#         is_legal = (lambda x: x in graph or any(x in k for k in graph[x]))
#         nodes = input("Pick any subset or enter 'done': " )
#         if nodes == 'done':
#             break
#         elif is_legal(nodes):
#             print(f"friends influenced by subset ({(len(nodes)/len(graph))*100} of graph)",all_influenced(graph,nodes) + "\n")
#     #         elif is_legal(nodes) == False:
#         else:
#             print('Please enter a legal string\n')
# #     while True:
# #         print(graph.values())
# #         nodes = prompt.for_string("Pick any subset or enter 'done' ", default=None, is_legal=lambda x:x in graph or (any(x in k for k in graph.values()) or x=='done' ), error_message='Node Doesnt exist')
# #         if nodes == 'done':
# #             break
# #         print(f"friends influenced by subset ({(len(nodes)/len(graph))*100} of graph)",all_influenced(graph,nodes))
#                               
    
    
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

