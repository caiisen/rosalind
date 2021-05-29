with open('rosalind_ini5.txt','r') as file_in:
    file_line = []
    for line in file_in:
        file_line.append(line)
    file_line = file_line[1::2]
with open('rosalind_ini5.out.txt','w') as file_out:
    for line in file_line:
        file_out.write(line)

    #file_line = file_object.readline()
    #print(file_line)