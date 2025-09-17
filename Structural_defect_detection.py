import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
import datetime as dt
from fpdf import FPDF
import io
import markdown2
from xhtml2pdf import pisa

#configure the model
key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-2.5-flash-lite')


st.sidebar.title(':orange[UPLOAD YOUR IMAGE HERE]')
uploaded_image=st.sidebar.file_uploader('Image',type=['jpeg','jpg','png'])
if uploaded_image:
    image=Image.open(uploaded_image)
    st.sidebar.subheader(':blue[UPLOADED IMAGE]')
    st.sidebar.image(image)

# create main page
st.markdown(
    "<h1 style='text-align: center; color:#2C3E50;'>AI-Powered Structural Defect Detection & Automated Reporting</h1>",
    unsafe_allow_html=True
)

tips = '''
### 📌 How to Use This Application

1. **Upload an Image**: Provide a clear photo of the structural element (e.g., beam, column, slab, wall).  
2. **Enter Report Details**: Add the report title, your name, and the recipient’s name.  
3. **Generate Report**: Click **"Generate Report"** to let the AI analyze the image and prepare a detailed engineering report.  
4. **Review & Download**: The report will be displayed on screen and can be downloaded as a PDF for project documentation.  

### 📝 What the Report Covers
- Types of defects (e.g., cracks, corrosion, spalling, honeycombing, etc.)  
- Severity assessment: **Low / Medium / High**  
- Classification: **Avoidable vs. Inevitable** defects  
- Estimated time before critical structural damage  
- Short-term and long-term repair strategies with **time & cost estimates**  
- Preventive recommendations to avoid recurrence  
'''

st.markdown(tips)

rep_title=st.text_input('Report Title:',None)
prep_by=st.text_input('Report Prepared By:',None)
prep_for=st.text_input('Report Prepared for:',None)


prompt = f"""
You are a professional structural engineer and AI assistant. The user has uploaded an image of a structural element.  
Your task is to generate a **clear, well-structured, and professional report** based on the image.

### Report Requirements

**1. Report Details**
- Title: {rep_title}
- Prepared By: {prep_by}
- Prepared For: {prep_for}
- Date: {dt.datetime.now().date()}

**2. Defect Identification**
- Detect and describe all visible defects (cracking, corrosion, honeycombing, spalling, surface wear, etc.)
- Classify each defect with a clear name and type
- Assess severity (**Low / Medium / High**)
- State whether the defect is **avoidable or inevitable**
- Provide an **estimated timeline** before permanent damage occurs

**3. Solutions & Recommendations**
- **Short-Term Solutions**: practical fixes with estimated **cost & implementation time**
- **Long-Term Solutions**: durable remediation with estimated **cost & implementation time**
- **Preventive Measures**: clear guidelines to minimize recurrence

**4. Formatting Guidelines**
- Use **headings, bullet points, and tables** where appropriate
- Keep report **professional and easy to follow**
- Ensure it is concise (≤ 3 pages) but sufficiently detailed for construction documentation
"""

if st.button('Generate Report'):
    if uploaded_image is None:
        st.error('Please upload an image first')
    else:
        with st.spinner('Generating report...'):
            response=model.generate_content([prompt,image],generation_config={'temperature':0.2})
            result=response.text
            st.write(result)

            result = result.replace("₹", "Rupees")

        # Convert Markdown text to HTML
        html = markdown2.markdown(result)

        # Convert HTML to PDF
        pdf_buffer = io.BytesIO()
        pisa.CreatePDF(html, dest=pdf_buffer)

        # Reset buffer position for Streamlit
        pdf_buffer.seek(0)

        # Streamlit download button
        st.download_button(
        label="Download Report as PDF",
        data=pdf_buffer,
        file_name="Structural_Defect_Report.pdf",
        mime="application/pdf"
        )