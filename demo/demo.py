import sys

sys.path.insert(0,'..')

from japanese_keyword_extractor.extractor import Extractor
from wordcloud import WordCloud
from PIL import Image
import json
import matplotlib.pyplot as plt
import numpy as np

extractor = Extractor()

with open('kokoro.json') as json_file:
    ningen_shikkaku = json.load(json_file)

for chapter in ningen_shikkaku[:]:
    extractor.add(chapter['text'])

result = extractor.extract()

mask = np.array(Image.open('mask_human.png'))
wordcloud = WordCloud(mask=mask, background_color='white', font_path='GN-KillGothic-U-KanaNB.ttf').generate_from_frequencies(result)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
