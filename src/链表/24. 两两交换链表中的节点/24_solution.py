'''
关键在于虚拟结点 
不用考虑没有pre的头节点
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(val=0, next=head)
        pre = dummy_head
        
        while pre.next is not None and pre.next.next is not None:
            cur = pre.next
            post = pre.next.next
            '''
            按照步骤一二三+临时存储的写法，已通过
            pre.next = post
            temp = post.next
            post.next = cur
            cur.next = temp
            '''

            #不用临时间接写法
            pre.next = post
            cur.next = post.next
            post.next = cur
            
            pre = pre.next.next

        return dummy_head.next
