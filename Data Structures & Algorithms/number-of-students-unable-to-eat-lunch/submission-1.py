class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # students
        # sandwiches
        res = len(students)
        cnt = {}

        for s in students:
            if s not in cnt:
                cnt[s] = 0
            cnt[s] += 1
        for sandwich in sandwiches:
            if cnt.get(sandwich, 0) == 0:
                break
            cnt[sandwich] -= 1
            res -= 1

        return res