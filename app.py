import streamlit as st
from PIL import Image
import easyocr
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Electrical Drawing Analyzer", layout="wide")
st.title("📊 Electrical Drawing Analyzer")
st.markdown("Analyze uploaded drawings and trace **upstream/downstream** electrical elements.")

col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("Upload an Electrical Drawing (Image)", type=["png", "jpg", "jpeg"])

with col2:
    query = st.text_area("Ask a question about the drawing:")

# Now you can safely use uploaded_file and query
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

    # Simulated logic for upstream/downstream based on keywords
    components = ["Transformer", "Breaker", "Busbar", "Load"]
    graph = nx.DiGraph()
    for i in range(len(components) - 1):
        graph.add_edge(components[i], components[i+1])

    st.markdown("### 🔁 Inferred Connection Path")
    fig, ax = plt.subplots(figsize=(8, 4))
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=2000, font_size=14, edge_color='gray', ax=ax)
    st.pyplot(fig)

    st.markdown("### 🤖 Model Interpretation")
    if "upstream" in query.lower():
        st.info("Upstream components: Transformer → Breaker → Busbar")
    elif "downstream" in query.lower():
        st.info("Downstream components: Busbar → Load")
    else:
        st.warning("Query doesn't mention upstream/downstream. Placeholder model logic applied.")
