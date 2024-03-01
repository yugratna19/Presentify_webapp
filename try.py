from pptxtools import split_sentences

x = '''Study on I/O Cost of Linear Repair Schemes for Reed-Solomon Codes
 Contributions include formula for computing I-O cost, lower bounds for RS codes with two and three parities, and reduced I-E cost.
 Highlights importance of considering repair bandwidth and I-e cost in efficient repair schemes.
 Provides insights into cost of existing repair schemes and opens research for optimizing I and I cost in distributed storage systems.'''
 
print(split_sentences(x))