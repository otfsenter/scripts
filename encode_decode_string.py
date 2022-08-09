import base64

# if you need encode, fill this two parameters
STRING = ""
KEYWORD = ""

# if you need decode, fill this one parameter
ENCODED_STR = ""

# can not empty
STEP = 2


def encode(string, step, keyword, len_keyword):
    new_str_list = []
    for i in range(0, len(string) + 1, step):
        index_keyword = i % len_keyword
        append_str = keyword[index_keyword]

        cut_str = string[i : i + step]
        if cut_str:
            new_str_list.append([cut_str, append_str])

    new_str = "".join(["".join(i) for i in new_str_list])
    new_str = base64.b64encode(new_str.encode()).decode()
    return new_str


def decode(string, step):
    string = base64.b64decode(string.encode()).decode()
    new_str_list = []
    for i in range(0, len(string) + 1, step):
        cut_str = string[i : i + step][:-1]
        new_str_list.append(cut_str)
    new_str = "".join(new_str_list)
    return new_str


def main():
    string = STRING
    step = STEP
    keyword = KEYWORD
    len_keyword = len(KEYWORD)
    encoded_str = ENCODED_STR

    # encoding string
    if not encoded_str:
        new_str = encode(string, step, keyword, len_keyword)
        decoded_str = decode(new_str, step + 1)
        print(new_str)
        print(decoded_str)
        print(string == decoded_str)
    # decoding str
    else:
        decoded_str = decode(encoded_str, step + 1)
        print(decoded_str)


if __name__ == "__main__":
    main()
