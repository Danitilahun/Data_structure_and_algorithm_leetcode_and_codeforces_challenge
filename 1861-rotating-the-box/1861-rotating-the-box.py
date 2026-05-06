class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        
        for row in range(rows):
            empty_spot = cols - 1
            
            for j in range(cols - 1, -1, -1):
                if boxGrid[row][j] == "*":
                    empty_spot = j - 1
                elif boxGrid[row][j] == "#":
                    boxGrid[row][j] = "."
                    boxGrid[row][empty_spot] = "#"
                    empty_spot -= 1
                    
        return[list(row) for row in zip(*boxGrid[::-1])]