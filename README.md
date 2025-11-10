# Named Entity Recognition (NER) using spaCy

## Overview
This project demonstrates **Named Entity Recognition (NER)** using the **spaCy** library in Python.  
NER is a fundamental task in Natural Language Processing (NLP) that identifies key information in text — such as names of people, organizations, locations, and more — and classifies them into predefined categories.

For example:
> “Elon Musk founded SpaceX and is the CEO of Tesla.”  
> → **Elon Musk (PERSON)**, **SpaceX (ORG)**, **Tesla (ORG)**

---

## Features
- Extracts named entities like **PERSON**, **ORG**, **GPE**, **DATE**, etc.  
- Uses the pre-trained **spaCy ‘en_core_web_sm’** model.  
- Supports **custom text input**.  
- Includes **visualization** of entities using spaCy’s `displacy` tool.

---

## Technologies Used
- Python  
- spaCy (for NLP and NER)  
- displaCy (for visualization)

---

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/tejansree21/Named-Entity-Recognition.git
   cd Named-Entity-Recognition

## How It Works
- Load the spaCy model
- Pass the text data through the NLP pipeline
- Extract entities and their labels
- Optionally visualize results in the browser

## Future Enhancements
- Train a custom NER model for domain-specific data
- Add a web interface using Streamlit or Flask
- Extend to multi-language entity recognition
