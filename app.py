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

def validateInput(input_value, valid_values):
    for value in valid_values:
        if (input_value == value):
            return True;
    return False;

def promptForSigColor():
    return input('Color ([B]lue, [G]reen, [D]ark) - ').upper()

def getSigColor():
    sig_color = promptForSigColor()
    sig_color_valid = validateInput(sig_color, ['B','G','D'])

    while (sig_color_valid != True):
        print('That is not a valid option.')
        sig_color = promptForSigColor()
        sig_color_valid = validateInput(sig_color, ['B','G','D'])

    return sig_color

def promptForSigType():
    return input('[Sales] or [Ops] - ').upper()

def getSigType():
    sig_type = promptForSigType()
    sig_type_valid = validateInput(sig_type,['SALES','OPS'])

    while (sig_type_valid != True):
        print('That is not a valid option.')
        sig_type = promptForSigType()
        sig_type_valid = validateInput(sig_type,['SALES','OPS'])

    return sig_type

def promptForSigIcon():
    return input('[B]est Company, [M]ilitary, [R]everse - ').upper()

def getSigIcon():
    sig_icon = promptForSigIcon()
    sig_icon_valid = validateInput(sig_icon,['B','M','R'])

    while (sig_icon_valid != True):
        print('That is not a valid option.')
        sig_icon = promptForSigIcon()
        sig_icon_valid = validateInput(sig_icon,['B','M','R'])

    return sig_icon

def promptForNumberOfLines():
    return input('NumberOfLines (4, 6) - ')

def getNumberOfLines():
    lines_of_content = promptForNumberOfLines()
    lines_of_content_valid = validateInput(lines_of_content, ['4','6'])

    while (lines_of_content_valid != True):
        print('That is not a valid option.')
        lines_of_content = promptForNumberOfLines()
        lines_of_content_valid = validateInput(lines_of_content, ['4','6'])

    return lines_of_content

def getContentData(lines):
    content_data = []
    for x in range(1,(int(lines) + 1)):
        content_data.append(input('    - Content for Line ' + str(x) + ' - '))
    return content_data

def promptForSocial(name):
    return input(name + '? [Y/N] - ').upper();

def getSocialLinks():
    social_links = []

    # facebook

    facebook_true = promptForSocial('Facebook')
    facebook_true_valid = validateInput(facebook_true,['Y','N'])

    while (facebook_true_valid != True):
        print('That is not a valid option.')
        facebook_true = promptForSocial('Facebook')
        facebook_true_valid = validateInput(facebook_true,['Y','N'])

    if (facebook_true == 'Y'):
        social_links.append(['facebook', input('Facebook link: ')])

    # linkedin

    linkedin_true = promptForSocial('LinkedIn')
    linkedin_true_valid = validateInput(linkedin_true,['Y','N'])

    while (linkedin_true_valid != True):
        print('That is not a valid option.')
        linkedin_true = promptForSocial('LinkedIn')
        linkedin_true_valid = validateInput(linkedin_true,['Y','N'])

    if (linkedin_true == 'Y'):
        social_links.append(['linkedin', input('LinkedIn link: ')])

    # yelp

    yelp_true = promptForSocial('Yelp')
    yelp_true_valid = validateInput(yelp_true,['Y','N'])

    while (yelp_true_valid != True):
        print('That is not a valid option.')
        yelp_true = promptForSocial('Yelp')
        yelp_true_valid = validateInput(yelp_true,['Y','N'])

    if (yelp_true == 'Y'):
        social_links.append(['yelp', input('Yelp link: ')])

    # instagram

    instagram_true = promptForSocial('Instagram')
    instagram_true_valid = validateInput(instagram_true,['Y','N'])

    while (instagram_true_valid != True):
        print('That is not a valid option.')
        instagram_true = promptForSocial('Instagram')
        instagram_true_valid = validateInput(instagram_true,['Y','N'])

    if (instagram_true == 'Y'):
        social_links.append(['instagram', input('Instagram link: ')])

    # twitter

    twitter_true = promptForSocial('Twitter')
    twitter_true_valid = validateInput(twitter_true,['Y','N'])

    while (twitter_true_valid != True):
        print('That is not a valid option.')
        twitter_true = promptForSocial('Twitter')
        twitter_true_valid = validateInput(twitter_true,['Y','N'])

    if (twitter_true == 'Y'):
        social_links.append(['twitter', input('Twitter link: ')])

    return social_links

def getData():
    data = {}

    data['type'] = getSigType()
    data['color'] = getSigColor()
    data['icon'] = getSigIcon()

    data['displayName'] = input('Display Name: ')
    data['filename'] = input('Output Filename: ')
    data['displayTitle'] = input('Display Title: ')

    lines_of_content = getNumberOfLines()
    data['content'] = getContentData(lines_of_content)

    data['type'] = 'SALES'
    if (data['type'] == 'SALES'):
        data['links'] = []
        data['links'].append(input('Apply Now Link: '))
        data['links'].append(input('FairwayNOW Link: '))
        data['social'] = getSocialLinks()

    return data

def main():
    data = getData()

if __name__ == '__main__':
    main()
