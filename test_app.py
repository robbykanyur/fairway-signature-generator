import app

def testIncorrectColors():
    response = app.testSigColorValid('a')
    assert response == False

def testCorrectColors():
    response_01 = app.testSigColorValid('B')
    response_02 = app.testSigColorValid('G')
    response_03 = app.testSigColorValid('D')
    assert response_01 == True
    assert response_02 == True
    assert response_03 == True

def testIncorrectLines():
    response = app.testLinesOfContentValid(8)
    assert response == False

def testCorrectLines():
    response_01 = app.testLinesOfContentValid(4)
    response_02 = app.testLinesOfContentValid(6)
    assert response_01 == True
    assert response_02 == True



