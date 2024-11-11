# programming-cw
This report provides an overview of the class design, function usage, and iteration techniques employed in the development of the program.
Each one had to atleast had different tasks to do
Mutabarura Marvin dealt with obtaining the source code
Muwonge Johnson dealt with checking whether the sequence of tokens matched the grammatical rules of the language.
The rest we dealt them together such as execution ,error handling.

Functions were used extensively throughout the program to encapsulate specific operations and enable code reuse. 
The key areas where functions were employed included:
Lexical Analysis Functions:

next_token(): This function returned the next token in the input stream.
tokenize(): Tokenized the entire source code into a list of tokens, using a loop to repeatedly call next_token().
Parsing Functions:

parse_expression(): A recursive function that parsed arithmetic and logical expressions.
parse_statement(): Handled the parsing of different types of statements, such as assignment or print statements.
match_token(): A helper function used to validate and consume tokens, ensuring the correct syntax was followed.
Execution Functions:

evaluate_expression(): Evaluated mathematical expressions, calling specific functions for operations like addition or multiplication.
execute_statement(): Executed different kinds of statements such as variable assignments, function calls, or control flow structures (if-else, loops).
Error Handling Functions:

report_error(): A generic function for reporting syntax or runtime errors with the appropriate line number and description.
teration Techniques
Iteration techniques were central to the design of both the lexer and parser. Some of the key iteration techniques used were:

For Loops:

The Lexer class used a for loop to iterate through each character in the input stream, collecting sequences of characters to form tokens.
While Loops:

The Lexer also used while loops to continue processing the input until the end of the source code was reached. This loop was responsible for checking for different types of tokens (e.g., identifiers, operators).
The Parser used while loops to continue parsing as long as there were valid tokens to process.
Recursion:

The Parser relied heavily on recursion for parsing nested expressions. Recursive descent parsing allowed for handling nested expressions and operations with varying precedence levels. For example, parsing arithmetic expressions like a + b * c required recursion to handle the operator precedence.
Iteration in AST Traversal:

For evaluating and interpreting expressions, the program used depth-first traversal of the AST, iterating through the tree nodes recursively. The interpreter visited each node, evaluated the expression or statement, and returned the result.
Look-ahead Iteration:

The parser employed a look-ahead strategy, where the current token was inspected and compared with expected values before making decisions about which parsing rule to apply. This helped in ensuring that the parsing process could handle variations in grammar rules effectively.    
Conclusion
The programming language program utilized a robust object-oriented approach to organize the code into distinct classes with clear responsibilities. Function usage facilitated modularity and reusability, while iteration techniques such as loops and recursion ensured that the program could efficiently process and interpret source code.
