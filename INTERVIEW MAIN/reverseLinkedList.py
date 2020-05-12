# input = [1,2,3,4,5]
# Linked List       [1]->[2]->[3]->[4]->[5]->
# Wrong!!!          [5]->[4]->[3]->[2]->[1]->
# Instead of reversing the nodes, just reverse the pointers themselves.
# New Linked List   <-[1]<-[2]<-[3]<-[4]<-[5]
# Don't change      self.val = x
#       Change      self.next.....
# We iterate over the list, and reverse each pointer.


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

    def reverseList(self, head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


"""
We are given the head. 
prev start at the beginning (nothing)
While head exists, we cycle through.
     temp/head
prev    [1]        -> [2] -> [3] -> [4] -> [5] ->   (prev = None,  temp = head)

        temp          head
prev    [1]        -> [2] -> [3] -> [4] -> [5] ->   (head = head.next)

        temp          head
prev  <-[1]           [2] -> [3] -> [4] -> [5] ->   (temp.next = prev)  Change the pointer

     prev/temp        head
      <-[1]           [2] -> [3] -> [4] -> [5] ->   (prev = temp)

Next Iteration
        prev      temp/head
      <-[1]           [2] -> [3] -> [4] -> [5] ->   (temp = head)
      
        prev         temp   head
      <-[1]           [2] -> [3] -> [4] -> [5] ->   (head = head.next)
      
        prev         temp   head
      <-[1]    <-     [2]    [3] -> [4] -> [5] ->   (temp.next = prev)
      
                    prev  temp/head
      <-[1]    <-     [2]    [3] -> [4] -> [5] ->   (temp.next = prev)   
"""