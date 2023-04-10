# 文本分隔并且索引
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, ServiceContext

# initialize simple vector indices + global vector index
service_context = ServiceContext.from_defaults(chunk_size_limit=512)
# 加载data文件夹下的示例文本
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

# 将生成后的索引存储至本地
index.save_to_disk('index.json')