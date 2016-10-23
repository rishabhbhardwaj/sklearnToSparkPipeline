from Serializer import Serializer
from SparkPipelineGenerator import SparkPipelineGenerator
import time

class PipelineConverter:

    def convert_to_spark_pipeline(self, sk_learn_pipeline, file_path):
        serializer = Serializer()
        spark_pipeline_code = serializer.serializePipeline(sk_learn_pipeline)
        serialize_temp_file = "/tmp/tmp_"+time.strftime("%Y%m%d%H%M")
        tmp_file = open(serialize_temp_file, "w")
        tmp_file.write(spark_pipeline_code)
        tmp_file.close()
        print("Serialization Done..Generating Spark Code now...")
        spark_pipeline_gen = SparkPipelineGenerator()
        code = "#Data Ingetion and cleaning..\n"
        code += "------------------------------------------------------------\n"
        code += "#Spark Pipeline code generated from scikit-learn pipeline\n\n"
        spark_code = spark_pipeline_gen.genPipelineCode(code=code,serialized_file_path=serialize_temp_file)
        spark_code += "------------------------------------------------------------\n"
        spark_code += "#Model Creation and Save.."
        out_file = open(file_path, "w")
        out_file.write(spark_code)
        out_file.close()
        print("Conversion completed..Content written to file: "+file_path)
