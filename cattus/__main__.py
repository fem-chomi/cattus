import sys
from Util.CommandParser import CommandParser
from Util.CommandParameter import CommandParameter
from Generator.GenerateCode import GenerateCode


def main(command: CommandParameter) -> None:
    genCode = GenerateCode()
    genCode.Generate()

command = CommandParser(1, 2, sys.argv[1:]).Parse()
main(command)
sys.exit(0)
