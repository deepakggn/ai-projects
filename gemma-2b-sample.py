from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")

input_text = "What's your name?"
input_ids = tokenizer(input_text, return_tensors="pt", return_attention_mask=False)

outputs = model.generate(**input_ids,max_new_tokens=20)
print(tokenizer.decode(outputs[0]))