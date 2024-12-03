import re

def extract_and_calculate(memory):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, memory)
    total = sum(int(x) * int(y) for x, y in matches)
    return total
def main():
    file_path = "input.txt"
    with open(file_path, "r") as file:
        memory = file.read()
    result = extract_and_calculate(memory)
    print(f"Sum of all valid multiplications: {result}")


if __name__ == "__main__":
    main()
