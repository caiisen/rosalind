with open('rosalind_rna.txt', 'r') as file_in:
    input = file_in.read().strip()
#input = 'GATGGAACTTGACTACGTAAATT'
output = ''
for letter in input:
    if letter == 'T':
        output += 'U'
    else:
        output += letter
print(output)