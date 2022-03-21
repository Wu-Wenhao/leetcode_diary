'''
链表

链表是一种通过指针串联在一起的数据结构,每一个节点由两部分组成,
一个是数据域一个是指针域,最后一个节点的指针指向null

数组插入删除慢，查找快
链表插入删除快，查找慢
'''

# 定义结点
class Node():
    '''单链表的结点'''
    def __init__(self, item):
        # item 存放数据元素
        self.item = item
        # next 指向下一个节点
        self.next = None

# 定义单链表
class simple_SingleLinkList():
    '''单链表'''
    def __init___(self):
        self._head = None

# 创建简单单链表
def create_simple_SingleLinkList():
    # 创建链表
    link_list = SingleLinkList()
    # 创建结点
    node1 = Node(1)
    node2 = Node(2)

    # 将结点添加到链表
    link_list._head = node1
    # 将第一个结点的next指针指向第二个结点
    node1.next = node2
    
    # 访问链表
    print(link_list._head.item)
    print(link_list._head.next.next)

# 链表中需要定义的一些操作方法
'''
is_empty() 链表是否为空
length() 链表长度
items() 获取链表数据迭代器
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
find(item) 查找节点是否存在
'''

# 定义一个完整的单链表
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
    
    def add(self, item):
        '''向链表头部添加元素'''
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    def append(self, item):
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
    
    def insert(self, index, item):
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

def test_SingleLinkList():
    link_list = SingleLinkList()
    # 向链表尾部添加数据
    for i in range(5):
        link_list.append(i)    
    # 向头部添加数据
    link_list.add(6)
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')
    # 链表数据插入数据
    link_list.insert(3, 9)
    print('\n', list(link_list.items()))
    # 删除链表数据
    link_list.remove(0)
    print('\n', list(link_list.items()))
    # 查找链表数据
    print(link_list.find(4))

if __name__ == '__main__':
    test_SingleLinkList()