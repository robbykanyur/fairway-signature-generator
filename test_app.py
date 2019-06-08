import app

def testColors():
    valid_inputs = ['B','G','D']
    response = app.validateInput('a', valid_inputs)
    response_01 = app.validateInput('B', valid_inputs)
    response_02 = app.validateInput('G', valid_inputs)
    response_03 = app.validateInput('D', valid_inputs)
    response_04 = app.validateInput('a', valid_inputs)
    assert response_01 == True
    assert response_02 == True
    assert response_03 == True
    assert response_04 == False

def testTypes():
    valid_inputs = ['SALES','OPS']
    response = app.validateInput('a', valid_inputs)
    response_01 = app.validateInput('SALES', valid_inputs)
    response_02 = app.validateInput('OPS', valid_inputs)
    response_03 = app.validateInput('b', valid_inputs)
    assert response_01 == True
    assert response_02 == True
    assert response_03 == False

def testIcons():
    valid_inputs = ['B','M','R']
    response = app.validateInput('a', valid_inputs)
    response_01 = app.validateInput('B', valid_inputs)
    response_02 = app.validateInput('M', valid_inputs)
    response_03 = app.validateInput('R', valid_inputs)
    response_04 = app.validateInput('c', valid_inputs)
    assert response_01 == True
    assert response_02 == True
    assert response_03 == True
    assert response_04 == False


def testLines():
    valid_inputs = [4,6]
    response_01 = app.validateInput(4, valid_inputs)
    response_02 = app.validateInput(6, valid_inputs)
    response_03 = app.validateInput(8, valid_inputs)
    assert response_01 == True
    assert response_02 == True
    assert response_03 == False

