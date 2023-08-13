# merge two sorted linked list

def merge_list(self,list1,list2):
    temp = Node()
    pointer = temp

    while list1 is not None and list2 is not None:
        if list1.getData() < list2.getData():
            pointer.setNext(list1)
            list1 = list1.getNext()
        else:
            pointer.setNext(list2)
            list2 = list2.getNext()
        pointer = pointer.getNext()
        if list1 is None:
            pointer.setNext(list2)
        else:
            pointer.setNext(list1)
        return temp.getNext()
