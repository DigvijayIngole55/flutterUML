from transformers import AutoTokenizer, AutoModel

# Initialize GraphCodeBERT
tokenizer = AutoTokenizer.from_pretrained("microsoft/graphcodebert-base")
model = AutoModel.from_pretrained("microsoft/graphcodebert-base")

def parse_code(code_snippet):
    # Tokenize the code and pass it through the model
    inputs = tokenizer(code_snippet, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    return outputs
