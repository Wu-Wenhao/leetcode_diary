# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 添加一个虚拟结点
        dummy_head = ListNode(val=0, next=head)
        cur = dummy_head
        while(cur.next != None):
            if cur.next.val == val:
                # 如果cur下一个结点需要被删除
                # 直接跳过原来的cur.next结点
                # 将cur直接指向cur.next.next
                # 并返回while进行判断
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy_head.next