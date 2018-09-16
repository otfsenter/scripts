"""
1- return dictionary which has all of index and string, length of lines, the indexes of starting with 'minor'
2- concatenate each line between the range number
"""

file_cacti = 'cacti.txt'
keyword = 'minor'


def origin():
    o = {}
    m = []
    with open(file_cacti, 'r', encoding='utf-8') as f:
        for i, d in enumerate(f):
            o.setdefault(i, d.strip())
            if d.lower().startswith(keyword):
                m.append(i)
    return o, len(o), m


def get_new_list():
    origin_dict, len_origin, minor_index_list = origin()

    new_list = []
    for index, minor_index in enumerate(minor_index_list):

        minor_next = index != len(minor_index_list) - 1 and minor_index_list[index + 1] or len_origin

        new_each_list = []
        for i in range(minor_index, minor_next):
            new_each_list.append(origin_dict.get(i, ''))
        new_list.append(' '.join(new_each_list))

    return new_list


def main():
    new = get_new_list()
    for i in new:
        print(i)


if __name__ == '__main__':
    main()
