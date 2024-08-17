class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
        return

    def list_to_linkedlist(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def length(self):
        counter = 1
        if self.head == None:
            return 0
        else:
            itr = self.head
            while itr.next:
                counter += 1
                itr = itr.next

        return counter

    def remove_at(self, index):
        curr_ind = 0
        if self.head == None:
            return

        elif index > self.length() or index < 0:
            raise Exception("Invalid index")

        elif index == 0:
            self.head = self.head.next

        else:
            itr = self.head
            while curr_ind + 1 != index:
                itr = itr.next
                curr_ind += 1

            itr.next = itr.next.next

    def insert_at(self, data, index):
        curr_ind = 0
        if index == 0:
            node = Node(data, self.head)
            self.head = node

        elif index > self.length() or index < 0:
            raise Exception("Invalid index")

        else:
            itr = self.head
            while curr_ind + 1 != index:
                itr = itr.next
                curr_ind += 1

            itr.next = Node(data, itr.next)

    def print(self):
        if self.head is None:
            print("Linkedlist is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            if itr.next:
                llstr += str(itr.data) + '--->'
                itr = itr.next
            else:
                llstr += str(itr.data)
                itr = itr.next

        print(llstr)
        return


if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_beginning(4)
    obj.insert_at_beginning(3)
    obj.insert_at_beginning(2)
    obj.insert_at_beginning(1)
    obj.insert_at_beginning(0)
    obj.insert_at_end(50)
    # obj.list_to_linkedlist([1,2,3,4,5,6])
    # print(obj.print())
    # print(obj.length())
    print(obj.insert_at('*', 4))
    print(obj.print())
