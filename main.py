import tkinter as tk
import random

BOARD_SIZE = 500

def neg_symbol(sym):
    return "X" if sym == "O" else "O"

class TicTacToe:
    def __init__(self, n=3):
        """Set up the main window and create the top and board frames (n*n cells)."""
        self.n = n
        self.board = []  
        self.human = None
        self.computer = None
        self.current_player = None
        self.game_over = False
        self.turns = 0

        self.window = tk.Tk()
        self.window.title("TicTacToe")
        self.window.resizable(False, False) 

        self.top_frame = tk.Frame(self.window, height=max(100, BOARD_SIZE // 5), width=250)
        self.top_frame.pack()
        self.top_frame.pack_propagate(False)  
        self.status = tk.Label(self.top_frame, text="", font=("Consolas", 16))

        self.board_frame = tk.Frame(self.window, width=BOARD_SIZE, height=BOARD_SIZE)
        self.board_frame.pack()
        self.board_frame.grid_propagate(False)    

        self.create_board()
        self.symbol_selection()

    def set_symbol(self, i, j, sym):
        self.board[i][j]["text"] = sym 
        self.turns += 1
    
    def get_symbol(self, i, j):
        return self.board[i][j]["text"]
    
    def highlight_cells(self, cells, color):
        for i, j in cells:
            self.board[i][j].config(bg=color)

    def set_hover(self, enabled):
        for row in self.board:
            for button in row:
                if enabled:
                    button.config(activebackground="#dcdcdc")
                else:
                    button.config(activebackground=button.cget("bg"))

    def create_board(self):
        """Creates a board of n*n buttons and link them to `human_move`."""
        for i in range(self.n):
            self.board_frame.grid_rowconfigure(i, weight=1, uniform="row")
            self.board_frame.grid_columnconfigure(i, weight=1, uniform="col")

        if self.n <= 10:
            font_size = 28
        else:
            font_size = max(8, int(28 * 10 / self.n))

        for i in range(self.n):
            row = []
            for j in range(self.n):
                button = tk.Button(
                    self.board_frame,
                    font=("Consolas", font_size, "bold"),
                    width=2,
                    height=1,
                    bg="#f0f0f0",
                    activebackground="#dcdcdc",
                    relief="flat",
                    borderwidth=0,
                    highlightthickness=1,
                    highlightbackground="#cccccc",
                    command=lambda i=i, j=j: self.human_move(i, j)
                )
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.board.append(row)
        self.set_hover(False)

    def symbol_selection(self):
        """Let the user chose a symbol"""
        self.selection_frame = tk.Frame(self.top_frame)
        self.selection_frame.pack()
        label = tk.Label(self.selection_frame, text="Choose your symbol:", font=("Consolas", 16))
        label.pack(pady=5)

        self.btn_frame = tk.Frame(self.selection_frame)
        self.btn_frame.pack()
        for sym in ["O", "X"]:
            btn = tk.Button(self.btn_frame, text=f"{sym}", font=("Consolas", 16), width=4,
                            command=lambda sym=sym: self.start_game(sym))
            btn.pack(side="left", padx=20, pady=5)

    def start_game(self, sym):
        """Assign X/O to the players and start the game (update status)."""
        self.human = sym
        self.computer = neg_symbol(sym)
        self.current_player = random.choice([self.human, self.computer])

        self.selection_frame.destroy()

        self.status.config(text=f"{self.current_player}'s turn")
        self.status.pack(expand=True)
        self.set_hover(True)
    
        if self.current_player == self.computer:
            self.window.after(500, self.computer_move)

    def human_move(self, i, j):
        """Check if all the preconditions are met for the human 
        to make the (i, j) move, then call `make_move`. If the game 
        isn't over, start the computer's move."""
    
        if self.human is None or self.game_over or self.current_player != self.human:
            return
        
        if self.get_symbol(i, j) != "":
            return
        
        self.make_move(i, j, self.human)

        if not self.game_over:
            self.window.after(400, self.computer_move)

    def computer_move(self):
        """Randomly chose a free cell for the computer to make 
        the (i, j) move, then call `make_move`."""

        free_cells = []
        for i in range(self.n):
            for j in range(self.n):
                if self.get_symbol(i, j) == "":
                    free_cells.append((i, j))
        
        i, j = random.choice(free_cells)
        self.make_move(i, j, self.computer)

    def is_board_full(self):
        return self.turns == self.n * self.n
        
    def check_winner(self, sym, color=None):
        """Check lines, columns and diagonals for player with symbol `sym`.
        Return True if he won, False otherwise."""

        n = self.n
        lines = []

        for i in range(n):
            lines.append([(i, j) for j in range(n)])       # row i
            lines.append([(j, i) for j in range(n)])       # column i
        lines.append([(i, i) for i in range(n)])           # main diagonal
        lines.append([(i, n-i-1) for i in range(n)])       # anti-diagonal

        for line in lines:
            if all(self.get_symbol(i, j) == sym for i, j in line):
                self.highlight_cells(line, color)
                return True
        return False
    
    def make_move(self, i, j, sym):
        """Place a player's symbol at (i, j), check for endgame 
        then switch turns."""

        color = "#2ecc71" if sym == self.human else "#e74c3c"

        self.set_symbol(i, j, sym)

        if self.check_winner(sym, color):
            text = "You win!" if sym == self.human else "Computer wins!"
            self.end_game(text)
            return
        
        if self.is_board_full():
            self.end_game("It's a draw!")
            return
        
        self.current_player = neg_symbol(sym)
        self.status.config(text=f"{self.current_player}'s turn")

    def end_game(self, text):
        """Update game status and show play again button."""
        self.status.config(text=text)
        self.game_over = True
        self.set_hover(False)
        self.show_play_again()
    
    def show_play_again(self):
        """Show play again button and link it to `reset_game`"""
        self.play_again_btn = tk.Button(
            self.top_frame,
            text="Play Again",
            font=("Consolas", 12, "bold"),
            fg="white",
            bg="#3498db",
            activebackground="#2980b9",
            relief="flat",
            command=self.reset_game
        )
        self.play_again_btn.pack(pady=5)

    def reset_game(self):
        """Clear board and reset all game state, then display 
        symbol selection for the next game."""

        self.play_again_btn.destroy()
        self.status.pack_forget()

        for i in range(self.n):
            for j in range(self.n):
                self.set_symbol(i, j, "")
                self.board[i][j].config(bg="#f0f0f0")

        self.set_hover(False)

        self.human = None
        self.computer = None
        self.current_player = None
        self.game_over = False
        self.turns = 0

        self.symbol_selection()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe(n=3)
    game.run()
