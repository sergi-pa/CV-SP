import requests
from pathlib import Path
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "3.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sergio Parra"
PAGE_ICON = ":wave:"
NAME = "Sergio Stiven Parra Solorzano"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "sergioparra782@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/spsol?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BcAbHFawxTUiNitK%2BmySQZQ%3D%3D",
    "GitHub": "https://github.com/sergi-pa",

}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


#---lottie_file ="https://lottie.host/9baf0a2f-76f7-457e-b867-bf63ae5003c3/wE2UE52wWJ.json"

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

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


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, Excel and R-Studio
- ✔️ Good understanding of statistical and their respective applications
"""
)


# --- SKILLS ---
st.write('\n')
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.subheader("Hard Skills")
        st.write(
            """
        - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
        - 📊 Data Visulization: PowerBi, MS Excel, Plotly,Tableau
        - 📚 Modeling: Logistic regression, linear regression, decition trees
        - 🗄️ Databases: Postgres and SQL_server
        """
        )
    #--with right_column:
       #---- st_lottie(load_lottieurl(lottie_file), height=250)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Cost Analyst| Colnotex S.A.S**")
st.write("06/2023 - Present")
st.write(
    """
- ► Implementation of ETL Strategies and Predictive Analysis for Cost Control: Developed and implemented an ETL (Extract, Transform, Load) process and applied inferential statistical analysis to optimize the product cost sheet system.
 This led to improved control of raw material costs, packaging supplies, labor, and overhead costs, resulting in a more accurate calculation of the real net margin.
- ► ▪ Optimization of Macros and Queries for Time Reduction: Improved the performance of macros and queries used for inventory valuation (Raw Materials, Work in Process, Finished Goods), reducing response times by 15% and 27%, respectively.
 This improvement enabled more agile processes and a significant increase in productivity when valuing inventories.
- ►▪ Optimization of the Overhead Cost System (Indirect Manufacturing Costs): Enhanced the calculation of overhead costs through mathematical modeling, which allowed for a more accurate allocation of indirect costs to the company's cost centers,
 resulting in a fairer and more efficient distribution of these costs.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "Improvement Manager | Colnotex S.A.S**")
st.write("03/2022 - 06/2023")
st.write(
    """
- ►  Optimization of Preventive Maintenance: I implemented a preventive maintenance plan for sewing machines, embroidery machines, and ultrasound equipment, which reduced unproductive time by 15%
    and improved the operational availability of the equipment, resulting in an 18% increase in production efficiency.
- ► Leadership in Lean Manufacturing and SMED: I coordinated the implementation of Lean Manufacturing methodology and the SMED (Single-Minute Exchange of Die) technique,
 achieving a 30% increase in the efficiency of embroidery and ultrasound machines by reducing machine changeover times and optimizing production processes.
- ► Automation and Improvement in Data Management: I led the automation of database management in the garment and quilting plant through Excel macros and Python,
 eliminating repetitive tasks and reducing data entry errors by 40%. Additionally, I improved data entry by 35%, increasing the reliability of the KPIs used for decision-making.
"""
)

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
