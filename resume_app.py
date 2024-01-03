from pathlib import Path
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "Kristine_Rodel_CV.pdf"

#PAGE CONFIG
st.set_page_config(
    page_title = 'CV: Kristine Jane Rodel',
    page_icon = '👩‍💻',
)
#LOAD LOTTIE FOR ANIMATION
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
            return None
    return r.json()
#LOTTIE ASSETS
skills_anime = load_lottieurl('https://lottie.host/1eecd6a7-4118-40f3-a505-fcc0ce6ce213/UEq8E8mabd.json')

#WEBPAGE CSS
def css(file_name):
     with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
css("style/style.css")

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#LOAD IMAGES HERE
img_list = [
     'images/display_picture.png',
     'images/certificates/Cert1.png',
     'images/certificates/Cert2.png',
     'images/certificates/Cert3.png',
     'images/certificates/Cert4.png',
     'images/certificates/Cert5.png',
     'images/certificates/Cert6.png',
     'images/certificates/Badge1.png',
     'images/certificates/Badge2.png'
]

# HOME SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(img_list[0], width=345)

with col2:
    st.header("Kristine Jane Rodel")
    st.write('Bachelor of Science in Computer Engineering')
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(
         """
- 📫 kristinejrodel@gmail.com
- 📞 (+63)9063458583
- 🌐 Facebook: [Kristine Jane Rodel](https://web.facebook.com/kwistin18)
- 🌐 Instagram: [@kristn.jane](https://www.instagram.com/kristn.jane?igsh=Mzg1d3o4MDVnNmUy)
"""
    )
    col1inside, col2inside = st.columns(2)
    with col1inside:
         st.image(img_list[7], width=120)
    with col2inside:
         st.image(img_list[8], width=120)

select = option_menu(
    menu_title = None,
    options = ['Skills', 'Experiences', 'Certificates'],
    icons = ['activity', 'book', 'patch-check'],
    default_index = 0,
    orientation = 'horizontal',
)

if select == 'Skills':
          st.write('---')
     st.header('Soft Skills')
     col1, col2 = st.columns(2, gap="small")
     with col1:
          st.write(
          """
- ✅ Multi-tasking Capability
- ✅ Adaptable to New Environments
- ✅ Efficient in Fast-Paced Environments
- ✅ Able to learn at any new task assigned
- ✅ Pressure Resilience and High Standards

"""
)
     with col2:
          st.empty()

     st.write('---')
     st.header('Hard Skills')
     col1, col2 = st.columns(2, gap="small")
     with col1:
          st.write(
          """
- 👩‍💻 Entry-Level Programmer
- 📅 Mid-Level Data Entry Specialist
- ⚙️ Mid-Level Inventory Management Specialist
- 📄 Proficiency in MS Office (Word, Excel, PowerPoint, & Outlook)

"""
)
     with col2:
          st_lottie(skills_anime, height=200, key='Skills')

if select == 'Experiences':
     st.header('Experiences')
     st.write('---')
     st.subheader('Intern | Puerto Princesa City Water District')
     st.write(
          """
April 2023 - June 2023
- 🟢 **Inventory Management Specialist**: Conducts thorough physical counts to assess remaining stock levels. Proficient in executing the issuance, recording, and receiving processes for outgoing tools and materials.
- 🟢 **Data Entry Specialist**: Inputting and documenting all of the items that come in and go out of the PPC Water District Warehouse into the database.
"""
     )
     st.subheader("Service Crew | Three A's Restaurant")
     st.write(
          """
September 2023 - October 2023
- 🟢 **Service Staff**: Collaborate with kitchen and serving staff to coordinate order fulfillment and address any customer concerns promptly. Monitor and replenish supplies in dining areas, including condiments, utensils, and napkins. Assist in maintaining cleanliness and hygiene standards in the dining area, ensuring a pleasant atmosphere for guests.
"""
     )
     st.subheader('Intern | Department of Information and Communications Technology (DICT) - The Department of Labor and Employment (DOLE)')
     st.write(
          """
October 2023 - Present
- 🟢 **Office Support Staff**: Provide support to the office by performing various administrative tasks, such as handling phone calls, managing schedules, organizing documents, and assisting with general office operations.
- 🟢 **Media Specialist**: Taking photos and videos content to document the proceedings throughout the seminar or training session, ensuring a comprehensive record of the event's activities.
- 🟢 **Entry-Level Programming Associates**: Handling basic programming, understanding the basic programming languages, testing, and debugging code under the guidance of more experienced developers or team leads.
"""
     )

if select == 'Certificates':
     st.header('Certificates')
     st.write('---')
#Certificate 1
     st.subheader('Decode 2021')
     st.write(
          """
In the year 2021, I attended a seminar on how to protect and defend our own data in the cyber society.
"""
     )
     st.image(img_list[1], caption='Decode 2021 - Cyber Defense Society')
     st.write('##')

#Certificate 2
     st.subheader('Decode 2021: Get it Girl')
     st.write(
          """
Discusses the state of the cybersecurity skills gap and how it has improved as a result of diversity and inclusion.
"""
     )
     st.image(img_list[2], caption='Decode 2021 - Women Work: How Women Stand Out')
     st.write('##')

#Certificate 3
     st.subheader('PPS Innovations Inc. | PUGAD')
     st.write(
          """
On July 28, 2022, I attended the seminar "Electronics Use in Medical Devices" at Ka Inato, San Manuel, Puerto Princesa City, Palawan.
"""
     )
     st.image(img_list[3], caption='PPS Innovations Inc. | PUGAD - Electronics Use in Medical Devices')
     st.write('##')

#Certificate 4
     st.subheader('DICT | Digital Mastery Unleashed')
     st.write(
          """
A training program centered around digital mastery took place on November 14-15, 2023, at the DICT Palawan Provincial Tech4ED Center.
"""
     )
     st.image(img_list[4], caption='Digital Mastery Unleashed - Exploring Advanced IT Concepts and Skills')
     st.write('##')

#Certificate 6
     st.subheader('CISCO | Cisco Networking Academy')
     st.write(
          """
A training program offered by Department of Information and Communications Technology (DICT) focuses about the Introduction to Cybersecurity.
"""
     )
     st.image(img_list[6], caption='CISCO - Introduction to Cybersecurity')
     st.write('##')

#Certificate 5
     st.subheader('CISCO | Cisco Networking Academy')
     st.write(
          """
A training program offered by Department of Information and Communications Technology (DICT) focuses about the Cybersecurity Essentials.
"""
     )
     st.image(img_list[5], caption='CISCO - Cybersecurity Essentials')
     st.write('##')