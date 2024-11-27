
# **Python Interpreter for a Simplistic Programming Language**

## **Table of Contents**
- [Project Overview](#project-overview)  
- [Project Structure](#project-structure)  
- [Setup Instructions](#setup-instructions)  
- [Features](#features)  
- [Contributing](#contributing)  
- [License](#license)  

---

## **Project Overview**
This project delivers a Python-based interpreter for a basic programming language. It is capable of:  
- **Tokenizing** the source code into meaningful symbols.  
- **Constructing** an Abstract Syntax Tree (AST) to represent program structure.  
- **Executing** the parsed instructions such as variable assignments, arithmetic operations, and print commands.  

The interpreter offers a practical insight into key interpreter concepts, including lexical analysis, parsing, and AST-driven execution.  

Developed as part of the **CS 609: Final Project Assignment** at Southeast Missouri State University, this project adheres to course requirements and provides a foundation for understanding interpreters.

---

## **Project Structure**
The project is modular and organized as follows:

| File/Folder         | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `lexer.py`          | Converts source code into tokens like keywords, variables, and operators.  |
| `parser.py`         | Builds an Abstract Syntax Tree (AST) from tokens.                          |
| `ast_nodes.py`      | Defines classes for AST nodes (`AssignNode`, `BinOpNode`, `PrintNode`).    |
| `interpreter.py`    | Executes commands such as variable assignments and arithmetic operations.  |
| `examples/`         | Contains sample programs and test cases to demonstrate functionality.      |

---

## **Setup Instructions**

### **Prerequisites**
- Python version **3.7 or higher** is required.

### **Steps to Run the Interpreter**
1. Clone this repository:
   ```bash
   git clone https://github.com/ApilParajuli/Interpreter_CS_Project.git
   cd interpreter
   ```

2. Create a program file in the appropriate format. For example:
   ```python
   let a = 15 - 3;
   let b = a / 2;
   let c = b + 7;
   print(a);
   print(b);
   print(c);
   ```
   Save the file as `program.txt`.

3. Execute the interpreter:
   ```bash
   python main.py program.txt
   ```

---

## **Features**
- Converts source code into tokens for processing.
- Constructs an AST to represent program logic hierarchically.
- Executes parsed code, including variable assignments, calculations, and print statements.
- Includes sample test cases for demonstration and debugging.

---

## **Contributing**
Contributions are welcome! To get started:  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add feature"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.  

Please ensure your code follows the project's style guidelines.

---

## **License**
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the license terms.

  
