import re

class Lexer:
    def __init__(self, input_code):
        self.input_code = input_code
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        token_specs = [
            ("NUMBER", r'\d+'),
            ("PLUS", r'\+'),
            ("MINUS", r'-'),
            ("MUL", r'\*'),
            ("DIV", r'/'),
            ("ASSIGN", r'='),
            ("SEMI", r';'),
            ("LPAREN", r'\('),
            ("RPAREN", r'\)'),
            ("WHITESPACE", r'\s+'),
            ("LET", r'let'),
            ("PRINT", r'print'),
            ("ID", r'[a-zA-Z_][a-zA-Z0-9_]*')
        ]
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
        matches = re.finditer(token_regex, self.input_code)
        for match in matches:
            kind = match.lastgroup
            value = match.group(kind)
            if kind != "WHITESPACE":
                value = int(value) if kind == "NUMBER" else value
                self.tokens.append((kind, value))
        return self.tokens
