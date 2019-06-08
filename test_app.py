import app

def testIncorrectColors():
    response = app.validateSigColor('a')
    assert response == False

def testCorrectColors():
    response_01 = app.validateSigColor('B')
    response_02 = app.validateSigColor('G')
    response_03 = app.validateSigColor('D')
    assert response_01 == True
    assert response_02 == True
    assert response_03 == True

def testIncorrectIcons():
    response = app.validateSigIcon('b')
    assert response == False

def testCorrectIcon():
    response_01 = app.validateSigIcon('B')
    response_02 = app.validateSigIcon('M')
    response_03 = app.validateSigIcon('R')
    assert response_01 == True
    assert response_02 == True
    assert response_03 == True


def testIncorrectLines():
    response = app.validateNumberOfLines(8)
    assert response == False

def testCorrectLines():
    response_01 = app.validateNumberOfLines(4)
    response_02 = app.validateNumberOfLines(6)
    assert response_01 == True
    assert response_02 == True

