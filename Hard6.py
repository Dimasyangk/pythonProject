dict_json = ({2002, 1965, 'DM', 'CSON'},
             {2002, 1965, 'DM', 'M4'},
             {2002, 1965, 'DM', 'CIRRU'},
             {2002, 1965, 'VCL', 'R'},
             {2002, 1965, 'VCL', 'PIKE'},
             {2002, 1965, 'VCL', 'MUPAD'},
             {2002, 1965, 'R', 'CSON'},
             {2002, 1965, 'R', 'M4'},
             {2002, 1965, 'R', 'CIRRU'},
             {2002, 2002},
             {2002, 1981},
             {2018})


def main(path):
    s1 = set(path)
    k = 0
    for i in range(len(dict_json)):
        if not (len(dict_json[i] - s1)):
            k = i
    return k


if __name__ == "__main__":
    print(main(['M4', 'VCL', 2002, 1965, 'PIKE']),
          main(['CIRRU', 'DM', 2002, 1981, 'MUPAD']),
          main(['M4', 'DM', 2002, 2002, 'MUPAD']),
          main(['M4', 'R', 2018, 1965, 'R']),
          main(['CSON', 'R', 2002, 1965, 'PIKE']))
