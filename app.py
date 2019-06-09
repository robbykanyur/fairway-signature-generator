import os
from os import path
import boto3
import botocore
import re
import csv
import json
import shutil
from shutil import copyfile
from paramiko import SSHClient
from scp import SCPClient
import sys
from templates import populate

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

def promptForUpload():
    return input('Upload to prod server? [Y/N] - ').upper()

def getUpload():
    should_upload = promptForUpload()
    upload_valid = validateInput(should_upload, ['Y','N'])

    while (upload_valid != True):
        print('That is not a valid option.')
        should_upload = promptForUpload()
        should_upload_valid = validateInput(should_upload, ['Y','N'])

    return should_upload

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

def promptForUpload():
    return input('Upload to prod server? [Y/N] - ').upper()

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
    dataArray = []
    data = {}

    data['type'] = getSigType()
    data['color'] = getSigColor()
    data['icon'] = getSigIcon()

    data['displayName'] = input('Display Name: ')
    data['filename'] = input('Output Filename: ')

    lines_of_content = getNumberOfLines()
    data['content'] = getContentData(lines_of_content)

    if (data['type'] == 'SALES'):
        data['links'] = []
        data['links'].append(input('Apply Now Link: '))
        data['links'].append(input('FairwayNOW Link: '))
        data['social'] = getSocialLinks()
    else:
        data['social'] = []
        data['links'] = []

    dataArray.append(data)
    return dataArray

def getPhotoPath():
    photo_exists = False
    while (photo_exists == False):
        photo_path = input('Absolute path to profile photo: ')
        if (path.exists(photo_path)):
            break
        else:
            print('That file does not exist.')
    return(photo_path)

def getCSVPath():
    csv_exists = False
    while (csv_exists == False):
        csv_path = input('Absolute path to CSV file: ')
        if (path.exists(csv_path)):
            break
        else:
            print('That file does not exist.')
    return(csv_path)

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


def cleanDirectories():
    src_dir = os.getcwd()
    if os.path.isdir(src_dir + '/dist'):
        shutil.rmtree(src_dir + '/dist')

def setupDirectories(data):
    # create src and dist variables
    src_dir = os.getcwd()
    dist_dir = src_dir + '/dist/' + data['filename']
    dist_file = dist_dir + '/index.html'
    os.makedirs(dist_dir)

    return [src_dir, dist_dir, dist_file]

def buildTemplate(data, variables, dirs):
    src_dir = dirs[0]
    dist_dir = dirs[1]
    dist_file = dirs[2]

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
        filedata = filedata.replace('{{ HEX_ALT }}', variables['blue']['alt'])
        filedata = filedata.replace('{{ FAIRWAY }}', variables['blue']['fairway'])
        filedata = filedata.replace('{{ NAME_COLOR }}', variables['blue']['nameColor'])

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

    # images for green template
    if (data['color'] == 'G'):
        filedata = filedata.replace('{{ HEX }}', variables['green']['hex'])
        filedata = filedata.replace('{{ HEX_ALT }}', variables['green']['alt'])
        filedata = filedata.replace('{{ FAIRWAY }}', variables['green']['fairway'])
        filedata = filedata.replace('{{ NAME_COLOR }}', variables['green']['nameColor'])

        if (data['type'] == 'SALES'):
            filedata = filedata.replace('{{ APPLICATION_IMAGE }}', variables['green']['application'])
            filedata = filedata.replace('{{ FAIRWAYNOW_IMAGE }}', variables['green']['fairwaynow'])

        if (data['icon'] == 'B'):
            filedata = filedata.replace('{{ ICON }}', variables['green']['bmc'])
        if (data['icon'] == 'M'):
            filedata = filedata.replace('{{ ICON }}', variables['green']['military'])
        if (data['icon'] == 'R'):
            filedata = filedata.replace('{{ ICON }}', variables['green']['reverse'])

        for x in range(1,(len(data['social']) + 1)):
            filedata = filedata.replace('{{ SOCIAL_IMAGE_' + str(x) + ' }}', 'social-' + data['social'][x - 1][0] + '-' + variables['green']['iconColor'] + '.png')

    # images for dark template
    if (data['color'] == 'D'):
        filedata = filedata.replace('{{ HEX }}', variables['dark']['hex'])
        filedata = filedata.replace('{{ HEX_ALT }}', variables['dark']['alt'])
        filedata = filedata.replace('{{ FAIRWAY }}', variables['dark']['fairway'])
        filedata = filedata.replace('{{ NAME_COLOR }}', variables['dark']['nameColor'])

        if (data['type'] == 'SALES'):
            filedata = filedata.replace('{{ APPLICATION_IMAGE }}', variables['dark']['application'])
            filedata = filedata.replace('{{ FAIRWAYNOW_IMAGE }}', variables['dark']['fairwaynow'])

        if (data['icon'] == 'B'):
            filedata = filedata.replace('{{ ICON }}', variables['dark']['bmc'])
        if (data['icon'] == 'M'):
            filedata = filedata.replace('{{ ICON }}', variables['dark']['military'])
        if (data['icon'] == 'R'):
            filedata = filedata.replace('{{ ICON }}', variables['dark']['reverse'])

        for x in range(1,(len(data['social']) + 1)):
            filedata = filedata.replace('{{ SOCIAL_IMAGE_' + str(x) + ' }}', 'social-' + data['social'][x - 1][0] + '-' + variables['dark']['iconColor'] + '.png')

    with open(dist_file, 'w') as file:
        file.write(filedata)

def uploadToServer(data):
    for x in data:
        foldername = os.getcwd() + '/dist/' + x['filename']
        print ('Uploading ' + foldername + ' to prod server...')
        os.system('scp -r ' + foldername + ' deploy@prod:html/fairway321.com/signatures')

def bulkBuild(data, variables):
    for x in range(0, len(data)):
        dirs = setupDirectories(data[x])
        instance = data[x]
        buildTemplate(instance, variables, dirs)
        print('Generating ' + instance['filename'] + '...')

def generateEmptyObject():
    data = {
        'displayName': '',
        'filename': '',
        'type': '',
        'color': '',
        'icon': '',
        'content': [],
        'links': [],
        'social': [],
        'photo': []
    }
    return data

def bulkImport(csv_file):
    data = []
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            instance = generateEmptyObject()
            if line_count < 2:
                line_count += 1
            else:
                instance['displayName'] = row[0].lower()
                instance['filename'] = row[1].lower()
                instance['type'] = row[2].lower()
                photo_path = row[23].lower()
                photo_filename = re.findall(r'^.*\/(.*)$', photo_path)
                instance['photo'] = photo_filename
                instance['content'].append(row[5])
                instance['content'].append(row[6])
                instance['content'].append(row[7])
                instance['content'].append(row[8])
                if row[3].lower() == 'blue':
                    instance['color'] = 'B'
                elif row[3].lower() == 'green':
                    instance['color'] = 'G'
                elif row[3].lower() == 'gray':
                    instance['color'] = 'D'
                if row[4].lower() == 'best':
                    instance['icon'] = 'B'
                elif row[4].lower() == 'reverse':
                    instance['icon'] = 'R'
                elif row[4].lower() == 'military':
                    instance['icon'] = 'M'
                if row[9] != '':
                    instance['content'].append(row[9])
                    instance['content'].append(row[10])
                if instance['type'] == 'sales':
                    instance['links'].append(row[11])
                    instance['links'].append(row[12])
                if row[13] != '':
                    social_one = []
                    social_one.append(row[13])
                    social_one.append(row[14])
                    instance['social'].append(social_one)
                if row[15] != '':
                    social_one = []
                    social_one.append(row[15])
                    social_one.append(row[16])
                    instance['social'].append(social_one)
                if row[17] != '':
                    social_one = []
                    social_one.append(row[17])
                    social_one.append(row[18])
                    instance['social'].append(social_one)
                if row[19] != '':
                    social_one = []
                    social_one.append(row[19])
                    social_one.append(row[20])
                    instance['social'].append(social_one)
                if row[21] != '':
                    social_one = []
                    social_one.append(row[21])
                    social_one.append(row[22])
                    instance['social'].append(social_one)

                data.append(instance)
                line_count+= 1
    return data

def main():
    cleanDirectories()

    testing = False
    bulk = False
    if (len(sys.argv) > 1):
        if(sys.argv[1] == '--test'):
            testing = True
        if(sys.argv[1] == '--bulk'):
            bulk = True
    else:
        testing = False
    variables = loadJSON()

    if bulk == True:
        csv_file = getCSVPath()
        data = bulkImport(csv_file)
        print()
        bulkBuild(data, variables,)
        print()

    elif testing == True:
        data = populate()
        bulkBuild(data, variables,)
        print()

    else:
        data = getData()
        instance = data[0]
        dirs = setupDirectories(instance)
        instance = uploadProfilePhoto(instance)
        buildTemplate(instance, variables, dirs)

    if testing == False:
        should_upload = getUpload()
        if (should_upload == 'Y'):
            uploadToServer(data)
            print()

    print('Operation completed successfully.')

if __name__ == '__main__':
    main()
