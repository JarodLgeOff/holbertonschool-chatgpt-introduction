def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 5)


def check_winner(board):
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	for col in range(3):
		if board[0][col] == board[1][col] == board[2][col] != " ":
			return True

	if board[0][0] == board[1][1] == board[2][2] != " ":
		return True

	if board[0][2] == board[1][1] == board[2][0] != " ":
		return True

	return False


def board_full(board):
	return all(cell != " " for row in board for cell in row)


def get_valid_input(player):
	while True:
		try:
			row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
			col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

			if row not in range(3) or col not in range(3):
				print("Coordinates must be between 0 and 2.")
				continue

			return row, col

		except ValueError:
			print("Invalid input. Please enter numbers only.")


def tic_tac_toe():
	board = [[" "] * 3 for _ in range(3)]
	player = "X"

	while True:
		print_board(board)

		row, col = get_valid_input(player)

		if board[row][col] != " ":
			print("That spot is already taken! Try again.")
			continue

		board[row][col] = player

		if check_winner(board):
			print_board(board)
			print(f"Player {player} wins!")
			break

		if board_full(board):
			print_board(board)
			print("It's a draw!")
			break

		player = "O" if player == "X" else "X"


tic_tac_toe()
