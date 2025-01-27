import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        # Check if all the cells in the sentence are mines
        if len(self.cells) == self.count:
            # If the count matches the number of cells, return all the cells as mines
            return  set (self.cells)
        # If not, return an empty set (no definitive information about mines)
        return set()

    def known_safes(self):
        # Check if the count is 0 ( No mine )
        if self.count == 0:
            # If true, return all the cells as safe
            return set(self.cells)
        # Else return an empty set
        return set()

    def mark_mine(self, cell):
        # Check if the cell is part of this sentence
        if cell in self.cells:
            # Remove the cell from the set of cells ----> confirmed as a mine
            self.cells.remove(cell)
            # Decrement mine count
            self.count -= 1

    def mark_safe(self, cell):
        # Check if the cell is part of this sentence
       if cell in self.cells:
           # Remove the cell from the set of cells ----> confirmed as safe
           self.cells.remove(cell)

class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        # 1. Mark the cell as a move made and as safe
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # 2. Collect all neighboring cells and count known mines
        all_neighbors = set()
        known_mines_in_neighbors = 0

        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                neighbor = (i, j)
                # Skip the cell itself and out-of-bounds
                if (i, j) == cell or not (0 <= i < self.height and 0 <= j < self.width):
                    continue
                all_neighbors.add(neighbor)
                if neighbor in self.mines:
                    known_mines_in_neighbors += 1

        # 3. Calculate adjusted count and valid neighbors
        adjusted_count = count - known_mines_in_neighbors
        valid_neighbors = {n for n in all_neighbors if n not in self.safes and n not in self.mines}

        # 4. Add the new sentence with adjusted count
        new_sentence = Sentence(valid_neighbors, adjusted_count)
        self.knowledge.append(new_sentence)

        # 5. Iteratively update knowledge until no changes
        updated = True
        while updated:
            updated = False

            # Check for known mines/safes in all sentences
            for sentence in self.knowledge.copy():
                # Mark mines
                for mine in sentence.known_mines().copy():
                    if mine not in self.mines:
                        self.mark_mine(mine)
                        updated = True

                # Mark safes
                for safe in sentence.known_safes().copy():
                    if safe not in self.safes:
                        self.mark_safe(safe)
                        updated = True

            # Remove empty sentences
            self.knowledge = [s for s in self.knowledge if len(s.cells) > 0]

            # Infer new sentences using subset rule
            new_sentences = []
            for sentence1 in self.knowledge:
                for sentence2 in self.knowledge:
                    if sentence1 == sentence2:
                        continue
                    if sentence1.cells.issubset(sentence2.cells):
                        new_cells = sentence2.cells - sentence1.cells
                        new_count = sentence2.count - sentence1.count
                        if new_count >= 0 and len(new_cells) >= new_count:
                            new_sentence = Sentence(new_cells, new_count)
                            if new_sentence not in self.knowledge and new_sentence not in new_sentences:
                                new_sentences.append(new_sentence)
                                updated = True

            self.knowledge.extend(new_sentences)

    def make_safe_move(self):
        # Loop through all cells known to be safe
        for cell in self.safes:
            # Check if the cell has not already been clicked
            if cell not in self.moves_made:
                # Return the first safe cell that hasn't been clicked
                return cell
        # If no safe moves are available, return None
        return None

    def make_random_move(self):
        # Initialize a list to store possible moves
        possible_moves = []
        # Loop through all cells on the board
        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)

                # Add the cell to possible moves if it is neither clicked nor a mine
                if cell not in self.moves_made and cell not in self.mines:
                    possible_moves.append(cell)

        # Return a random choice from possible moves if any exist, otherwise return None
        return random.choice(possible_moves) if possible_moves else None
