def brainfuck_interpreter(code, input_data=""):
    tape = [0] * 30000  # Mémoire (tableau de 30 000 cases)
    pointer = 0  # Pointeur mémoire
    code_pointer = 0  # Pointeur du code
    loop_stack = []  # Pile pour les boucles
    input_pointer = 0  # Pointeur pour l'entrée utilisateur
    output = ""

    while code_pointer < len(code):
        command = code[code_pointer]

        if command == '>':
            pointer = (pointer + 1) % len(tape)
        elif command == '<':
            pointer = (pointer - 1) % len(tape)
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == '-':
            tape[pointer] = (tape[pointer] - 1) % 256
        elif command == '.':
            output += chr(tape[pointer])
        elif command == ',':
            if input_pointer < len(input_data):
                tape[pointer] = ord(input_data[input_pointer])
                input_pointer += 1
            else:
                tape[pointer] = 0  # Si plus d'entrée, on met 0
        elif command == '[':
            if tape[pointer] == 0:
                # Aller à la fin de la boucle
                open_brackets = 1
                while open_brackets:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_brackets += 1
                    elif code[code_pointer] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_pointer)
        elif command == ']':
            if tape[pointer] != 0:
                code_pointer = loop_stack[-1] - 1
            else:
                loop_stack.pop()

        code_pointer += 1

    return output


# --- Exemple d'utilisation ---
bf_code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
print(brainfuck_interpreter(bf_code))  # Affichera "Hello World"

