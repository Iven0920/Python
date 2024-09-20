from pyspark import SparkConf, SparkContext
import os
os.environ['JAVA_HOME'] = 'd:\Java'
# import os
# os.environ['JAVA_HOME'] = 'd:/java/jdk-1.8'
# 创建SparkConf类对象  setMaster设置运行模式：本地  setappName:设置spark任务名称
# 链式调用
conf1 = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# # 作用同下
# conf = SparkConf()
# conf.setMaster("local[*]")
# conf.setAppName("test_spark_app")

# 基于SparkConf类对象创建SprkContext对象
sc = SparkContext(conf=conf1)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()