import tkinter as tk

# Size of square in grid
GRID_SQUARE_SIZE = 40
# Size of square in palette
PALETTE_SQUARE_SIZE = 30
# Size of space between squares in palette
SPACE_SIZE = 15
# Yellow, Orange, Red, Magenta, Purple, Blue, Cyan, Teal, Green, Lime
# https://colorswall.com/palette/73/
COLORS = ['#fff100', '#ff8c00', '#e81123', '#ec008c', '#68217a', '#00188f', '#00bcf2', '#00b294', '#009e49', '#bad80a']

class SolverGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Star Battle Solver")
        self.frame2 = None
        self.frame1 = tk.Frame(self)
        self.frame1.pack()

        num_regions_label = tk.Label(self.frame1, text="Number of rows/columns/regions (10 max):", padx=3, pady=3)
        num_regions_label.pack()

        num_regions_entry = tk.Entry(self.frame1, width=2)
        num_regions_entry.pack()

        generate_grid_button = tk.Button(self.frame1, text='Generate grid',command=lambda: self.draw_frame2(
                int(num_regions_entry.get()),
            ))
        generate_grid_button.pack()        

    def draw_frame2(self, num_regions):
        if self.frame2:
            self.frame2.destroy()

        self.num_regions = num_regions

        print(num_regions)

        self.frame2 = tk.Frame(self)
        self.frame2.pack()


        color_palette = tk.Canvas(self.frame2,
                    height=PALETTE_SQUARE_SIZE + 15,
                    width=PALETTE_SQUARE_SIZE*num_regions + SPACE_SIZE*(num_regions-1) + 30)
        color_palette.pack()

        for color_num in range(num_regions):
            color_palette.create_rectangle(
                color_num*(PALETTE_SQUARE_SIZE + SPACE_SIZE) + 15,
                15,
                color_num*(PALETTE_SQUARE_SIZE + SPACE_SIZE) + PALETTE_SQUARE_SIZE + 15,
                PALETTE_SQUARE_SIZE + 15,
                                        fill=COLORS[color_num])

        color_palette.bind("<Button-1>", self.get_color)


        self.grid = tk.Canvas(self.frame2,
                    height=GRID_SQUARE_SIZE*num_regions + 50,
                    width=GRID_SQUARE_SIZE*num_regions + 50)
        self.grid.pack()

        for row in range(num_regions):
            for col in range(num_regions):
                self.grid.create_rectangle(GRID_SQUARE_SIZE*col + 25, 
                                        GRID_SQUARE_SIZE*row + 25,
                                        GRID_SQUARE_SIZE*(col+1) + 25,
                                        GRID_SQUARE_SIZE*(row+1) + 25,
                                        fill='')

        self.grid.bind("<Button-1>", self.paint_square)

        num_stars_label = tk.Label(self.frame1, text="Number of stars per row/column/region:", padx=3, pady=3)
        num_stars_label.pack()

        num_stars_entry = tk.Entry(self.frame1, width=2)
        num_stars_entry.pack()

        solve_button = tk.Button(self.frame1, text='Solve!',command=None)
        solve_button.pack() 
        
        self.frame2.tkraise()

    def get_color(self, event):
        if event.y < 15 or (event.x % PALETTE_SQUARE_SIZE + SPACE_SIZE) < 15:
            return

        self.color = COLORS[event.x // (PALETTE_SQUARE_SIZE + SPACE_SIZE)]

        print(event.x, event.y)
        print(self.color)

    def paint_square(self, event):
        if not ((25 < event.x < GRID_SQUARE_SIZE*self.num_regions + 25) and (25 < event.y < GRID_SQUARE_SIZE*self.num_regions + 25)):
            return

        square_x = (event.x - 25) // GRID_SQUARE_SIZE 
        square_y = (event.y - 25) // GRID_SQUARE_SIZE 

        self.grid.create_rectangle(GRID_SQUARE_SIZE*square_x + 25, 
                                    GRID_SQUARE_SIZE*square_y + 25,
                                    GRID_SQUARE_SIZE*(square_x+1) + 25,
                                    GRID_SQUARE_SIZE*(square_y+1) + 25,
                                        fill=self.color)

solver = SolverGUI()
solver.mainloop()