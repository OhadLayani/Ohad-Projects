

import re

# Token types
VARI = 'VARI'
INTEGER = 'INTEGER'
BOOLEAN = 'BOOLEAN'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
LBRACE = 'LBRACE'
RBRACE = 'RBRACE'
SEMICOLON = 'SEMICOLON'
EQUALS = 'EQUALS'
IF = 'IF'
ELSE = 'ELSE'
WHILE = 'WHILE'
FOR = 'FOR'
GREATER_THAN = 'GREATER_THAN'
LESS_THAN = 'LESS_THAN'
EQUALS_EQUALS = 'EQUALS_EQUALS'
VARIABLE_NAME = 'VARIABLE_NAME'
STRING_LITERAL = 'STRING_LITERAL'
PRINT = 'PRINT'


# Token patterns
token_patterns = [
    (r'Vari', VARI),
    (r'[0-9]+', INTEGER),
    (r'true|false', BOOLEAN),
    (r'\+', PLUS),
    (r'-', MINUS),
    (r'\*', MULTIPLY),
    (r'/', DIVIDE),
    (r'\(', LPAREN),
    (r'\)', RPAREN),
    (r'\{', LBRACE),  # Updated pattern for opening brace
    (r'\}', RBRACE),  # Updated pattern for closing brace
    (r';', SEMICOLON),
    (r'=', EQUALS),
    (r'if', IF),
    (r'else', ELSE),
    (r'"[^"]*"', STRING_LITERAL),
    (r'while', WHILE),
    (r'for', FOR),
    (r'>', GREATER_THAN),
    (r'<', LESS_THAN),
    (r'==', EQUALS_EQUALS),
    (r'print', PRINT),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', VARIABLE_NAME),
]

# Tokenize function
def tokenize(code):
    tokens = []
    code = code.strip()
    while code:
        matched = False
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                code = code[match.end():].strip()
                matched = True
                break
        if not matched:
            raise SyntaxError(f"Invalid token: {code}")
    return tokens

# Test the tokenizer
code = """
Vari x = 102;
Vari y = 5;
Vari z = x + y ;
print z;
"""
tokens = tokenize(code)
for token in tokens:
    print(token)