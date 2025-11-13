import streamlit as st

st.set_page_config(page_title="Persona App", layout="wide")

# ----- GLOBAL STYLE FROM FIGMA -----
st.markdown("""
    <style>
        /* Page background and font from Figma */
        body {
            background-color: #0f172a;
            color: #e5e7eb;
            font-family: "Inter", sans-serif;
        }

        /* Card style */
        .card {
            border-radius: 16px;
            padding: 20px;
            background: #111827;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .title {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .subtitle {
            font-size: 16px;
            color: #9ca3af;
        }
    </style>
""", unsafe_allow_html=True)

# ----- HEADER (like your Figma hero section) -----
st.markdown(
    """
    <div class="card">
        <div class="title">AI-Powered Persona Engine</div>
        <div class="subtitle">Turn your raw customer data into rich synthetic personas.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")  # spacing

# ----- MAIN LAYOUT (copied from Figma concept) -----
left_col, right_col = st.columns([1, 2])

with left_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Controls")
    uploaded_file = st.file_uploader("Upload customer CSV")
    persona_count = st.slider("Number of personas", 1, 10, 3)
    if st.button("Generate Personas"):
        st.info("This is where your backend logic runs.")
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Persona Output")
    st.write("Show persona cards / charts here to match your Figma design.")
    st.markdown('</div>', unsafe_allow_html=True)
