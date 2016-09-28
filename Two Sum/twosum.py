# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def createList(self, a):
        if a is None:
            print 'no elements'
            return
        head = ListNode(a[0])
        p = head
        i = 1
        n = len(a)
        while i < n:
            t = ListNode(a[i])
            p.next = t
            p = t
            i = i + 1
        return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                print v1
                l1 = l1.next
            if l2:
                v2 = l2.val
                #print v2
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


a = Solution()
L1 = ListNode([2, 4, 3])
L2 = ListNode([5, 6, 4])

b = a.addTwoNumbers(L1, L2)
print b