from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "write a quick summary about python programming."}],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(f'{response}')


string_with_single_quotes = "This is a string with 'single quotes'."
string_without_single_quotes = string_with_single_quotes.replace("'", "")
print(string_without_single_quotes)

string_replace_single_with_double = string_with_single_quotes.replace("'", "\"")
print(string_replace_single_with_double)

