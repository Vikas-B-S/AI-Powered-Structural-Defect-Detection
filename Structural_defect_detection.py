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
st.title('STRUCTURAL DEFECTS: :grey[AI assisted structural defect identifier in construction buisness]')

# Tips
tips = '''
To use this AI-assisted structural defect identifier application, follow these steps:

1. Upload a clear image of the structure you want to analyze.
2. Fill in the report details: title, prepared by, and prepared for.
3. Click the "Generate Report" button to analyze the image and produce a detailed structural defect report.
4. Once generated, review the report on-screen and download it for documentation.

The report will provide:
- Classification of structural defects (e.g., cracking, corrosion, honeycombing, etc.)
- Severity assessment (low, medium, high) and avoidable vs inevitable defects
- Estimated time before permanent damage occurs
- Short-term and long-term remediation solutions with cost and time estimates
- Precautionary measures to prevent future defects
'''

st.write(tips)
rep_title=st.text_input('Report Title:',None)
prep_by=st.text_input('Report Prepared By:',None)
prep_for=st.text_input('Report Prepared for:',None)


prompt = f'''
You are an expert structural engineer and AI assistant. The user has provided an image of a structure.
Your task is to generate a comprehensive report based on the image.

The report should include:

1. **Report Details**:
   - Title: {rep_title}
   - Prepared By: {prep_by}
   - Prepared For: {prep_for}
   - Date: {dt.datetime.now().date()}

2. **Defect Identification**:
   - Identify all defects in the image (e.g., cracking, corrosion, honeycombing, spalling, etc.)
   - Classify each defect separately
   - Assess severity (Low / Medium / High)
   - Indicate if the defect is avoidable or inevitable
   - Estimate time before permanent structural damage occurs

3. **Solutions and Recommendations**:
   - Short-term solution with estimated cost and implementation time
   - Long-term solution with estimated cost and implementation time
   - Precautionary measures to prevent recurrence

4. **Formatting Requirements**:
   - Use bullet points for clarity
   - Include tables where appropriate for easy understanding
   - Ensure the report is concise and does not exceed 3 pages

Generate a professional, actionable report suitable for construction project documentation.
'''

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