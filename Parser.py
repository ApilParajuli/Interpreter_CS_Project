from AST_node import AssignNode, BinOpNode, PrintNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = 0  # Tracks the current position in the token list

    def parse(self):
        """
        Parse individual statements, either assignment or print.
        Returns the root node of the parsed AST.
        """
        token_type, token_value = self.tokens[self.current_pos]
        if token_type == "LET":
            # Parse an assignment statement
            node = self.parse_assignment()
            self.consume("SEMI")  # Ensure the statement ends with a semicolon
            return node
        elif token_type == "PRINT":
            # Parse a print statement
            node = self.parse_print()
            self.consume("SEMI")  # Ensure the statement ends with a semicolon
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token_type}")

    def parse_assignment(self):
        """
        Parse an assignment statement in the form 'let <ID> = <expression>'.
        Returns an AssignNode with the variable name and the parsed expression.
        """
        self.consume("LET")  # Expect 'let' keyword
        var_name = self.consume("ID")[1]  # Extract variable name
        self.consume("ASSIGN")  # Expect '=' symbol
        expr = self.parse_expression()  # Parse the right-hand side expression
        return AssignNode(var_name=var_name, expr=expr)

    def parse_print(self):
        """
        Parse a print statement in the form 'print(<expression>)'.
        Returns a PrintNode containing the parsed expression.
        """
        self.consume("PRINT")  # Expect 'print' keyword
        self.consume("LPAREN")  # Expect '(' symbol
        expr = self.parse_expression()  # Parse the expression inside parentheses
        self.consume("RPAREN")  # Ensure the parentheses are properly closed
        return PrintNode(expr=expr)

    def parse_expression(self):
        """
        Parse an expression, which can include primary expressions
        (numbers, identifiers, or parentheses) and binary operations.
        Returns the root of the parsed expression subtree.
        """
        # Handle primary expressions
        if self.tokens[self.current_pos][0] == "LPAREN":
            self.consume("LPAREN")  # Expect '('
            expr = self.parse_expression()  # Parse the expression inside parentheses
            self.consume("RPAREN")  # Ensure the parentheses are properly closed
            return expr

        elif self.tokens[self.current_pos][0] in ("NUMBER", "ID"):
            # Consume a number or identifier
            left = self.consume(self.tokens[self.current_pos][0])
        else:
            raise SyntaxError(
                f"Expected a NUMBER, ID, or LPAREN, got {self.tokens[self.current_pos]}"
            )

        # Handle binary operations (e.g., +, -, *, /)
        while (self.current_pos < len(self.tokens) and 
               self.tokens[self.current_pos][0] in ("PLUS", "MINUS", "MUL", "DIV")):
            op = self.consume(self.tokens[self.current_pos][0])  # Consume the operator
            if self.tokens[self.current_pos][0] in ("NUMBER", "ID", "LPAREN"):
                right = self.parse_expression()  # Parse the right operand
                # Combine left, operator, and right into a BinOpNode
                left = BinOpNode(left=left[1], op=op[0], right=right)
            else:
                raise SyntaxError(
                    f"Expected a NUMBER, ID, or LPAREN after {op}, got {self.tokens[self.current_pos]}"
                )

        # Return the final expression node
        return left[1] if isinstance(left, tuple) else left

    def consume(self, expected_type):
        """
        Consume the current token if it matches the expected type.
        Raises a SyntaxError if the token does not match.
        """
        if self.current_pos < len(self.tokens) and self.tokens[self.current_pos][0] == expected_type:
            current_token = self.tokens[self.current_pos]
            self.current_pos += 1  # Advance to the next token
            return current_token
        raise SyntaxError(
            f"Expected {expected_type}, got {self.tokens[self.current_pos][0]} at position {self.current_pos}"
        )
