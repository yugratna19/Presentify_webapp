def bullet_point(text):
  from openai import OpenAI
  import os
  client = OpenAI(
      api_key=os.getenv("OPENAI_API_KEY"),
  )
  # text = '''Transformer comprises encoder and decoder composed of stacked identical layers , each consisting of multi-head self-attention mechanism and position-wise fully connected feed-forward network with residual connections and layer normalization . Multi-head attention involves projecting queries , keys , and values linearly several times to different subspaces , performing attention in parallel on these projected versions , and concatenating and projecting results . Additionally , positional encodings are injected to incorporate sequence order information , using sine and cosine functions of different frequencies .'''
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an expert paragraph to bullet point converter"},
      {"role": "user", "content": f"Convert {text} into bullet points. Limit the bullet points to 5 or less points."},
    ]
  )
  output =  completion.choices[0].message.content
  real_output = ''
  for char in output:
      if char != '-':
          real_output += char
    
  print(output) 
    
  return real_output

# bullet_point('Transformer comprises encoder and decoder composed of stacked identical layers , each consisting of multi-head self-attention mechanism and position-wise fully connected feed-forward network with residual connections and layer normalization . Multi-head attention involves projecting queries , keys , and values linearly several times to different subspaces , performing attention in parallel on these projected versions , and concatenating and projecting results . Additionally , positional encodings are injected to incorporate sequence order information , using sine and cosine functions of different frequencies .')