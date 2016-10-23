from sklearn.feature_extraction.text import CountVectorizer
from sklearn import datasets, linear_model
from sklearn.pipeline import FeatureUnion
from skLearnPipeline import *
import json

class Serializer:
    def getCountVectorizerJson(self, count_vectorizer):
        count_vectorizer_dict = CountVectorizer().__dict__

        count_vect_data = {}
        for param in {"input", "vocabulary", "binary", "min_df"}:
            count_vect_data[param] = count_vectorizer_dict[param]
        # count_vect_json_data = json.dumps(count_vect_data)

        return count_vect_data

    def getFeatureUnionJson():
        estimators = [('countVectorizer',CountVectorizer())]
        combined = FeatureUnion(estimators)

        combined_dict = combined.__dict__

        combined_data = {}
        combined_data["transformer_list"] = combined_dict["transformer_list"]

        combined_json_data = json.dumps(combined_data)

        return combined_json_data

    def getLinearRegressionJson(self, linear_regression):
        linear_regression_dict = linear_regression.__dict__

        linear_regression_data = {}
        linear_regression_data["fit_intercept"] = linear_regression_dict["fit_intercept"]
        linear_regression_json_data = json.dumps(linear_regression_data)

        return linear_regression_json_data

    def getObjectJson(self, className,classObject):
        if className=='CountVectorizer':
            return self.getCountVectorizerJson(classObject)
        elif className=='FeatureUnion':
            return self.getFeatureUnionJson()
        elif className=='LinearRegression':
            return self.getLinearRegressionJson(classObject)

    def serializePipeline(self, pipeline):
        stages = pipeline.__dict__
        sk_pipeline_serialize = skLearnPipeline()
        sk_pipeline_serialize.stages=[]
        for stage in stages['steps']:
            sk_pipeline_stages_serailize = skLearnPipelineStages()
            sk_pipeline_stages_serailize.name = stage[0]
            sk_pipeline_stages_serailize.className = type(stage[1]).__name__
            sk_pipeline_stages_serailize.params = self.getObjectJson(type(stage[1]).__name__,stage[1])
            sk_pipeline_serialize.stages.append(sk_pipeline_stages_serailize)

        return sk_pipeline_serialize.toJSON()


# from sklearn.pipeline import Pipeline
# pipeline = Pipeline([('cv', CountVectorizer())])
# ser = Serializer()
# serialized_output = ser.serializePipeline(pipeline)
#
# print(serialized_output)
