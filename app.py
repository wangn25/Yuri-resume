import streamlit as st
from pathlib import Path
from PIL import Image



#---path settings---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Yuri Wang"
PAGE_ICON = ":wave:"
NAME = "Yuri Wang"
DESCRIPTION =(
     """
Working experience on full cycle of project management both domestic& global projects.
11 years of pre-sale solution and transition and IT helpdesk operation management and project management experience. Good people management skill and leadership skill with strong teamwork spirit.

Strong communication skills with good command of both spoken and written English. Ability to multi-task and prioritize work. Ability to deliver result within tight timeframe. 
Strong analytical skill and good at MySQL, PowerQuery, PowerPivot, Automate& Powerapps, proficient in PowerBI dashboard design and deployment. 
**Python user on AI app Dev& data analysis orientation.**

"""
)
EMAIL = "swat_2046@hotmail.com"
SOCIAL_MEDIA = {
   
    "***🗿Need GPT support***": "https://yuri-knowledgegpt.streamlit.app/",
    "GitHub": "https://github.com",
   
}
PROJECTS = {
    "🏆 **Forecast Sales** - Machine Learning model build up to train& forecast telemarketing": "https://www.163.com",
    "🏆 **User Persona** - Build up user persona to identfy telemarketing opportunities": "https://www.163.com",
    "🏆 **P&L BI Dashboard** - Operation P&L monitor across multiple accounts": "https://www.163.com",
    "🏆 **MS Power Platform Automation** - Jidoka initiatives  to improve productivity": "https://www.163.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=":lollipop:")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# with col3:
#     gif_url= ("https://lottie.host/024e28d9-c1e1-4081-a778-c50dea7c774e/GEwO6idrMN.lottie")
#     st.lottie(gif_url, key = "hello lottie")

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---

st.markdown("---")

st.write('\n')
st.subheader("Experience & Qulifications")


st.write(
    """
- ✔️ Good people management skill and leadership skill  
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in data visualizaion, automation
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 💯 Methnology: Six Sigma Certification
- 👩‍💻 Programming: Python (Streamlit, Pandas), MS Power platform
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees, Random Forester
- 🗄️ Databases: Access, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🌊", "**Black belt- Genpact LDT**")
st.write("2021/7 - Present")
st.write(
    """
1.	Develop and maintain an in-depth understanding of Lean/Six Sigma philosophy, theory, applications, tools, and tactics in the Customer Service & SCM service-line.
2.	Facilitate the execution of plant strategy and provide lean expertise and guidance through focused and sustainable value stream transformation to enable cross-functional collaboration, best practice sharing, and implementation.
3.	As business partner, facilitate responsible Operations/Depts. to continuously improve operational performance.
4.	Lead assigned teams throughout the problem-solving efforts, identifying barriers to the effective implementation of lean & six sigma process and taking the necessary action to resolve or escalate issues/problems.
5.	Report as appropriate on project status through the established project tracking system and manage project reviews.
6.	Maintain an awareness of impact to the customer of process improvement projects, as well as customer requirements regarding process change, ensuring effective communication is maintained to eliminate any potential negative impact.
7.	Mentor and coach Lean & Six Sigma Green Belts candidates. Support development of a pipeline of GB team members able to drive business result.
8.	Provide necessary lean & six sigma tools training to develop targeted people’s capability on PDCA & DMAIC methodology application.

"""
)

# --- JOB 2
st.write('\n')
st.write("🌊", "**Project Manager-Genpact CS**")
st.write("2018/04-2021/06")
st.write(
    """
**Drive Operation Excellence**
1.	Worked with service delivery leaders to provide operational consulting support across multiple domains.
2.	Supported the procurement BPR (business process re-engineering) project in 2018 and 2019, overseeing 8 months of new process implementation.
3.	Conducted financial process data analysis, implemented KPI improvement projects, and designed interactive Power BI reports, receiving high recognition from customers.
4.	Engaged in new project client interactions, developed business cases, participated in MSA discussions, and analyzed clients' existing processes while designing future processes.
5.	Handled RFX responses for a large online shopping platform contact center, including pre-sale activities and Sol-ID & Transition support.
6.	Supported and coordinated digital initiatives across various domains.

"""
)

# --- JOB 3
st.write('\n')
st.write("🌊", "**Project Manager-Genpact ITMS**")
st.write("2017/01-2018/04")
st.write(
    """
APAC regional leader of IT helpdesk support center.
1.	Ensure customer satisfaction and foster continuous business growth.
2.	Led five teams with over 60 staff members, comprising three foreign teams and two local teams, across the APAC region.
3.	Determine, monitor, and review the economic aspects of all sites, including costs, operational budgets, staffing requirements, resources, and risks.
4.	Led a team to establish attainable goals and achieve KPI targets.
5.	Collaborated closely with other functional teams on the development of new business models and projects aimed at improving performance.
6.	Implemented personnel management and institutional mechanisms.

"""
)


# --- JOB 4
st.write('\n')
st.write("🌊", "**Solution Assistant Manager-Genpact ITMS**")
st.write("2015/8-2017/1")
st.write(
    """
1.	Support New Deal RFPs and RFIs across various industries for clients. 
2.	Collaborated closely with Genpact's Operation function support and transition team to deliver solutions directly to customers during pre-sales, early project start-up, and transition phases.
3.	Ensured seamless integration with customers in the IT helpdesk services area.
4.	Coordinated and integrated internal resources to cover the service scope from the initial design solution to program implementation and tracked the progress of implementation.
5.	Implemented programs for improving project functions.

"""
)

# --- JOB 5
st.write('\n')
st.write("🍦", "**Subject Matter Expert HP-GSD**")
st.write("2012/03-2015/08")
st.write(
    """
1.	Provide second-level technical support for team span of 30 staffs. 
2.	Conduct onboarding training for new employees.
3.	Facilitate the transition of new projects and the transfer of knowledge.
4.	Manage the daily operations of the team, including monitoring KPIs, scheduling staff, handling escalations, etc.
5.	Take responsibility for global team communication to address challenging issues.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"{project}")


# --- EDUCATION
st.write('\n')
st.subheader( "**EDUCATION**")

st.write(
"""
2010/3-2012/4	Academy of Information Technology Australia 

***Diploma: Arts & Design***

2010/3-2012/4	Academy of Information Technology Australia

***Diploma: Arts & Technology of Film and Television***

2010/3-2012/4	Academy of Information Technology Australia

***Diploma: Economic Management***
"""    
)
