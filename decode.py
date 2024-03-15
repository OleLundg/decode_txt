def decode(message_file):
    with open(f"{message_file}", 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    decoded_words = []
    last_index = 0
    n = 1
    sorted_lines = sorted((line.split(maxsplit=1) for line in lines), key=lambda x: int(x[0]))
    for index, word in sorted_lines:
        index = int(index)
        if index == last_index + n:
            decoded_words.append(word)
            last_index = index
            n += 1
    return ' '.join(decoded_words)

def main():
    file_name = "195 land.txt" 
    decoded_msg = decode(file_name)
    print(decoded_msg)
    

if __name__ == "__main__":
    main()