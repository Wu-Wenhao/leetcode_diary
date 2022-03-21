'''
这道题还有一个迭代解法
暂时还看不太懂迭代
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur is not None:
            # 记录一下cur.next原本方向，因为马上要扭转cur.next方向
            temp = cur.next
            cur.next = pre
            # 更新pre和cur
            pre = cur
            cur = temp
        # 注意这里return的是pre不是cur，因为虽然判断条件是cur is not None
        # 但最后cur更新了一下到None，结束时的pre是原链表最后一个节点
        return pre