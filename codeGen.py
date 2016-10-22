import json
from symbols import symbols
from pprint import pprint

def genPipelineCode(code):
    print("In pipeline gen code")
    with open('samplePipelineInfo.json') as data_file:
        data = json.load(data_file)
    jsonContent = data
    pprint(jsonContent)
    for stage in jsonContent["stages"]:
        code += genStageCode(stage)+"\n"

    return code

def genStageCode(stage):
    stageType = stage["name"]
    params = stage["params"]
    if stageType == symbols.COUNTVECTORIZER:
        return genCountVectorizerCode(params)
    elif stageType == symbols.FEATUREUNION:
        return genVectorAssemblerCode(params)
    elif stageType == symbols.LINEARREGRESSION:
        return genLinearRegressionCode(params)

def genCountVectorizerCode(params):
    return "CountVectorizer"

def genVectorAssemblerCode(params):
    return "VectorAssembler"

def genLinearRegressionCode(params):
    return "LinearRegression"


code = "#Spark Pipeline code generated from scikit-learn pipeline\n"
sparkPipelineCode = genPipelineCode(code)
print(sparkPipelineCode)
