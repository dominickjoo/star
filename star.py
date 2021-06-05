import numpy as np

# symbolic constants
EMPTY = 0
STAR = 1
SLASH = 2
DIRS = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

class StarGrid:

    def __init__(self, regions):
        self.board_len = len(regions)
        self.board = np.zeros((self.board_len, self.board_len), dtype=int)
        self.regions = regions

    def get_next_empty(self):
        for region in self.regions:
            for x, y in region:
                if self.board[x][y] == EMPTY:
                    return (x, y, region)

        return None

    def star_valid(self, pos, region):
        x, y = pos

        for i, j in DIRS:
            if (0 <= x+i <= self.board_len - 1 and
                0 <= y+j <= self.board_len - 1 and
                self.board[x+i][y+j] == STAR):
                return False

        if (np.bincount(self.board[x,:])[STAR] > 2 or
            np.bincount(self.board[:,y])[STAR] > 2 or
            np.bincount([self.board[x][y] for x, y in region])[STAR] > 2):
            return False

        return True

    def slash_valid(self, pos, region):
        x, y = pos
        n = self.board_len

        if (np.bincount(self.board[x,:])[SLASH] > n-2 or
            np.bincount(self.board[:,y])[SLASH] > n-2 or
            np.bincount([self.board[x][y] for x, y in region])[SLASH] > len(region)-2):
            return False

        return True

    def solve(self):
        cur_cell = self.get_next_empty()
        if not cur_cell:
            return True
        x, y, region = cur_cell

        self.board[x][y] = STAR
        # print(f"cur_cell: {cur_cell}")
        # print(self.board)
        if self.star_valid((x, y), region) and self.solve():
            return True
        self.board[x][y] = EMPTY
        # print(f"cur_cell: {cur_cell}")
        # print(self.board)

        self.board[x][y] = SLASH
        # print(f"cur_cell: {cur_cell}")
        # print(self.board)
        if self.slash_valid((x, y), region) and self.solve():
            return True
        self.board[x][y] = EMPTY
        # print(f"cur_cell: {cur_cell}")
        # print(self.board)

        return False

    def print_board(self):
        print(self.board)


if __name__ == "__main__":

    # 0 0 1 1 1 1 1 1 1 1
    # 0 0 1 2 3 3 3 3 3 3
    # 0 0 2 2 2 4 4 4 3 5
    # 0 0 2 2 2 2 2 4 5 5
    # 0 0 2 2 2 6 5 5 5 5
    # 6 6 6 6 6 6 7 5 5 5
    # 8 8 6 6 6 7 7 5 5 5
    # 8 8 9 9 9 7 7 7 7 5
    # 8 8 8 9 9 9 9 9 7 7
    # 8 8 8 8 9 9 9 9 7 7

    # region0 = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1),(4,0),(4,1)]
    # region1 = [(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(1,2)]
    # region2 = [(1,3),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(3,5),(3,6),(4,2),(4,3),(4,4)]
    # region3 = [(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,8)]
    # region4 = [(2,5),(2,6),(2,7),(3,7)]
    # region5 = [(2,9),(3,8),(3,9),(4,6),(4,7),(4,8),(4,9),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9),(7,9)]
    # region6 = [(4,5),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(6,2),(6,3),(6,4)]
    # region7 = [(5,6),(6,5),(6,6),(7,5),(7,6),(7,7),(7,8),(8,8),(8,9),(9,8),(9,9)]
    # region8 = [(6,0),(6,1),(7,0),(7,1),(8,0),(8,1),(8,2),(9,0),(9,1),(9,2),(9,3)]
    # region9 = [(7,2),(7,3),(7,4),(8,3),(8,4),(8,5),(8,6),(8,7),(9,4),(9,5),(9,6),(9,7)]
    # regions = [region0,region1,region2,region3,region4,region5,region6,region7,region8,region9]

    # 0 1 1 1 1 2 2 2 3 3
    # 0 0 0 4 1 1 2 2 2 3
    # 0 0 4 4 4 1 2 2 3 3
    # 4 4 4 5 4 2 2 2 6 3
    # 4 4 4 5 5 5 5 2 6 3
    # 4 5 5 5 5 2 2 2 6 3
    # 5 5 7 8 5 8 8 6 6 3
    # 5 5 7 8 8 8 8 6 6 3
    # 5 5 7 9 8 9 6 6 6 6
    # 5 7 7 9 9 9 9 9 9 9
# 0111122233
# 0004112223
# 0044412233
# 4445422263
# 4445555263
# 4555522263
# 5578588663
# 5578888663
# 5579896666
# 5779999999

    region0 = [(0,0),(1,0),(1,1),(1,2),(2,0),(2,1)]
    region1 = [(0,1),(0,2),(0,3),(0,4),(1,4),(1,5),(2,5)]
    region2 = [(0,5),(0,6),(0,7),(1,6),(1,7),(1,8),(2,6),(2,7),(3,5),(3,6),(3,7),(4,7),(5,5),(5,6),(5,7)]
    region3 = [(0,8),(0,9),(1,9),(2,8),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9)]
    region4 = [(1,3),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,4),(4,0),(4,1),(4,2),(5,0)]
    region5 = [(3,3),(4,3),(4,4),(4,5),(4,6),(5,1),(5,2),(5,3),(5,4),(6,0),(6,1),(6,4),(7,0),(7,1),(8,0),(8,1),(9,0)]
    region6 = [(3,8),(4,8),(5,8),(6,7),(6,8),(7,7),(7,8),(8,6),(8,7),(8,8),(8,9)]
    region7 = [(6,2),(7,2),(8,2),(9,1),(9,2)]
    region8 = [(6,3),(6,5),(6,6),(7,3),(7,4),(7,5),(7,6),(8,4)]
    region9 = [(8,3),(8,5),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)]
    regions = [region0,region1,region2,region3,region4,region5,region6,region7,region8,region9]

    sg = StarGrid(regions)
    sg.solve()
    sg.print_board()
