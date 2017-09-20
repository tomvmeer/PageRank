import Matrix
import time

m = Matrix.NewMatrix(4, 2)
m.adv_set_col([9, 7, 5, 3], 0)
m.adv_set_col([8, 6, 4, 2], 1)
m.print_out()

print("")
m2 = Matrix.NewMatrix(3,4)
m2.adv_set_row([1, 2, 3, 4], 0)
m2.adv_set_row([5, 6, 7, 8], 1)
m2.adv_set_row([9, 0, -1, -2], 2)
m2.print_out()
print("")

m3 = Matrix.multiplication(m, m2)
m3.print_out()
print("")

m4 = Matrix.NewMatrix(2, 3)
m4.adv_set_row([1, 5, 7], 0)
m4.adv_set_row([2, 6, 8], 1)
m4.print_out()
print("")

m5 = Matrix.multiplication_number(m4, 10)
m5.print_out()
print("")

m6 = Matrix.NewMatrix(1,3)
m6.adv_set_row([1,2,3],0)
m6.print_out()
print("")
m6.new_row()
m6.print_out()

while True:
    time.sleep(3)
    try:
        a = 10
    except KeyboardInterrupt:
        break