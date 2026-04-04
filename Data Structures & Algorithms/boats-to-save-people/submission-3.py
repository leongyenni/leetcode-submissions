class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        l, r = 0, len(people) - 1
        
        people = sorted(people)

        while l <= r:

            if l != r and people[l] + people[r] <= limit:
                l += 1
                r -= 1
                count += 1

            elif people[l] + people[r] > limit:
                r -= 1
                count += 1

            else:
                l += 1
                count += 1


        return count