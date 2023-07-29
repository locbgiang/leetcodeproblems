'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
'''
first = 0
last= len(matrix) - 1

while first < last:
    for i in range(first, last):
        temp = matrix[first][i]
        matrix[first][i] = matrix[(len(matrix)-1)-i][first]
        matrix[(len(matrix)-1)-i][first] = matrix[last][(len(matrix)-1)-i]
        matrix[last][(len(matrix)-1)-i] = matrix[i][last]
        matrix[i][last] = temp
    first +=1
    last -=1
'''


def rotate(matrix):
    first, last = 0, len(matrix) - 1
    while first < last:
        for i in range(first, last):
            temp = matrix[first][first+i]
            matrix[first][first+i] = matrix[last-i][first]
            matrix[last-i][first] = matrix[last][last-i]
            matrix[last][last-i] = matrix[first+i][last]
            matrix[first+i][last] = temp
        first += 1
        last -= 1
    print(matrix)
    return
    

matrix = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]]
matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
rotate(matrix2)