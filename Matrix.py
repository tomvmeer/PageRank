#!/usr/bin/python

"""" Module for creating matrices as a class and manipulating those matrix-classes"""

__author__ = "Tom van Meer"


class NewMatrix:
    # Initiating the matrix class with height and with h, w:
    def __init__(self, h, w):
        self.w = w
        self.h = h
        empty = []
        for p in range(0, self.h):
            empty_x = []
            for i in range(0, self.w):
                empty_x.append(0)
            empty.append(empty_x)
        self.matrix = empty  # empty is the empty matrix

    # Function for printing out the formatted matrix
    def print_out(self):
        length_list = []
        for y in self.matrix:
            for x in y:
                length_list.append(len(str(x)))
        space = int(max(length_list))
        for i in self.matrix:
            row = ""
            for p in i:
                ammount = space - len(str(p))+1
                row = row + ammount*" " + str(p)
            print(row)

    # Function for setting an entire row of a matrix to list [row]
    def adv_set_row(self, row, y):
        for i in range(0, len(row)):
            self.matrix[y][i] = row[i]

    # Function for setting an entire column of a matrix to list [col]
    def adv_set_col(self, col, x):
        for i in range(0, len(col)):
            self.matrix[i][x] = col[i]

    # Function for setting 1 value val of the matrix on pos x,y
    def set(self, val, x, y):
        self.matrix[y][x] = val


# Function for adding 2 matrices, returns error if sizes are not equal
def addition(matrix1, matrix2):
    if matrix1.w == matrix2.w and matrix1.h == matrix2.h:
        result = NewMatrix(matrix1.h, matrix1.w)
        for y in range(0, matrix1.h):
            for x in range(0, matrix2.h):
                result.set((matrix1.matrix[y][x]+matrix2.matrix[y][x]), x, y)
        return result
    else:
        raise IndexError("Entered matrix with non-valid dimensions!")


# Function for multiplying 2 matrices, returns error if sizes are incorrect
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
        for y in matrix_a.matrix:
            for i in range(0, matrix_b.w):
                sum = 0
                columns = []
                for row in matrix_b.matrix:
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
        raise IndexError("Entered matrix with non-valid dimensions!")


# Function for multiplying an entire matrix with a number
def multiplication_number(matrix1, number):
    result = NewMatrix(matrix1.h, matrix1.w)
    for y in range(0, len(matrix1.matrix)):
        for x in range(0, len(matrix1.matrix[y])):
            result.set((matrix1.matrix[y][x])*number, x, y)
    return result
