"""
Name: Caleb Quattlebaum
lab8.py
"""

from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'wt')
    i = 1
    for line in infile:
       words = line.split()
       for word in words:
           outfile.write(str(i) + " " + word + "\n")
       i = i + 1
    infile.close()
    outfile.close()

def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'wt')
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage = wage + 1.65
        wage = wage * int(parts[3])
        outfile.write(parts[0] + " " + parts[1] + " " + str(wage) + "\n")
    infile.close()
    outfile.close()

def calc_check_sum(isbn):  #pass condition as str
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc = acc + int(isbn[i]) * pos
    print(acc)

def send_message(file, friend):
    infile = open(file, 'r')
    outfile = open(friend + ".txt", "wt")
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()

def send_safe_mesage(file, friend, key):
    infile = open(file, 'r')
    outfile = open(friend + ".txt", "wt")
    for line in infile:
        outfile.write(encode(line, key))
    infile.close()
    outfile.close()

def send_safest_message(file, friend, pad):
    padfile = open(pad, "r")
    key = padfile.read()
    infile = open(file, 'r')
    outfile = open(friend + ".txt", "wt")
    for line in infile:
        outfile.write(encode_better(line, key))
    infile.close()
    outfile.close()

def main():
    number_words('Walrus.txt', 'Walrus_out.txt')
    hourly_wages('hourly_wages.txt', 'hourly_wages_out.txt')
    calc_check_sum('0072946520')
    send_message("message.txt", "Bob")
    send_safe_mesage("secret_message.txt", "Jack", 3)
    send_safest_message("safest_message.txt", "Jill", "pad.txt")


main()
