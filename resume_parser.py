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
