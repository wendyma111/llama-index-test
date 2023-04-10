from llama_index import GPTSimpleVectorIndex

newIndex = GPTSimpleVectorIndex.load_from_disk('index.json')
response = newIndex.query("小明家有几个亲戚是警察，分别是谁")
print("query: \n", "小明家有几个亲戚是警察，分别是谁\n")

print("response: ", response)
