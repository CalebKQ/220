"""
Name: Caleb Quattlebaum
weighted_average.py

Purpose: calculate the weighted average for students in a class and the overall average then write it to
         a new file

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# create weighted_average() function that takes in-file name and out-file name as parameters
def weighted_average(in_file_name, out_file_name):
    # open and read grades.txt to get grade info for students
    in_file = open(in_file_name, 'r')
    # create variable to open and write info to out-file avg.txt
    out_file = open(out_file_name, 'wt')
    # create for loop to go line by line in grades.txt
    total_acc = 0
    num_i = 0
    for line in in_file:
        # separate student names from numbers by splitting at ":"
        name_num = line.split(': ')
        names = name_num[0]
        nums_together = name_num[1]
        nums = nums_together.split()
        # store every other number starting at [0] for weights
        weights = nums[0::2]
        # store every other number starting at [1] for grades
        grades = nums[1::2]
        # if sum of weights are > 100 write error message to out-file
        accu = 0
        for iteration in weights:
            accu = accu + int(iteration)
        sum_weights = accu
        if sum_weights > 100:
            out_file.write(names + "'s average: Error: The weights are more than 100. \n")
        # elif weights are < 100 write error message to out-file
        elif sum_weights < 100:
            out_file.write(names + "'s average: Error: The weights are less than 100. \n")
        # else run the weighted average formula
        else:
            acc = 0
            grades_acc = 0
            for weight in weights:
                product = int(weight) * int(grades[grades_acc])
                acc = acc + product
                grades_acc = grades_acc + 1
            avg = acc / 100
            # write names and averages to out-file
            out_file.write(names + "'s average: " + str(round(avg, 1)) + "\n")
        total_acc = total_acc + avg
        num_i = num_i + 1
    total_avg = total_acc / num_i
    out_file.write("Class average: " + str(round(total_avg, 1)))
    # close grades.txt and avg.txt
    in_file.close()
    out_file.close()

# create main() function to run weighted_average('grades.txt', 'avg.txt'
def main():
    weighted_average('grades.txt', 'avg.txt')

if __name__ == "__main__":
    main()
