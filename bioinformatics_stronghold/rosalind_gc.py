with open('rosalind_gc.txt', 'r') as input_file:
    seq = {}
    for line in input_file:
        if '>' in line:
            label = line.strip().strip('>')
            seq[label] = []
        else:
            seq[label].append(line.strip())
    for key, value in seq.items():
        sequence = ''.join(value)
        gc_count = 0
        gc_percent = 0
        for character in sequence:
            if character == 'C' or character == 'G':
                gc_count += 1
        gc_percent = gc_count / len(sequence) * 100
        seq[key] = gc_percent

with open('rosalind_gc.out', 'w') as out_file:
    max_value = 0
    for key, value in seq.items():
        if value > max_value:
            max_key = key
            max_value = value
    out_file.write(max_key + '\n')
    out_file.write(str(max_value) + '\n')