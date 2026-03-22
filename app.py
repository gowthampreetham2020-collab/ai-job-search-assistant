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
<<<<<<< HEAD
uploaded = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded:
=======


if uploaded_file:
>>>>>>> e964efba0d8a6b86fee83d400bb44c95b9fe409f

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
<<<<<<< HEAD
    st.write("✔", skill)     
=======
    st.write("✔", skill)     
>>>>>>> e964efba0d8a6b86fee83d400bb44c95b9fe409f
