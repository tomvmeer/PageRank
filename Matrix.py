class NewMatrix:
    def __init__(self, h, w):
        self.w = w
        self.h = h
        empty = []
        for p in range(0, self.h):
            empty_x = []
            for i in range(0, self.w):
                empty_x.append(0)
            empty.append(empty_x)
        self.empty = empty

    def print_out(self):
        length_list = []
        for y in self.empty:
            for x in y:
                length_list.append(len(str(x)))
        space = int(max(length_list))
        for i in self.empty:
            row = ""
            for p in i:
                ammount = space - len(str(p))+1
                row = row + ammount*" " + str(p)
            print(row)

    def adv_set_row(self, row, y):
        for i in range(0, len(row)):
            self.empty[y][i] = row[i]

    def adv_set_col(self, col, x):
        for i in range(0, len(col)):
            self.empty[i][x] = col[i]

    def set(self, val, x, y):
        self.empty[y][x] = val


def addition(matrix1, matrix2):
    if matrix1.w == matrix2.w:
        if matrix1.h == matrix2.h:
            result = NewMatrix(matrix1.h, matrix1.w)
            for y in range(0, matrix1.h):
                for x in range(0, matrix2.h):
                    result.set((matrix1.empty[y][x]+matrix2.empty[y][x]), x, y)
            return result
    else:
        return 0


def multiplication(matrix1, matrix2):
    if matrix1.w == matrix2.h or matrix1.h == matrix2.w:
        if matrix1.w > matrix2.w:
            matrix_a = matrix1
            matrix_b = matrix2
        else:
            matrix_a = matrix2
            matrix_b = matrix1
        result = NewMatrix(matrix_a.h, matrix_b.w)
        xresult, yresult = 0, 0
        for y in matrix_a.empty:
            for i in range(0, matrix_b.w):
                sum = 0
                columns = []
                for row in matrix_b.empty:
                    columns.append(row[i])
                for p in range(0,len(columns)):
                    sum = sum + y[p]*columns[p]
                result.set(sum, xresult, yresult)
                if xresult < result.w-1:
                    xresult = xresult + 1
                else:
                    xresult = 0
                    yresult = yresult + 1
        return result
    else:
        return 0


def multiplication_number(matrix, number):
    result = NewMatrix(matrix.h, matrix.w)
    for y in range(0, len(matrix.empty)):
        for x in range(0, len(matrix.empty[y])):
            result.set((matrix.empty[y][x])*number, x, y)
    return result
