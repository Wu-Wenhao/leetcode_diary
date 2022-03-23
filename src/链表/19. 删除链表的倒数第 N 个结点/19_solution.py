# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from multiprocessing import dummy


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        方法一 笨方法 两次遍历
        '''
        # dummy_head = ListNode(val=0, next=head)
        # cur = dummy_head
        # count = 0
        # while cur is not None:
        #     cur = cur.next
        #     count += 1
        # cur = dummy_head
        # for i in range(count-n-1):
        #     cur = cur.next
        # cur.next = cur.next.next
        # return dummy_head.next
        '''
        方法二 双指针法
        '''
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(val=0, next=head)
        fast = dummy_head
        slow = dummy_head
        # fast先往前走n步
        for i in range(n):
            fast = fast.next
        # 需要注意fast.next is not None 和 fast is not None的区别
        # fast is not None 判断结束之后再多走一步会让fast停到None 
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        # fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next
        return dummy_head.next

