
f = open("INPUT.txt", "r")
data = f.readlines()
f_out = open("OUTPUT.txt", "w")

# input
Rain_number = int(data[1])
UH_number = int(data[3])
QN = int(data[5])
DRH_number = UH_number + Rain_number - 1

f.close()
# writing to file
f_out.write("Generating Ordinates of DRH" + "\n")
f_out.write("---------------------------" + "\n")
f_out.write("Number of non-zero UH ordinates = " + str(UH_number) + "\n")
f_out.write("Number of non-zero DRH ordinates = " + str(DRH_number) + "\n")
f_out.write("Number of Rainfall pulse = " + str(Rain_number) + "\n\n")


# function to find DRH
def drh_rows(k1, k2):
    global r_first_index
    for s in range(k1, k2, 1):
        if s > UH_number:
            u_first_index = UH_number
            r_first_index = (s + 1) - u_first_index
        elif s <= UH_number:
            r_first_index = 1
            # u_first_index = s

        f_out.write("Q" + str(s) + " = ")
        check = 0
        for i in range(r_first_index, Rain_number + 1, 1):
            if 0 < (s + 1 - i) <= UH_number:
                check = check + 1
                if check > 1:
                    f_out.write(" + ")

                f_out.write("R" + str(i) + "U" + str(s + 1 - i))

        f_out.write("\n")


# calling function to find specific rows/ordinates of DRH i.e. QN
if 0 < QN <= DRH_number:
    f_out.write("The DRH Ordinate for row " + str(QN) + "\n")
    f_out.write("------------------------------" + "\n")
    drh_rows(QN, QN + 1)
else:
    f_out.write("The DRH Ordinate for row " + str(QN) + "\n")
    f_out.write("------------------------------" + "\n")
    f_out.write("Can't find! Enter value between " + str(0) + " and " + str(DRH_number) + "\n")

# calling function to find all rows/ordinates of DRH
f_out.write("\n")
f_out.write("All DRH Ordinates are " + "\n")
f_out.write("---------------------------" + "\n")
drh_rows(1, DRH_number + 1)

f_out.close()
