
from queue import Queue
def get_reduced_string(input_string):

    q = Queue(maxsize=500)

    for ch in input_string:
        q.put(ch)
    
    reduced_string_list = []
    while(not q.empty()):
        element1 = q.get()
        if not q.empty():
            element2 = q.get()
            if element1 != element2:
                reduced_string_list.append(element1)
                reduced_string_list.append(element2)
            # reduced_string += element2
        else:
            if element1 not in reduced_string_list:
                reduced_string_list.append(element1)
    
    return ''.join(reduced_string_list)

    
input_string = input("Enter the input string: ")
print("Reduced String {}".format(get_reduced_string(input_string)))


        
