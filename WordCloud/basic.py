from docx import Document
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the .docx file
file_path = 'lyrics.docx'  # Replace with your file path
doc = Document(file_path)

# Extract text from the document
text = ' '.join(paragraph.text for paragraph in doc.paragraphs)

# Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
