class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for num in asteroids:
            while stack and num < 0 < stack[-1]:
                top = stack.pop()

                if abs(top) == abs(num):
                    break

                elif abs(top) > abs(num):
                    stack.append(top)
                    break
            else:
                stack.append(num)
        
        return stack
                    
