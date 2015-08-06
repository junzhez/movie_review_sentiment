import os

neg_text = []
pos_text = []

neg_filenames = open("neg/filename.txt", "r")
pos_filenames = open("pos/filename.txt", "r")

os.chdir("./neg")
for name in neg_filenames:
    cur_file = open(name[:-1], "r") # Drop newline character

    neg_text.append(cur_file.read())
    cur_file.close()

neg_filenames.close()

os.chdir("../pos")
for name in pos_filenames:
    cur_file = open(name[:-1], "r") # Drop newline character

    pos_text.append(cur_file.read())
    cur_file.close()

pos_filenames.close()

os.chdir("..")
