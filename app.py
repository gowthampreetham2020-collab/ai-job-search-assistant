import streamlit as st
from scraper import get_jobs
from resume_parser import parse_resume
from skills import detect_skills

st.title("AI Job Search Assistant")

# --- Job Search Section ---
query = st.text_input("Search for jobs")
location = st.selectbox("Location", ["Any", "Bangalore", "Mumbai", "Delhi", "Pune", "Hyderabad"])

if st.button("Search Jobs"):
    jobs = get_jobs(query)
    if jobs:
        st.subheader("Job Results")
        for job in jobs[:10]:
            st.write(job)
    else:
        st.write("No jobs found")

# --- Resume Upload & Skill Detection ---
st.subheader("Upload Resume")
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"], key="resume_upload")

if uploaded_file:
    resume_text = parse_resume(uploaded_file)
    st.subheader("Resume Text Preview")
    st.text_area("Resume Preview", resume_text, height=300)

    skills = detect_skills(resume_text)
    st.subheader("Detected Skills")
    if skills:
        for skill in skills:
            st.write("✔", skill)
    else:
        st.write("No skills detected")