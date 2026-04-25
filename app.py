
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="FireVision AI",
    page_icon="🔥",
    layout="centered"
)

st.title("🔥 FireVision AI")
st.subheader("MVP — Detecção Inteligente de Fumaça e Incêndio")

st.info(
    "Este é um esqueleto inicial do MVP. "
    "O modelo e o dataset ainda não foram integrados."
)

uploaded_file = st.file_uploader(
    "Envie uma imagem para teste",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem enviada", use_container_width=True)

    st.warning(
        "Modelo ainda não carregado. "
        "Nenhuma inferência real foi executada."
    )

    st.markdown("### Saída esperada quando o modelo estiver integrado")
    st.write("- Classe detectada: fumaça / fogo / sem ocorrência")
    st.write("- Confiança da detecção")
    st.write("- Bounding box")
    st.write("- Status do alerta")
