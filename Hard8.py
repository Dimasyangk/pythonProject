import re


def main(x):
    z = {}
    x = x.replace(" ", "")
    x = x.replace ("\n", "")
    names = re.findall("=>.*?;", x)
    data = re.findall("loc.*?=", x)
    for i in range(len(names)):
        name = names[i].replace("=>", "").replace(";", "")
        z[name] = data[i].replace("loc", "").replace("=", "")
    return z


if __name__ == "__main__":
    print(main("[ << loc laleti_821==> uses_232; >>; <<loc qucere_427==> oranor;>>; \
               << loc aroron_734==> qubi_471; >>;<< loc rivein ==>beceza_6; >>; ]"), "\n\n",
          main("[ << loc cequat ==> quveor_680; >>;<< loc reso_84 ==> vearxe; >>; \
               <<loc diatxe ==>died;>>;]"))