with open('rosalind_prot.txt', 'r') as input_file:
    raw_seq = input_file.read().strip()
    rnaseq = []
    i = 1
    while i <= len(raw_seq) / 3:
        rnaseq.append(raw_seq[ (i-1)*3 : (i-1)*3+3 ])
        i = i + 1

codon_table = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V', 'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V', 'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V', 'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A', 'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A', 'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A', 'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A', 'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D', 'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D', 'UAA':'', 'CAA':'Q', 'AAA':'K', 'GAA':'E', 'UAG':'', 'CAG':'Q', 'AAG':'K', 'GAG':'E', 'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G', 'UGA':'', 'CGA':'R', 'AGA':'R', 'GGA':'G', 'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}

with open('result', 'w') as output_file:
    for codon in rnaseq:
        output_file.write(codon_table[codon])