japanese_keyword_extractor
=============



### Introduction
---
**japanese_keyword_extractor** is a python script to extract keywords from Japanese text.  **Janome** is used to tokenize a text. Extrating algorithm is **TF-IDF**.
### Usage
---
```
# Import Extractor module
from japanese_keyword_extractor.extractor import Extractor

extractor = Extractor()

# If you want to add custom dictionary, add csv file to arugument 
#extractor = Extractor('custom_dictionary.csv')

# Add texts that you want to analyze
extractor.add(text_1)
extractor.add(text_2)
extractor.add(text_3)

# Get the result
result = extractor.extract()
```
### Demo
---
Demo extracts keywords from 'No Longer Human' by Osamu Dazai. Text file is downloaded from aozora(https://www.aozora.gr.jp/). It prints keywords on mask image using ***wordcloud***.