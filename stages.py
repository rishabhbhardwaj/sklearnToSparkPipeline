from sklearn.feature_extraction.text import CountVectorizer
from sklearn import datasets, linear_model
from sklearn.pipeline import FeatureUnion
import json

"""
{
 "stages": [
   {
     "name":"cv",
     "className":"CountVectorizer"
     "params":null
   },
   {
     "name":"fu",
     "className":"FeatureUnion"
     "params": {"columns":["cv"]}
   },
   {
     "name":"lr",
     "className": "LinearRegression"
     "params":{"fit_intercept":"true"}
   }
 ]
}
"""




def getCountVectorizerJson(count_vectorizer):
    count_vectorizer_dict = CountVectorizer().__dict__

    count_vect_data = {}
    for param in {"input", "vocabulary", "binary", "min_df"}:
        count_vect_data[param] = count_vectorizer_dict[param]
    count_vect_json_data = json.dumps(count_vect_data)

    return count_vect_json_data

def getFeatureUnionJson():
    estimators = [('countVectorizer',CountVectorizer())]
    combined = FeatureUnion(estimators)

    combined_dict = combined.__dict__

    combined_data = {}
    combined_data["transformer_list"] = combined_dict["transformer_list"]

    combined_json_data = json.dumps(combined_data)

    return combined_json_data

def getLinearRegressionJson(linear_regression):
    linear_regression_dict = linear_regression.__dict__

    linear_regression_data = {}
    linear_regression_data["fit_intercept"] = linear_regression_dict["fit_intercept"]
    linear_regression_json_data = json.dumps(linear_regression_data)

    return linear_regression_json_data

def getObjectJson(className,classObject):
    if className=='CountVectorizer':
        return getCountVectorizerJson(classObject)
    elif className=='FeatureUnion':
        return getFeatureUnionJson()
    elif className=='LinearRegression':
        return getLinearRegressionJson(classObject)

def genJson(pipeline,json):
    stagesStr = ""
    stages = pipeline.__dict__
    for stage in stages['steps']:
        stagesStr+='{"name":"'+stage[0]+'","className":"'+type(stage[1]).__name__+'","params":"'+getObjectJson(type(stage[1]).__name__,stage[1])+'}'

"""
count_vectorizer = CountVectorizer()
regr = linear_model.LinearRegression()
print getCountVectorizerJson(count_vectorizer)
print getLinearRegressionJson(regr)
print getFeatureUnionJson()
"""
"""
sklearn, spark

CountVectorizer:
input, inputCol
vocabulary, vocabulary
binary, binary
min_df, minDF

LinearRegression:
fit_intercept, fitIntercept

"""
