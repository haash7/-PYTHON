 class Solution(object):
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):

            if i == 0:
                triangle.append([1])

            elif i == 1:
                triangle.append([1, 1])

            else:
                row = [1]

                

                