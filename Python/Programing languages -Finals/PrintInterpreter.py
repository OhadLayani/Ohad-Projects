import re

# Define token patterns
token_patterns = [
    (r'Vari', 'VARI'),
    (r'[0-9]+', 'INTEGER'),
    (r'true|false', 'BOOLEAN'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
    (r'\(', 'LEFTPAREN'),
    (r'\)', 'RIGHTPAREN'),
    (r'=', 'EQUALS'),
    (r'if', 'IF'),
    (r'else', 'ELSE'),
    (r'"[^"]*"', 'STRING_LITERAL'),
    (r'while', 'WHILE'),
    (r'for', 'FOR'),
    (r'\{', 'LEFTBRACE'),
    (r'\}', 'RIGHTBRACE'),
    (r'>', 'GREATER_THAN'),
    (r'<', 'LESS_THAN'),
    (r'==', 'EQUALS_EQUALS'),
    (r';', 'SEMICOLON'),
    (r'print', 'PRINT'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'VARIABLE_NAME')
]

class SimpleInterpreter:
    def __init__(self):
        self.variables = {}

    def tokenize(self, code):
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

    def interpret(self, code):
        tokens = self.tokenize(code)
        i = 0
        while i < len(tokens):
            token, token_type = tokens[i]
            if token_type == 'VARI':
                variable_name = tokens[i + 1][0]
                if tokens[i + 2][0] != '=':
                    raise SyntaxError("Invalid variable assignment")
                value_token, value_type = tokens[i + 3]
                if value_type == 'VARIABLE_NAME':
                    value = self.variables.get(value_token)
                elif value_type == 'INTEGER':
                    value = int(value_token)
                elif value_type == 'BOOLEAN':
                    value = value_token == 'true'
                elif value_type == 'STRING_LITERAL':
                    value = value_token.strip('"')
                self.variables[variable_name] = value
                i += 4
            elif token_type == 'IF':
                condition = tokens[i + 2][0]
                if tokens[i + 1][1] != 'CONDITION' or tokens[i + 3][1] != 'CONDITION':
                    raise SyntaxError("Invalid if statement")
                condition = self.eval_condition(condition)
                if condition:
                    j = i + 5
                    while tokens[j][1] != 'RIGHTBRACE':
                        self.handle_token(tokens[j])
                        j += 1
                else:
                    j = i + 5
                    while tokens[j][1] != 'ELSE':
                        j += 1
                    j += 2
                    while tokens[j][1] != 'RIGHTBRACE':
                        self.handle_token(tokens[j])
                        j += 1
                i = j + 1
            elif token_type == 'PRINT':
                self.handle_token(tokens[i + 1])  # Pass the correct token to handle_token
                i += 2  # Move to the next token after the one passed to handle_token
            elif token_type == 'SEMICOLON':
                i += 1  # Ignore SEMICOLON tokens
            else:
                raise SyntaxError(f"Unexpected token: {token}")
    def eval_condition(self, condition):
        # Dummy implementation for demonstration
        return True

    def handle_token(self, token):
        value, token_type = token
        if token_type == 'VARIABLE_NAME':
            print(self.variables.get(value, "Variable not found"))  # Print the value or a message if variable not found
        elif token_type == 'INTEGER':
            print(int(value))
        elif token_type == 'BOOLEAN':
            print(value == 'true')
        elif token_type == 'STRING_LITERAL':
            print(value.strip('"'))
        else:
            raise SyntaxError(f"Unhandled token type: {token_type}")

# Test code with different print statements
test_code = """
Vari x = 10;
Vari y = "hello";
Vari z = true;
print x;
print "This is a string literal";
print y;
print z;
"""

# Create an instance of the interpreter and interpret the test code
interpreter = SimpleInterpreter()
interpreter.interpret(test_code)