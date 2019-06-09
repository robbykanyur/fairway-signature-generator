import os
from os import path
import boto3
import botocore
import re
import json
import shutil
from shutil import copyfile

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

    lines_of_content = getNumberOfLines()
    data['content'] = getContentData(lines_of_content)

    data['type'] = 'SALES'
    if (data['type'] == 'SALES'):
        data['links'] = []
        data['links'].append(input('Apply Now Link: '))
        data['links'].append(input('FairwayNOW Link: '))
        data['social'] = getSocialLinks()

    return data

def getPhotoPath():
    photo_exists = False
    while (photo_exists == False):
        photo_path = input('Absolute path to profile photo: ')
        if (path.exists(photo_path)):
            break
        else:
            print('That file does not exist.')
    return(photo_path)

def uploadProfilePhoto(data):
    photo_path = getPhotoPath()
    photo_filename = re.findall(r'^.*\/(.*)$', photo_path)

    s3 = boto3.resource('s3')
    try:
        s3.Object('fairway-salesforce', 'signatures/' + photo_filename[0]).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            s3.meta.client.upload_file(photo_path, 'fairway-salesforce', 'signatures/' + photo_filename[0])

    data['photo'] = photo_filename
    return data

def loadJSON():
    with open('variables.json', 'r') as file:
        filedata = file.read().replace('\n','')
    variables = json.loads(filedata)
    return variables

def testData():
    data = {
        'type': 'SALES', 
        'color': 'B', 
        'icon': 'M', 
        'displayName': 'Robert Kanyur', 
        'filename': 'kanyur-robert', 
        'content': [
            'Marketing Manager',
            'Phone: 480-346-1371', 
            'Fax: 888-676-7807', 
            'www.fairway321.com',
            '17851 N. 85th St. #250', 
            'Scottsdale, AZ 85255'], 
        'links': [
            'http://google.com', 
            'http://google.com'], 
        'social': [
            ['facebook', 'http://facebook.com'],
            ['instagram', 'http://instagram.com'],
            ['yelp', 'http://yelp.com'],
            ['twitter', 'http://twitter.com']
        ],
        'photo': ['profile-brady-jessica.png']
    }
    return data

def buildTemplate(data, variables):
    # create src and dist variables
    src_dir = os.getcwd()
    dist_dir = src_dir + '/dist/' + data['filename']
    dist_file = dist_dir + '/index.html'

    # clean output directory
    if os.path.isdir(src_dir + '/dist'):
        shutil.rmtree(src_dir + '/dist')
    os.makedirs(dist_dir)

    # copy base file
    copyfile(src_dir + '/templates/base.html', dist_dir + '/index.html')

    # insert content section
    with open(dist_file, 'r') as file:
        filedata = file.read()

    if (len(data['content']) == 6):
        with open(src_dir + '/templates/content_06.html', 'r') as file:
            contentdata = file.read()
    else:
        with open(src_dir + '/templates/content_04.html', 'r') as file:
            contentdata = file.read()

    filedata = filedata.replace('{{ CONTENT }}', contentdata)
    with open(dist_file, 'w') as file:
        file.write(filedata)

    # insert buttons section
    with open(dist_file, 'r') as file:
        filedata = file.read()
    if (data['type'] == 'SALES'):
        with open(src_dir + '/templates/buttons_sales.html', 'r') as file:
            contentdata = file.read()
    else:
        with open(src_dir + '/templates/buttons_ops.html', 'r') as file:
            contentdata = file.read()

    filedata = filedata.replace('{{ BUTTONS }}', contentdata)
    with open(dist_file, 'w') as file:
        file.write(filedata)

    # insert social section
    with open(dist_file, 'r') as file:
        filedata = file.read()

    if (len(data['social']) == 1):
        with open(src_dir + '/templates/social_01.html', 'r') as file:
            socialdata = file.read()
    elif (len(data['social']) == 2):
        with open(src_dir + '/templates/social_02.html', 'r') as file:
            socialdata = file.read()
    elif (len(data['social']) == 3):
        with open(src_dir + '/templates/social_03.html', 'r') as file:
            socialdata = file.read()
    elif (len(data['social']) == 4):
        with open(src_dir + '/templates/social_04.html', 'r') as file:
            socialdata = file.read()
    elif (len(data['social']) == 5):
        with open(src_dir + '/templates/social_05.html', 'r') as file:
            socialdata = file.read()
    else:
        socialdata = ''

    filedata = filedata.replace('{{ SOCIAL }}', socialdata)
    with open(dist_file, 'w') as file:
        file.write(filedata)

    # find and replace
    with open(dist_file, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace('{{ AWS }}', variables['aws'])
    filedata = filedata.replace('{{ PROFILE_FILENAME }}', data['photo'][0])
    filedata = filedata.replace('{{ CONTACT_NAME }}', data['displayName'])
    for x in range(len(data['content'])):
        filedata = filedata.replace('{{ CONTENT_0' + str((x + 1)) + ' }}', data['content'][x])

    if (data['type'] == 'SALES'):
        filedata = filedata.replace('{{ APPLICATION_LINK }}', data['links'][0])
        filedata = filedata.replace('{{ FAIRWAYNOW_LINK }}', data['links'][1])

    # images for blue template
    if (data['color'] == 'B'):
        filedata = filedata.replace('{{ HEX }}', variables['blue']['hex'])
        filedata = filedata.replace('{{ FAIRWAY }}', variables['blue']['fairway'])

        if (data['type'] == 'SALES'):
            filedata = filedata.replace('{{ APPLICATION_IMAGE }}', variables['blue']['application'])
            filedata = filedata.replace('{{ FAIRWAYNOW_IMAGE }}', variables['blue']['fairwaynow'])

        if (data['icon'] == 'B'):
            filedata = filedata.replace('{{ ICON }}', variables['blue']['bmc'])
        if (data['icon'] == 'M'):
            filedata = filedata.replace('{{ ICON }}', variables['blue']['military'])
        if (data['icon'] == 'R'):
            filedata = filedata.replace('{{ ICON }}', variables['blue']['reverse'])

        for x in range(1,(len(data['social']) + 1)):
            filedata = filedata.replace('{{ SOCIAL_IMAGE_' + str(x) + ' }}', 'social-' + data['social'][x - 1][0] + '-' + variables['blue']['iconColor'] + '.png')

    with open(dist_file, 'w') as file:
        file.write(filedata)

def main():
    # data = getData()
    # data = uploadProfilePhoto(data)

    data = testData()
    variables = loadJSON()
    buildTemplate(data, variables)

if __name__ == '__main__':
    main()
