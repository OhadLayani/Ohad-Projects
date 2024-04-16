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
    (r'to', 'TO'),
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
        num_lines = 0
        num_variables = 0
        i = 0

        while i < len(tokens):
            # Check if the maximum number of lines has been reached
            if num_lines >= 100:
                print("Maximum number of lines exceeded.")
                break

            token, token_type = tokens[i]
            if token_type == 'VARI':
                # Check if the maximum number of variables has been reached
                if num_variables >= 20:
                    print("Maximum number of variables exceeded.")
                    break

                variable_name = tokens[i + 1][0]
                if tokens[i + 2][0] != '=':
                    raise SyntaxError("Invalid variable assignment")

                # Find the end index of the assignment statement
                end_index = i + 3
                while end_index < len(tokens) and tokens[end_index][1] != 'SEMICOLON':
                    end_index += 1

                # Evaluate arithmetic expressions or string literals within the assignment statement
                if tokens[i + 3][1] == 'STRING_LITERAL':
                    value = self.handle_token(tokens[i + 3])
                else:
                    value = self.evaluate_expression(tokens[i + 3:end_index])

                # Assign the value to the variable
                self.variables[variable_name] = value

                # Move to the next statement
                i = end_index + 1
                num_variables += 1
            elif token_type == 'IF':
                # Handle if statement
                i += 1
            elif token_type == 'FOR':
                # Handle FOR statement
                # Get the variable name
                variable_name = tokens[i + 1][0]
                # Get the start value
                start_value = self.evaluate_expression(tokens[i + 3:i + 5])
                # Get the end value
                end_value = self.evaluate_expression(tokens[i + 5:i + 7])
                # Check for the body of the loop
                body_start_index = i + 8
                end_index = body_start_index
                while end_index < len(tokens) and tokens[end_index][1] != 'RIGHTBRACE':
                    end_index += 1
                body_tokens = tokens[body_start_index:end_index]

                # Execute the loop
                for value in range(start_value, end_value):
                    # Assign the current value to the loop variable
                    self.variables[variable_name] = value
                    # Execute the body of the loop
                    self.interpret(' '.join([t[0] for t in body_tokens]))

                # Move the index to the end of the loop
                i = end_index + 1
            elif token_type == 'WHILE':
                # Handle FOR statement
                i += 1
            elif token_type == 'PRINT':
                print(self.handle_token(tokens[i + 1]))  # Print the value of the token after 'PRINT'
                i += 2  # Move to the next token after the one passed to handle_token
            elif token_type == 'SEMICOLON':
                i += 1  # Ignore SEMICOLON tokens
            else:
                raise SyntaxError(f"Unexpected token: {token}")

            num_lines += 1

    def evaluate_expression(self, expression_tokens):
        # Check if the expression is a for loop
        if len(expression_tokens) == 3 and expression_tokens[1][0] == 'to':
            # Extract start and end values from the expression tokens
            start_value = self.handle_token(expression_tokens[0])
            end_value = self.handle_token(expression_tokens[2])

            # Check if start and end values are integers
            if not isinstance(start_value, int) or not isinstance(end_value, int):
                raise ValueError("Invalid loop bounds")

            # Return the end value of the loop
            return end_value
        else:
            # Evaluate arithmetic expression
            value = None
            operator = None
            for token, token_type in expression_tokens:
                if token_type == 'INTEGER':
                    if value is None:
                        value = int(token)
                    else:
                        if operator == '+':
                            value += int(token)
                        elif operator == '-':
                            value -= int(token)
                        elif operator == '*':
                            value *= int(token)
                        elif operator == '/':
                            value /= int(token)
                elif token_type == 'BOOLEAN':
                    if token.lower() == 'true':
                        value = True
                    elif token.lower() == 'false':
                        value = False
                elif token_type == 'VARIABLE_NAME':
                    variable_value = self.variables.get(token)
                    if variable_value is None:
                        raise ValueError(f"Variable '{token}' has not been assigned a value")
                    if value is None:
                        value = variable_value
                    else:
                        if operator == '+':
                            value += variable_value
                        elif operator == '-':
                            value -= variable_value
                        elif operator == '*':
                            value *= variable_value
                        elif operator == '/':
                            if variable_value == 0:
                                raise ValueError("Division by zero")
                            value /= variable_value
                elif token_type in ['PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE']:
                    operator = token
            return value

    def eval_condition(self, condition):
        # Dummy implementation for demonstration
        return True

    def handle_token(self, token):
        value, token_type = token
        if token_type == 'VARIABLE_NAME':
            # If the token is a variable name, look up its value in the dictionary
            variable_value = self.variables.get(value,
                                                "Variable not found")  # Return "Variable not found" if variable not found
            # Debugging statement
            return variable_value
        elif token_type == 'INTEGER':
            # If the token is an integer, return its integer value
            return int(value)

        elif token_type == 'STRING_LITERAL':
            # If the token is a string literal, strip the double quotes and return the string
            return value.strip('"')
        else:
            raise SyntaxError(f"Unhandled token type: {token_type}")


# Test code with different print statements
code = """
Vari x = true;
Vari y = false;
Vari z = x == true;
print z;
print y;
    """

# Create an instance of the interpreter and interpret the test code
interpreter = SimpleInterpreter()
interpreter.interpret(code)
