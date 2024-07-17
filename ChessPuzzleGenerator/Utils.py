class Utils:
    @staticmethod
    def squareCoordsCoverter(coords):
        row = 8 - int(coords[1])
        x = coords[0]
        match x:
            case 'a': col = 0
            case 'b': col = 1
            case 'c': col = 2
            case 'd': col = 3
            case 'e': col = 4
            case 'f': col = 5
            case 'g': col = 6
            case 'h': col = 7
        return (row,col)

    @staticmethod
    def fenToBoard(fen):
        listFen = fen.split()
        boardFen = listFen[0].split('/')
        board = [[0 for _ in range(8)] for _ in range(8)]
        i = 0
        for row in boardFen:
            j = 0
            for x in row:
                if x.isdigit():
                    j -= 1
                    for k in range(int(x)):
                        j += 1
                        board[i][j] = "-"
                else:
                    board[i][j] = x
                j += 1
            i += 1
        return board
    @staticmethod
    def boardToFen(board):
        fen = ""
        count = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "-":
                    count += 1
                elif count != 0:
                    fen += str(count)
                    count = 0
                    fen += board[i][j]
                else:
                    fen += board[i][j]
            if count != 0:
                fen += str(count)
            count = 0
            fen += "/"
        return fen[:-1]
