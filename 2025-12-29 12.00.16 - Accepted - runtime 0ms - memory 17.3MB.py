class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # We need to buy items such that we get at least need1 units of type1
        # and at least need2 units of type2
        # Type 1: costs cost1, gives 1 to need1
        # Type 2: costs cost2, gives 1 to need2
        # Type 3 (both): costs costBoth, gives 1 to both
        
        # Let x = number of "both" type items
        # Cost = x * costBoth + max(0, need1 - x) * cost1 + max(0, need2 - x) * cost2
        
        # The function is piecewise linear with changes at x = need1 and x = need2
        # We should check x = 0, min(need1, need2), max(need1, need2)
        
        def calc_cost(x):
            remaining1 = max(0, need1 - x)
            remaining2 = max(0, need2 - x)
            return x * costBoth + remaining1 * cost1 + remaining2 * cost2
        
        # Check key points
        result = calc_cost(0)
        result = min(result, calc_cost(min(need1, need2)))
        result = min(result, calc_cost(max(need1, need2)))
        
        return result