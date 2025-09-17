# AI-Powered Structural Defect Detection & Reporting System  

## 📖 Overview  
This project is an AI-assisted application that analyzes structural images (such as beams, columns, slabs, and walls) to identify potential defects and generate a **professional engineering report**.  

Built with **Streamlit**, **Google Gemini API**, and **Generative AI**, the system provides actionable insights into structural health and produces downloadable PDF reports for documentation.  

---

## 🚀 Features  
- 📤 **Upload structural images** (JPEG, JPG, PNG)  
- 🤖 **AI-based defect detection & classification** (cracks, corrosion, spalling, honeycombing, etc.)  
- 📊 **Severity assessment**: Low / Medium / High  
- 📅 **Estimated timeline** before permanent damage  
- 💡 **Short-term & long-term remediation** with time & cost estimates  
- 🛡️ **Preventive measures** to avoid recurrence  
- 📑 **Auto-generated PDF reports** (with tables, bullets & formatted text)  

---

## 🛠️ Tech Stack  
- **Python 3.9+**  
- [Streamlit](https://streamlit.io/) – interactive web UI  
- [Google Gemini API](https://ai.google.dev/) – generative AI for report generation  
- [Pillow](https://python-pillow.org/) – image processing  
- [FPDF / xhtml2pdf](https://pypi.org/project/xhtml2pdf/) – PDF generation  
- [Markdown2](https://github.com/trentm/python-markdown2) – markdown-to-HTML conversion  

---

## 📦 Installation  

1. **Clone this repository**  
```bash
git clone https://github.com/Vikas-B-S/AI-Powered-Structural-Defect-Detection.git
cd AI-Powered-Structural-Defect-Detection
```

2. **Create and activate virtual environment**  
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Set up API key**  
Get a Google Gemini API key and add it to your environment:  
```bash
export GOOGLE_API_KEY="your_api_key_here"   # Mac/Linux
set GOOGLE_API_KEY="your_api_key_here"      # Windows
```

---

## ▶️ Usage  

Run the Streamlit app:  
```bash
streamlit run Structural_defect_detection.py
```

Then:  
1. Upload a **structural image** from the sidebar  
2. Enter **report details** (title, prepared by, prepared for)  
3. Click **Generate Report**  
4. Review the AI-generated defect assessment on screen  
5. **Download the report as PDF**   


---

✨ With this project, structural engineers, construction teams, and inspectors can **save time, reduce risk, and document structural health efficiently**.  

