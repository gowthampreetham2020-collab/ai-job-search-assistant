import streamlit as st
from scraper import get_jobs

st.title("AI Job Search Assistant")

query = st.text_input("Search for jobs")

if st.button("Search Jobs"):

    jobs = get_jobs(query)

    if jobs:
        st.subheader("Job Results")

        for job in jobs[:10]:
            st.write(job)

    else:
        st.write("No jobs found")
location = st.selectbox(
"Location",
["Any","Bangalore","Mumbai","Delhi","Pune","Hyderabad"]
)        


if uploaded_file:

    from resume_parser import parse_resume

    resume_text = parse_resume(uploaded)

    st.write("Resume loaded successfully")
import streamlit as st
from resume_parser import parse_resume  
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:

    resume_text = parse_resume(uploaded_file)

    st.subheader("Resume Text Preview")

    st.write(resume_text[:500]) 
from skills import detect_skills

skills = detect_skills(resume_text)

st.subheader("Detected Skills")

for skill in skills:
    st.write("✔", skill)     
