import re

def extract_and_calculate(file_path):
    with open(file_path, 'r') as file:
        contenuto = file.read()
      
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    abilita_mul = True
    somma = 0
    token_pattern = f"{do_pattern}|{dont_pattern}|{mul_pattern}"
    tokens = re.finditer(token_pattern, contenuto)
    for token in tokens:
        if token.group(0) == "do()":
            abilita_mul = True
        elif token.group(0) == "don't()":
            abilita_mul = False
        elif token.group(1) and abilita_mul:
            a, b = map(int, (token.group(1), token.group(2)))
            somma += a * b
    return somma

file_path = "./input.txt"
result = extract_and_calculate(file_path)
print(f"Sum of all valid multiplications: {result}")
