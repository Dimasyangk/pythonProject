import re


def main(x):
    z = {}
    x = x.replace(" ", "")
    x = x.replace("\n", "")
    names = re.findall(":.*?;", x)
    data = re.findall("#.*?=", x)
    for i in range(len(names)):
        name = names[i].replace(":", "").replace(";", "")
        z[name] = int(data[i].replace("#", "").replace("=", ""))
    return z

if __name__ == "__main__":
    print(main("((.do declare #-379 =: quarbi_915; .end, .do declare #9028=: \
               xegeso_950;.end, ))"), "\n\n",
          main("(( .do declare#-1606 =:reanar;.end, .do declare #3642=:ribe;.end, ))"))

