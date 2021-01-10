from typing import List


class Solution:

    def move(self, pos, index, _type):
        """
        @param pos:    当前密码
        @param index:  第几个密码 从0计数
        @param _type:  向上还是向下
        @return:
        """
        if _type == "up":
            if pos[index] == "0":
                return pos[:index] + "9" + pos[index+1:]
            else:
                return pos[:index] + str(int(pos[index]) - 1) + pos[index + 1:]
        elif _type == "down":
            if pos[index] == "9":
                return pos[:index] + "0" + pos[index+1:]
            else:
                return pos[:index] + str(int(pos[index]) + 1) + pos[index + 1:]


    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        has_checked = set()

        help_stack = list()
        help_stack.append("0000")
        result = 0

        while len(help_stack) != 0:
            now_stack = []
            for now_pos in help_stack:
                if now_pos in has_checked:
                    continue
                if now_pos in deadends:
                    continue
                if now_pos == target:
                    return result
                for i in range(4):
                    moved_pos = self.move(now_pos, i, "down")
                    now_stack.append(moved_pos)
                    moved_pos = self.move(now_pos, i, "up")
                    now_stack.append(moved_pos)
                has_checked.add(now_pos)
            help_stack = now_stack
            result += 1

        return -1


if __name__ == '__main__':

    s = Solution()
    print(s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
    print(s.openLock(["0000", "0101", "0102", "1212", "2002"], "0202"))
    print(s.openLock(["8888"], "0009"))
