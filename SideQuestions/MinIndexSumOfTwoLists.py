#  Suppose Andy and Doris want to choose a restaurant for dinner,
#  and they both have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.
from typing import List


class Solution:
    def findRestaurant(self, A: List[str], B: List[str]) -> List[str]:
        #associate index with every value u, then create dictionary value:index
        Aindex = {u: i for i, u in enumerate(A)}
        best, ans = 1e9, []

        for j, v in enumerate(B):
            #get dictionary key value v, if not in A then return 1e9
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]

    print(sol.findRestaurant(list1,list2))
