dict_json = ({'MINID', 1981, 1999, 'LIMBO'},
{'MINID', 1981, 1999, 'LEX'},
{'MINID', 1981, 2013},
{'MINID', 1982},
{'MINID', 1998},
{'HTML', 1999},
{'HTML', 2013, 1981, 2009},
{'HTML', 2013, 1981, 1979},
{'HTML', 2013, 1981, 1991},
{'HTML', 2013, 1982},
{'HTML', 2013, 1998},
{'YANG'})

def main(path):
    s1 = set(path)
    k = 0
    for i in range(len(dict_json)):
        if not (len(dict_json[i] - s1)):
            k = i
            break
    return k


if __name__ == "__main__":
    print(main([1998, 2013, 1979, 'LIMBO', 'HTML']),
          main([1981, 2013, 1979, 'LIMBO', 'HTML']),
          main([1998, 2013, 1979, 'LIMBO', 'YANG']),
          main([1981, 1999, 1991, 'LIMBO', 'HTML']),
          main([1982, 2013, 2009, 'LIMBO', 'MINID']))