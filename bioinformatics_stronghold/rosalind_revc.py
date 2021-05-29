with open('rosalind_revc.txt', 'r') as file_in:
    input = file_in.read().strip()
#input = 'AAAACCCGGT'
output = []
for letter in input:
    if letter == 'A':
        output.insert(0, 'T')
    elif letter == 'T':
        output.insert(0, 'A')
    elif letter == 'C':
        output.insert(0, 'G')
    elif letter == 'G':
        output.insert(0, 'C')
outstr = ''.join(output)
print(outstr)