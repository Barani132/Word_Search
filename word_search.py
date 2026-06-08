#Word Search (Backtracking Grid)
board = [
 ['A','B','C','E'],
 ['S','F','C','S'],
 ['A','D','E','E']
]

word = "ABCCED"
def dfs(i, j, k):
    if k == len(word):
        return True
    if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != word[k]:
        return False

    temp = board[i][j]
    board[i][j] = "#"

    found = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or
             dfs(i,j+1,k+1) or dfs(i,j-1,k+1))

    board[i][j] = temp
    return found

print(dfs(0,0,0))
