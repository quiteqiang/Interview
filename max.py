'''
max(iterable, *[, key, default])¶
max(arg1, arg2, *args[, key])
Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, it should be an iterable. The largest 
item in the iterable is returned. If two or more positional arguments are 
provided, the largest of the positional arguments is returned.

There are two optional keyword-only arguments. The key argument specifies a 
one-argument ordering function like that used for list.sort(). The default 
argument specifies an object to return if the provided iterable is empty. 
If the iterable is empty and default is not provided, a ValueError is raised.

If multiple items are maximal, the function returns the first one encountered. 
This is consistent with other sort-stability preserving tools such as 
sorted(iterable, key=keyfunc, reverse=True)[0] and 
heapq.nlargest(1, iterable, key=keyfunc).
'''
'''
1. Return largest item of the interable object   --Done
2. Return largest item of multiple argument      --Done
3. Return default value if argument is empty     --Done 
4. Sepcify the KEY value in comparision          -- 
'''

#Initialization
DEFAULT = 111; 
LIST    = [
  {'nation': 'China', 'history': 2021},
  {'nation': 'England', 'history': 2020},
  {'nation': 'USA', 'history': 2019}
]
KEY     = "KEY"


#Function to get the max item in an list
def get_max(args):
    max_num = None                                                          
    lst = args[0]                                   
    if not isinstance(lst,list):
        return "Error: item is not interable"
    max_num = lst[0]                                                        
    for item in lst:
        if isinstance(item,(float,int)):
            if max_num < item:
                max_num = item
            else:
                max_num = max_num
    return max_num

#Boolean function: check if the argument is given with "KEY"
def key_spcf_com(args):
    for arg in args:
        if arg == "KEY":
            return True
    return False

#Handle the situation: 
#   1. if KEY is given as "string"
#   2. if KEY is given as "integer"
def key_int_str(key_type, args, length):
    arg_list = []
    if key_type == "int":
        for i in range(length - 1):
            arg_list.append(int(args[i]))
        max_num = None
        if not isinstance(arg_list,list):
            return max_num
        max_num = arg_list[0]
        for item in arg_list:
            if isinstance(item,(float,int)):                                    
                if max_num < item:                                              
                    max_num = item                                              
                else:                                                           
                    max_num = max_num
        return str(type(max_num)) + " " + str(max_num) 
    elif key_type == "str":
        for i in range(length - 1):
            arg_list.append(str(args[i]))
        max_num = None
        if not isinstance(arg_list,list):
            return max_num
        max_num = arg_list[0]
        for item in arg_list:
            if isinstance(item,(float,int,str)):                                    
                if max_num < item:                                              
                    max_num = item                                              
                else:                                                           
                    max_num = max_num
        return str(type(max_num)) + " " + max_num


#Implementing MAX funtion here:
def my_max(*args):

#Only one argument
    if len(args) == 1:
        if args[0] == "DEFAULT":
            u_input = int(input("Argument NOT provided. Enter a DEFAULT INT:  "))
            DEFAULT = u_input;
            return DEFAULT
        return get_max(args)
#Multiple arguments    
    else:
        length = len(args)
        #When the second argument is specified as "KEY"
        if length == 2 and  args[1] == "KEY":
            container = []
            KEY = "history"
            for obj in args[0]:
                container.append(obj[KEY])
                
            max_num = None
            if not isinstance(container,list):                                            
                return "Error: item is not interable"                               
            max_num = container[0]                                                        
            for item in container:                                                        
                if isinstance(item,(float,int)):                                    
                    if max_num < item:                                              
                        max_num = item                                              
                    else:                                                           
                        max_num = max_num
            return max_num 

#Multile Args >= 3
        arg_list = [];
        if key_spcf_com(args) == True:              #Key specified Int comparision
            spef = str(input("KEY Specifiction (int/str)   "))    
            #Key specified as string OR integer
            return key_int_str(spef, args, length)


#Multiple arguments of Int 
        for i in range(length):
            arg_list.append(args[i])
        max_num = None
        if not isinstance(arg_list,list):
            return max_num
        max_num = arg_list[0]
        for item in arg_list:
            if isinstance(item,(float,int)):
                if max_num < item:
                    max_num = item
                else:
                    max_num = max_num
        return max_num





if __name__ == "__main__":
    #Call the MAX funciton with numbers of input
    print("                      Bigest Float  ", my_max(1,2,3,4,5.5))

    print("                        Bigest Int  ", my_max(1,2,3,2.4,6))

    print("                     Iterable item  ", my_max([1,2,3,2.4,7]))

    print("              Default & Empty Item  ", my_max("DEFAULT"))

    print("                 KEY specified MAX  ", my_max(LIST, "KEY"))

    print("     KEY specificed Integer/String  ", my_max(1,2,'3',"KEY"))



