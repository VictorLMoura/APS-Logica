import sys
from Parser import Parser

def main():
    arguments = sys.argv

    f = open(arguments[1], "r")
    # f = open("teste5", "r")

    Expression = ""
    lines = f.readlines()
    for i in range(len(lines)):
        try:
            Expression += lines[i].strip()
        except Exception as e:
            print(e)
    Parser.run(Expression)

main()