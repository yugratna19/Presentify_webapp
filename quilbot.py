from openai import OpenAI
import os
def bullet_point(text):
  client = OpenAI(
      api_key=os.getenv("OPENAI_API_KEY"),
  )
  # text = '''Transformer comprises encoder and decoder composed of stacked identical layers , each consisting of multi-head self-attention mechanism and position-wise fully connected feed-forward network with residual connections and layer normalization . Multi-head attention involves projecting queries , keys , and values linearly several times to different subspaces , performing attention in parallel on these projected versions , and concatenating and projecting results . Additionally , positional encodings are injected to incorporate sequence order information , using sine and cosine functions of different frequencies .'''
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an expert paragraph to bullet point convertor system. Any paragraph I give to you, you convert them into short informative bulletpoints suitable for presentation slides."},
      {"role": "user", "content": f"Convert {text} into concise bullet points. Try to keep the points as short and informative as possible. Limit the number of bullet points to 5. Make sure each bullet point provides as much information as possible which is suitable for presentation slides. The paragraphs contain irrelevant words like 'nan ;, ; nan Figure + some number' so discard these words whenever you encounter them."},
    ]
  )
  output =  completion.choices[0].message.content
  real_output = ''
  for char in output:
      if char != '-':
          real_output += char
    
  print(output) 
    
  return real_output