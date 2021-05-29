with open('rosalind_dna.txt', 'r') as file_in:
    input = file_in.read().strip()
#input = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
atcg = {'A':0, 'T':0, 'C':0, 'G':0}
for letter in input:
    if letter == 'A':
        atcg['A'] += 1
    elif letter == 'T':
        atcg['T'] += 1
    elif letter == 'C':
        atcg['C'] += 1
    elif letter == 'G':
        atcg['G'] += 1
print(atcg['A'], atcg['C'], atcg['G'], atcg['T'])