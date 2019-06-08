print("""\

------------------------------------------------------------------------------
  ____ ___  __    _____ _____ _____ _   _       _______ _    _ _____  ______
 |___ \\__ \\/_ |  / ____|_   _/ ____| \\ | |   /\\|__   __| |  | |  __ \\|  ____|
   __) | ) || | | (___   | || |  __|  \\| |  /  \\  | |  | |  | | |__) | |__
  |__ < / / | |  \\___ \\  | || | |_ | . ` | / /\\ \\ | |  | |  | |  _  /|  __|
  ___) / /_ | |  ____) |_| || |__| | |\\  |/ ____ \\| |  | |__| | | \\ \\| |____
 |____/____||_| |_____/|_____\\_____|_| \\_/_/    \\_\\_|   \\____/|_|  \\_\\______|
       _____ ______ _   _ ______ _____         _______ ____  _____
      / ____|  ____| \\ | |  ____|  __ \\     /\\|__   __/ __ \\|  __ \\
     | |  __| |__  |  \\| | |__  | |__) |   /  \\  | | | |  | | |__) |
     | | |_ |  __| | . ` |  __| |  _  /   / /\\ \\ | | | |  | |  _  /
     | |__| | |____| |\\  | |____| | \\ \\  / ____ \\| | | |__| | | \\ \\
      \\_____|______|_| \\_|______|_|  \\_\\/_/    \\_\\_|  \\____/|_|  \\_\\

------------------------------------------------------------------------------

""")

def promptForSigColor():
    return input('Color ([B]lue, [G]reen, [D]ark) - ').upper()

def testSigColorValid(sig_color):
    valid_colors = ['B','G','D']
    for color in valid_colors:
        if (sig_color == color):
            return True;
    return False;

def getSigColor():
    sig_color = promptForSigColor()
    sig_color_valid = testSigColorValid(sig_color)

    while (sig_color_valid != True):
        print('That is not a valid option.')
        sig_color = promptForSigColor()
        sig_color_valid = testSigColorValid(sig_color)

    return sig_color

def promptForLinesOfContent():
    return int(input('LinesOfContent (4, 6) - '))

def testLinesOfContentValid(lines_of_content):
    valid_values = [4, 6]
    for value in valid_values:
        if (lines_of_content == value):
            return True;
    return False;

def getLinesOfContent():
    lines_of_content = promptForLinesOfContent()
    lines_of_content_valid = testLinesOfContentValid(lines_of_content)

    while (lines_of_content_valid != True):
        print('That is not a valid option.')
        lines_of_content = promptForLinesOfContent()
        lines_of_content_valid = testLinesOfContentValid(lines_of_content)

    return lines_of_content

def main():
    sig_color = getSigColor()
    lines_of_content = getLinesOfContent()
    print(lines_of_content)

if __name__ == '__main__':
    main()
