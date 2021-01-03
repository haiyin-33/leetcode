class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        orig_head, cnt = head, 1  # cnt如果会遍历到none，就从0开始计数（右开空间），如果遍历到最后有效位，就从1开始（右闭空间）
        while head.next:  # head遍历到了最后一位
            head, cnt = head.next, cnt + 1  # cnt若从1开始，且紧跟着head，那么pointer最终停到哪，cnt就包括到哪。是完全相同的
        head.next = orig_head  # 首尾连接上

        step = cnt - k % cnt - 1  # 计算有效移动步数
        while step > 0:
            orig_head, step = orig_head.next, step - 1

        new_head, orig_head.next = orig_head.next, None
        return new_head
