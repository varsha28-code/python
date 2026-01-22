class Solution:
    def rectangleCount(self, A):
        count = 0
        import math
        
        for B in range(1, int(math.sqrt(A)) + 1):
            if A % B == 0:
                L = A // B

                # Ensure L >= B (avoid duplicates)
                if L < B:
                    continue

                # Condition when both even
                if L % 2 == 0 and B % 2 == 0:
                    if L == B:
                        count += 1
                else:
                    count += 1
        
        return count
