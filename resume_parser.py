<<<<<<< HEAD
import pdfplumber

def parse_resume(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text
=======
st.subheader("Upload Resume")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"],
    key="resume_upload"
)

if uploaded_file:

    resume_text = parse_resume(uploaded_file)

    st.subheader("Resume Text Preview")

    st.write(resume_text[:500])

    skills = detect_skills(resume_text)

    st.subheader("Detected Skills")

    for skill in skills:
        st.write("✔", skill)
>>>>>>> e964efba0d8a6b86fee83d400bb44c95b9fe409f
