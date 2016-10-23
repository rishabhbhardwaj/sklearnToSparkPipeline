from sklearn.pipeline import Pipeline
from PipelineConverter import PipelineConverter
from sklearn.feature_extraction.text import CountVectorizer

pipeline = Pipeline([('cv', CountVectorizer())])

PipelineConverter().convert_to_spark_pipeline(sk_learn_pipeline=pipeline,file_path="/tmp/demoSparkPipeline")
