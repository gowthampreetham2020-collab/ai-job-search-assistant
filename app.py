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