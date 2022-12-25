def proccess(input_str: str):
    counter = 0
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]:
            counter += 1

    return counter


if __name__ == "__main__":
    input_str = input()
    print(proccess(input_str))
