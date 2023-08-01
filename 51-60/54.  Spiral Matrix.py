'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

def spiralOrder(matrix):
    answer = []
    while matrix:
        # left to right
        answer += matrix.pop(0)
        if not matrix:
            break

        # top to bot
        for i in matrix:
            answer += [i.pop()]
            if not matrix[-1]:      # if last sub arr is empty return answer
                return answer

        # right to left
        answer += matrix.pop()[::-1]
        if not matrix:
            break

        # bot to top
        for i in matrix[::-1]:
            answer += [i.pop(0)]
            if not matrix[0]:       # if first sub arr is empty return answer
                return answer

    return answer

matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
'''
[
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15,16]]

out: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,10,11]
real:[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
'''
spiralOrder(matrix)