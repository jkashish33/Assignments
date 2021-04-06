def error_eval():
    try:
        eval('a===b')
    except SyntaxError:
        print("There is syntax error")
error_eval()