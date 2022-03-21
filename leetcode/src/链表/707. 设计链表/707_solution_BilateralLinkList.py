## 失败的硬写

class LinkNode(object):
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length():
            return -1
        else:
            cur = self._head
            for i in range(index):
                cur = cur.next
            return cur.val 


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = LinkNode(val)
        node.next = self._head
        if self._head is not None:
            self._head.prev = node
        self._head = node


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = LinkNode(val)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            node.prev = cur
            cur.next = node



    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        node = LinkNode(val)
        #特殊情况1 指定位置在第一个元素前， 在头部插入：
        if index <= 0:
            self.addAtHead(val)
        elif index == self.length():
            self.addAtTail(val)
        elif index > self.length():
            return
        else:
            cur = self._head
            for i in range(index-1):
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next = node


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length():
            return
        # 删除第一个元素的情况
        elif index == 0:
            self._head = self._head.next
        else:
            cur = self._head
            for i in range(index - 1):
                cur = cur.next
            if cur.next.next is not None:
                cur.next.next.prev = cur
            cur.next = cur.next.next

    def show(self):
        cur = self._head
        while cur is not None:
            print(cur.val)
            cur = cur.next
        print('---------------')
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


def test():
    linkedList = MyLinkedList()
    linkedList.addAtIndex(0,10)
    linkedList.show() 
    linkedList.addAtIndex(0,20) 
    linkedList.show()
    linkedList.addAtIndex(1,30) 
    linkedList.show()
    print(linkedList.get(0))

if __name__ == '__main__':
    test()