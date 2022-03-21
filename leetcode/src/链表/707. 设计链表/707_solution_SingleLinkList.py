from ast import Delete


class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkList():
    '''单链表'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self._head is None
    
    def length(self):
        '''链表长度'''
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指向None表示到达尾部
        while cur is not None:
            #指针下移
            cur = cur.next
            count += 1
        return count

    def items(self):
        '''遍历链表'''
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next
    
    def addAtHead(self, item):
        '''向链表头部添加元素'''
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    def addAtTail(self, item):
        '''向链表尾部添加元素'''
        node = Node(item)
        # 先判断是否为空链表
        if self.is_empty():
            # 空链表，_head 指向新结点
            self._head = node
        else:
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    
    def addAtIndex(self, index, item):
        '''向指定位置插入元素'''
        # 特殊情况1 指定位置在第一个元素前，在头部插入
        if index <= 0:
            self.add(item)
        # 特殊情况2 指定位置在最后一个元素后，在尾部插入
        elif index >= self.length():
            self.append(item)
        # 其余正常情况
        else:
            node = Node(item)
            cur = self._head
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
    
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length():
            return 
        elif index == 0:
            self._head = self._head.next()
        else:
            cur = self._head
            for i in range(i - 1):
                cur = cur.next
            cur.next = cur.next.next
            

            
    def remove(self, item):
        '''删除结点'''
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个结点（即head就是要删除的结点）
                if pre is None:
                    # 将头指针指向head后一个结点
                    self._head = cur.next
                else:
                    # 将前一个位置结点直接指向下一个位置，跳过cur结点
                    pre.next = cur.next
                return True
            else:
                # 按照链表后移结点
                pre = cur
                cur = cur.next
    def find(self, item):
        '''查找元素是否存在'''
        return item in self.items()
