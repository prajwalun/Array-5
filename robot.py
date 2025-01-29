# The isRobotBounded method determines if a robot remains in a bounded cycle after executing instructions.

# Approach:
# - Track position `(x, y)` and direction `(dirX, dirY)`.
# - 'G' moves forward, 'L' rotates left, 'R' rotates right.
# - The robot is bounded if:
#   - It returns to (0,0) or 
#   - It does not face its original direction after one cycle.

# TC: O(n) - Single pass through instructions.
# SC: O(1) - Constant space usage.


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        x, y = 0, 0

        for d in instructions:
            if d == "G":
                x, y = x + dirX, y + dirY
            elif d == "L":
                dirX, dirY = -dirY, dirX
            else:
                dirX, dirY = dirY, -dirX

        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)