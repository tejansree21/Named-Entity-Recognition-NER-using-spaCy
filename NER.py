# Named Entity Recognition using spaCy
import spacy

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """
Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino, California.
Elon Musk founded SpaceX and is the CEO of Tesla, headquartered in Austin, Texas.
Sundar Pichai is the CEO of Google, a company under Alphabet Inc.
"""

# Process the text
doc = nlp(text)

# Extract and display named entities
print("Named Entities, Phrases, and Labels:\n")
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")

# Optionally, visualize entities in a browser window
from spacy import displacy

# Visualize entities
displacy.serve(doc, style="ent")

# Output
"""
Apple Inc. (ORG)
Steve Jobs (PERSON)
Steve Wozniak (PERSON)
Ronald Wayne (PERSON)
Cupertino (GPE)
California (GPE)
Elon Musk (PERSON)
SpaceX (ORG)
Tesla (ORG)
Austin (GPE)
Texas (GPE)
Sundar Pichai (PERSON)
Google (ORG)
Alphabet Inc. (ORG)
"""
