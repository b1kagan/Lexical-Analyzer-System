
symbol_table = {
    "if": "IF_TOKEN",
    "while": "WHILE_TOKEN",
    "for": "FOR_TOKEN"
}


def is_integer(token):
    try:
        int(token)
        return True
    except:
        return False


def is_float(token):
    try:
        float(token)
        return '.' in token
    except:
        return False


def is_identifier(token):
    if token[0].isalpha(): 
        for ch in token:
            if not (ch.isalnum() or ch == '_'):
                return False
        return True
    return False


def is_relop(token):
    relops = ["<", "<=", ">", ">=", "=="]
    return token in relops


def lex(tokens, index):
    if index >= len(tokens):
        return None, None, index

    token = tokens[index]

    
    if token in symbol_table:
        return symbol_table[token], token, index + 1

    
    elif is_integer(token):
        return "INTEGER", token, index + 1

    
    elif is_float(token):
        return "FLOAT", token, index + 1

    
    elif is_relop(token):
        return "RELOP", token, index + 1

    
    elif is_identifier(token):
        if token not in symbol_table:
            symbol_table[token] = "ID"

        return "ID", token, index + 1

    else:
        return "ERROR", token, index + 1


def main():
    filename = input("Enter a file name: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            tokens = content.split() 
    except:
        print("File not found!")
        return

    index = 0

    while True:
        print("\n****MENU****")
        print("1- Call lex()")
        print("2- Show symbol table")
        print("3- Exit")

        choice = input("Choose option: ")

        if choice == "1":
            token_type, lexeme, index = lex(tokens, index)

            if token_type is None:
                print("End of file reached.")
            else:
                print("Token:", token_type)
                print("Lexeme:", lexeme)

        elif choice == "2":
            print("\nSYMBOL TABLE:")
            for lexeme in symbol_table:
                print(f"{lexeme} --> {symbol_table[lexeme]}")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")
main()       
