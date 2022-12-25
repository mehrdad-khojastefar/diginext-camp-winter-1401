def repeatString(input: str, count: int) -> str:
    """
    repeatString returnes the valid string based on the user inputs.
    since the count can be less than the length of the input we create a condition to check
    and proccess string accordingly.
    """
    if count <= len(input):
        return input[:count]
    else:
        list_input = list(input)
        result = input
        while len(result) < count:
            result += list_input[0]
            list_input.append(list_input[0])
            list_input.pop(0)

        return result


if __name__ == "__main__":
    # get the inputs from user
    input_str = input()
    input_count = int(input())
    a_count = repeatString(input_str, input_count).count("a")
    print(a_count)
