import streamlit as st
from PIL import Image
#import pytesseract  # remove this
import easyocr  # add this
import networkx as nx
import matplotlib.pyplot as plt

# ...rest unchanged...

if uploaded_file and query:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Drawing", use_column_width=True)
    
    with st.spinner("🔍 Extracting text from image using EasyOCR..."):
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(image, detail=0)
        text = " ".join(result)

    st.success("✅ Text Extraction Complete")
    st.markdown("### 📜 Extracted Text")
    st.code(text[:1000])

# ...rest unchanged...

