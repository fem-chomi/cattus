import re
from typing import List


class NameConverter():
    @staticmethod
    def ToUpperCamelCase(name: str) -> str:
        builder: List[str] = []
        for token in re.split('[-_]', name):
            builder.append(token[0].upper() + token[1:].lower())
        return ''.join(builder)

    @staticmethod
    def ToLowerCamelCase(name: str) -> str:
        first: bool = True
        builder: List[str] = []
        for token in re.split('[-_]', name):
            if first:
                builder.append(token.lower())
                first = False
            else:
                builder.append(token[0].upper() + token[1:].lower())
        return ''.join(builder)

    @staticmethod
    def ToUpperSnakeCase(name: str) -> str:
        first: bool = True
        builder: List[str] = []
        for token in re.split('[-_]', name):
            if first:
                first = False
            else:
                builder.append('_')
            builder.append(token.upper())
        return ''.join(builder)

    @staticmethod
    def ToLowerSnakeCase(name: str) -> str:
        first: bool = True
        builder: List[str] = []
        for token in re.split('[-_]', name):
            if first:
                first = False
            else:
                builder.append('_')
            builder.append(token.lower())
        return ''.join(builder)

    @staticmethod
    def ToUpperKebabCase(name: str) -> str:
        first: bool = True
        builder: List[str] = []
        for token in re.split('[-_]', name):
            if first:
                first = False
            else:
                builder.append('-')
            builder.append(token.upper())
        return ''.join(builder)

    @staticmethod
    def ToLowerKebabCase(name: str) -> str:
        first: bool = True
        builder: List[str] = []
        for token in re.split('[-_]', name):
            if first:
                first = False
            else:
                builder.append('-')
            builder.append(token.lower())
        return ''.join(builder)
