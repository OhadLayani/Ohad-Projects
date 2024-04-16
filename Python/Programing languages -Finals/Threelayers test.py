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
    (r'==', 'EQUALS_EQUALS'),
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
    (r';', 'SEMICOLON'),
    (r'print', 'PRINT'),
    (r'@', 'NOTE'),
    (r'to', 'TO'),

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
        ElseActive=True

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
                if tokens[i + 3][1] == 'BOOLEAN':
                    value = self.handle_token(tokens[i + 3])

                # Assign the value to the variable
                self.variables[variable_name] = value

                # Move to the next statement
                i = end_index + 1
                num_variables += 1
            elif token_type == 'IF':
                ifstart=True
                # Find the condition
                condition_tokens = []
                i += 1  # Move to the next token after 'IF'
                while tokens[i][1] != 'LEFTPAREN':
                    i += 1
                i += 1  # Move past the LEFTPAREN token
                while tokens[i][1] != 'RIGHTPAREN':
                    condition_tokens.append(tokens[i])
                    i += 1
                condition = self.eval_condition(condition_tokens)

                # If the next token is not '{', proceed to the next token
                #print(tokens[i + 1][1])
                if tokens[i + 1][1] != 'LEFTBRACE':
                    i += 1

                # Find the body of the 'if' statement
                body_tokens = []
                brace_stack = []
                i += 1  # Move past the LEFTBRACE token
                while i < len(tokens):
                    if tokens[i][1] == 'LEFTBRACE':
                        brace_stack.append(tokens[i][1])
                    elif tokens[i][1] == 'RIGHTBRACE':
                        if len(brace_stack) == 1:
                            break  # Exit the loop when the outermost braces are closed
                        brace_stack.pop()
                    if not brace_stack:  # If brace_stack is empty, all braces are closed
                        break
                    body_tokens.append(tokens[i])
                    i += 1

                # Execute the 'if' statement if the condition is true
                if condition:
                    ElseActive=False
                    self.interpret(' '.join([t[0] for t in body_tokens]))



            elif token_type == 'ELSE':
                # ELSE statement logic
                # Find the body of the 'else' statement

                else_body_tokens = []
                brace_count = 1
                i += 1  # Move past the 'ELSE' token
                while brace_count != 0:
                    if tokens[i][1] == 'LEFTBRACE':
                        brace_count += 1
                    elif tokens[i][1] == 'RIGHTBRACE':
                        brace_count -= 2
                    if brace_count != 0 and tokens[i][1] != 'LEFTBRACE':
                        else_body_tokens.append(tokens[i])
                    i += 1

                # Execute the 'else' statement body
                if ElseActive==True:
                    print("Executing ELSE body")
                    self.interpret(' '.join([t[0] for t in else_body_tokens]))


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
                # WHILE statement logic
                # Find the condition for the while loop
                condition_tokens = []
                i += 1  # Move to the next token after 'WHILE'
                while tokens[i][1] != 'LEFTPAREN':
                    i += 1
                i += 1  # Move past the LEFTPAREN token
                while tokens[i][1] != 'RIGHTPAREN':
                    condition_tokens.append(tokens[i])
                    i += 1

                # Evaluate the condition
                    # Find the body of the 'while' loop
                while_body_tokens = []
                brace_stack = []
                i += 1  # Move past the LEFTBRACE token
                while i < len(tokens):
                    if tokens[i][1] == 'LEFTBRACE':
                        brace_stack.append(tokens[i][1])
                    elif tokens[i][1] == 'RIGHTBRACE':
                        if len(brace_stack) == 1:
                            break  # Exit the loop when the outermost braces are closed
                        brace_stack.pop()
                    if not brace_stack:  # If brace_stack is empty, all braces are closed
                        break
                    while_body_tokens.append(tokens[i])
                    i += 1
                while self.eval_condition(condition_tokens):
                # Execute the body of the 'while' loop
                        self.interpret(' '.join([t[0] for t in while_body_tokens]))
            elif token_type == 'PRINT':
                print(self.handle_token(tokens[i + 1]))  # Print the value of the token after 'PRINT'

                i += 2  # Move to the next token after the one passed to handle_token
            elif token_type == 'SEMICOLON':
                i += 1  # Ignore SEMICOLON tokens

            elif token_type=='RIGHTBRACE':
                i+=1

            elif token_type=='LEFTBRACE':
                i+=1

            elif token_type=='NOTE':
                i+=1

            else:
                raise SyntaxError(f"Unexpected token: {token}")

            num_lines += 1

    def evaluate_expression(self, expression_tokens):
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

    def eval_condition(self, condition_tokens):
        # If the condition tokens represent a boolean value
        if len(condition_tokens) == 1 and condition_tokens[0][1] == 'BOOLEAN':
            if condition_tokens[0][0].lower() == 'true':
                return True
            elif condition_tokens[0][0].lower() == 'false':
                return False
        elif len(condition_tokens) == 1 and condition_tokens[0][1] == 'VARIABLE_NAME':
                variable_name = condition_tokens[0][0]
                variable_value = self.variables.get(variable_name)
                if(variable_value==True):
                    return True
                else:
                    return False

        # If the condition tokens represent a comparison
        elif len(condition_tokens) == 3:
            left_operand = self.handle_token(condition_tokens[0])
            operator = condition_tokens[1][0]
            right_operand = self.handle_token(condition_tokens[2])


            # Perform the comparison based on the operator
            if operator == '==':
                return left_operand == right_operand
            elif operator == '>':
                return left_operand > right_operand
            elif operator == '<':
                return left_operand < right_operand
            else:
                raise SyntaxError("Invalid comparison operator")

        # Invalid condition format
        else:
            raise SyntaxError("Invalid condition format")

    def handle_token(self, token):
        value, token_type = token
        if token_type == 'VARIABLE_NAME':
            # If the token is a variable name, look up its value in the dictionary
            variable_value = self.variables.get(value,"Variable not found")  # Return "Variable not found" if variable not found
            # Debugging statement
            return variable_value
        elif token_type == 'INTEGER':
            # If the token is an integer, return its integer value
            return int(value)
        elif token_type == 'BOOLEAN':

            if token[0].lower() == 'true':
                value = True
                return value
            elif token[0].lower() == 'false':
                value = False
                return value

        elif token_type == 'STRING_LITERAL':
            # If the token is a string literal, strip the double quotes and return the string
            return value.strip('"')
        else:
            raise SyntaxError(f"Unhandled token type: {token_type}")
# Test code with different print statements
code = """
Vari x=5;
Vari d=10;
Vari f=true;

if(x>2){
print x;
if(f){
print f;
if(d>7){
print d;
}
}

Vari y=1;
while(y<5){
if(y==2){
Vari x=x+2;
}
if(y==3){
Vari Mult=x*y;
}
if(y==4){
print "Getting closer.";
}
Vari y=y+1;
}

print x;
print Mult;
Vari div=Mult/x;
Vari sub=Mult-div;

print div;
print sub;
for Vari i =0 to 6{
Vari y=y+2;
print y;

}

"""

# Create an instance of the interpreter and interpret the test code
interpreter = SimpleInterpreter()
tokens = interpreter.tokenize(code)
interpreter.interpret(code)