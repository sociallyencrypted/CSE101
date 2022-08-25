from urllib.parse import ParseResultBytes


n = int(input())
x = int(input())
y = int(input())
t = int(input())
u = int(input())
v = int(input())


def bishop(x, y, t, u, v):
    if (x + y) % 2 != (u + v) % 2:
        return False
    else:
        if t == 0:
            if x == u and v == y:
                return True
            else:
                return False
        elif t == 1:
            if x + y == u + v or abs(x - y) == abs(u - v):
                return True
            else:
                return False
        else:
            return True


def rook(x, y, t, u, v):
    if t >= 2:
        return True
    elif t == 1:
        if x == u or y == v:
            return True
        else:
            return False
    else:
        if x == u and v == y:
            return True
        else:
            return False


def queen(x, y, t, u, v):
    if t >= 2:
        return True
    elif t == 1:
        if x == u or y == v or x + y == u + v or abs(x - y) == abs(u - v):
            return True
        else:
            return False
    else:
        if x == u and v == y:
            return True
        else:
            return False


board = [[False] * n] * n


def knightmoves(n, x, y):

    l = [
        (x + a, y + b)
        for a in [-1, -2, 1, 2]
        for b in [-1, -2, 1, 2]
        if abs(a) != abs(b)
        and x + a in range(n)
        and y + b in range(n)
        and board[x + a][y + b] == False
    ]
    return l


def knightColour(n, x, y, t, u, v):
    if t > 0:
        kn = knightmoves(n, x, y)
        for c in kn:
            if c == (u, v):
                board[u][v] = True
                pass
            else:
                a = c[0]
                b = c[1]
                board[a][b] = True
                knightColour(n, a, b, t - 1, u, v)


def knight(n, x, y, t, u, v):
    board[x][y] = True
    knightColour(n, x, y, t, u, v)
    return board[u][v]


print("Knight:", knight(n, x, y, t, u, v))
print("Queen:", queen(x, y, t, u, v))
print("Bishop:", bishop(x, y, t, u, v))
print("Rook:", rook(x, y, t, u, v))
