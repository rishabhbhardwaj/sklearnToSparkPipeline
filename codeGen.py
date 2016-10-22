import json
from symbols import symbols
from pprint import pprint

var_names=[]

def genPipelineCode(code):
    with open('samplePipelineInfo.json') as data_file:
        data = json.load(data_file)
    jsonContent = data
    # pprint(jsonContent)
    for stage in jsonContent["stages"]:
        code += genStageCode(stage)+"\n"

    code +="from pyspark.ml import Pipeline\n"
    code +="pipeline = Pipeline(stages=["
    for name in var_names:
        code+=name+", "
    code = code[:-2]
    code += "])\n"
    return code

def genStageCode(stage):
    global var_names;
    var_name = stage["name"]
    var_names.append(var_name)
    stage_type = stage["className"]
    params = stage["params"]
    if stage_type == symbols.COUNTVECTORIZER:
        return genCountVectorizerCode(var_name, params)
    elif stage_type == symbols.FEATUREUNION:
        return genVectorAssemblerCode(var_name, params)
    elif stage_type == symbols.LINEARREGRESSION:
        return genLinearRegressionCode(var_name, params)

def genCountVectorizerCode(var_name, params):
    count_vectorizer_code = "from pyspark.ml.feature import CountVectorizer\n"
    count_vectorizer_code += var_name+" = CountVectorizer("
    if params!= None:
        if "input" in params:
            count_vectorizer_code+="inputCol="+params["input"]+", "
        if "binary" in params:
            count_vectorizer_code+="binary="+params["binary"]+", "
        if "min_df" in params:
            count_vectorizer_code+="min_df="+params["min_df"]
    count_vectorizer_code += ")\n"
    return count_vectorizer_code

def genVectorAssemblerCode(var_name, params):
    va_code = "from pyspark.ml.feature import VectorAssembler\n"
    va_code += var_name+" = VectorAssembler(inputCols=["
    for cols in params["columns"]:
        va_code +=cols+", "
    va_code = va_code[:-2]
    va_code+="])"
    return va_code

def genLinearRegressionCode(var_name, params):
    lr_code = "from pyspark.ml.regression import LinearRegression\n"
    lr_code += var_name+" = LinearRegression("
    if params!= None:
        if "fit_intercept" in params:
            lr_code+="fitIntercept="+params["fit_intercept"]
    lr_code +=")"
    return lr_code

code = "#Spark Pipeline code generated from scikit-learn pipeline\n\n"
sparkPipelineCode = genPipelineCode(code)
print(sparkPipelineCode)
