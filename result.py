from sklearn.feature_extraction.text import CountVectorizer
from sklearn import datasets, linear_model
import stages

count_vectorizer = CountVectorizer()
regr = linear_model.LinearRegression()

result = {
 "stages": [
   {
     "name":"cv",
     "className":"CountVectorizer",
     "params":stages.getCountVectorizerJson(count_vectorizer)
   },
   {
     "name":"fu",
     "className":"FeatureUnion",
     "params": {"columns":["cv"]}
   },
   {
     "name":"lr",
     "className": "LinearRegression",
     "params":stages.getLinearRegressionJson(regr)
   }
 ]
}

print result
