import streamlit as st

st.set_page_config(page_title="AI Education Agent", layout="centered")

st.title("🎓 AI Education Suggestion Agent")
st.subheader("Career Guidance for Intermediate Students")

st.write("Fill the student details below")

name = st.text_input("Student Name")
interest = st.text_input("Student Interest")
subject = st.text_input("Favorite Subject")
goal = st.text_input("Career Goal")

if st.button("Generate AI Suggestions"):

    career = ""
    course = ""
    skills = ""

    # AI Logic
    if "computer" in interest.lower() or "coding" in interest.lower():
        career = "Software Engineer"
        course = "B.Tech CSE / AI & ML / Data Science"
        skills = "Python, Java, Cloud Computing"

    elif "doctor" in goal.lower() or "biology" in subject.lower():
        career = "Doctor"
        course = "MBBS / BDS / Pharmacy"
        skills = "Biology, Communication, Patient Care"

    elif "business" in interest.lower() or "commerce" in subject.lower():
        career = "Business Analyst"
        course = "BBA / MBA / Finance"
        skills = "Communication, Excel, Marketing"

    elif "design" in interest.lower() or "drawing" in interest.lower():
        career = "UI/UX Designer"
        course = "Design / Animation / Multimedia"
        skills = "Figma, Photoshop, Creativity"

    else:
        career = "General Career Guidance"
        course = "Degree / Skill Development Courses"
        skills = "Communication, Problem Solving"

    st.success("AI Analysis Completed")

    st.markdown("---")
    st.header("📘 Student Report")

    st.write(f"👤 Student Name: {name}")
    st.write(f"⭐ Interest: {interest}")
    st.write(f"📚 Favorite Subject: {subject}")
    st.write(f"🎯 Career Goal: {goal}")

    st.markdown("---")
    st.header("🤖 AI Suggestions")

    st.write(f"✅ Recommended Career: {career}")
    st.write(f"✅ Suggested Course: {course}")
    st.write(f"✅ Skills to Learn: {skills}")

    st.info("Future Scope: Excellent Career Opportunities Available")

    st.balloons()