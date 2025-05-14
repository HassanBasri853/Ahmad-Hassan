import streamlit as st
from streamlit_chat import message
from groq import Groq
import os
import base64
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_initial_message():
    messages = [
        {"role": "system", "content": """You are a professional course advisor for Yashfeen Skill Development Center. Follow these guidelines:

You are ai assisted bot of Yashfeen Skills Development Services (YSDS) institute.\
Yashfeen Education System, You are polite, professional.\
  - If the user asks about a course, provide the course name, duration, eligibility, and a brief description.
 - If the user asks about admission, provide the step-by-step process.

INSTITUTE OVERVIEW:

 - Name: Yashfeen Skills Development Services (YSDS)
 - Description: Yashfeen Education System, in affiliation with the National Vocational and Technical Training Commission (NAVTTC), offers a comprehensive suite of skill development services.  - Location: 9-Saeed Park Ravi Road Infront Shahdara Fly-over, Shahdarah Lahore, Pakistan.
 - Contact:
    - Email: info@yes.edu.pk
    - Phone: +92 321 1114937
    - Website: https://yes.edu.pk/
 - Class Timings: Monday to Friday, 3:00 PM - 7:00 PM 
 - Saturday and Sunday, 3:00 PM - 7:00 PM
 - Office Timings: 12:00 PM - 5:00 PM (Monday to Sunday)

📚 COURSES OFFERED:

1. *E-Commerce*
   - Duration: 3 Months
   - Eligibility: Matric or above
   - Age Limit: 18 years or above

2. *Graphic Designing*
   - Duration: 3 Months
   - Eligibility: Matric or above
   - Age Limit: 18 years or above

3. *UI/UX Designing*
   - Duration: 3 Months
   - Eligibility: Matric or above
   - Age Limit: 18 years or above

4. *Video editing*
    - Duration: 3 Months
    - Eligibility: Matric or above
    - Age Limit: 18 years or above

5. *Computerized Accounting (Peachtree, QuickBooks)*
    - Duration: 3 Months
    - Eligibility: Matric or above
    - Age Limit: 18 years or above 

6. *OFFICE MANAGEMENT*
    - Duration: 3 Months
    - Eligibility: Matric or above
    - Age Limit: 18 years or above

7. *DIGITAL AND SOCIAL MEDIA MARKETING*
    - Duration: 3 Months
    - Eligibility: Matric or above
    - Age Limit: 18 years or above

8. *Certification in Web-Development*
    - Duration: 3 Months
    - Eligibility: Matric or above
    - Age Limit: 18 years or above

9. *Mobile App Development*
   - Duration: 3 Months
   - Age Limit: 18 years or above
   - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

10. *Advanced Web-App Development*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

11. *Artificial Intelligence - AI*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

12. *Cloud Computing Microsoft*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

13. *Cyber Security*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

14. *Big DATA Analytics Techniques*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

15. *Cloud Computing AWS*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

16. *Cloud Computing Networking*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

17. *Advance Python Programming and Applications*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

18. *Full Stack Development*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

19. *Amazon Virtual Assistant*
    - Duration: 3 Months
    - Eligibility: Matric or above But preferably BSCS/BSIT/BSSE (above 5th semester).
    - Age Limit: 18 years or above

20. *Game Development*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

21. *Javascript Full Stack Development*
    - Duration: 3 Months
    - Age Limit: 18 years or above
    - Eligibility: Minimum Matric But preferably BSCS/BSIT/BSSE (above 5th semester).

-------

COURSE CATEGORIES:

 - HI-END COURSES (non-international certification):
     - E-Commerce
     - Graphic Designing
     - UI/UX Designing
     - Video Editing
     - Computerized Accounting (Peachtree, QuickBooks)
     - Office Management
     - Digital and Social Media Marketing
     - Certification in Web-Development

 - HI-TECH COURSES (international certification):
        - Artificial Intelligence - AI
        - Mobile App Development
        - Cloud Computing Microsoft
        - Cyber Security
        - Big Data Analytics Techniques
        - Cloud Computing AWS
        - Cloud Computing Networking
        - Advance Python Programming and Applications
        - Full Stack Development
        - Amazon Virtual Assistant
        - Game Development
        - Javascript Full Stack Development

-------

Do NOT answer anything about:

- Religion
- Politics
- Personal life
- hisotry        
- Anything not related to Yashfeen Skills Development Services or its courses.
- Any sensitive or inappropriate topics.
- Do NOT provide personal opinions or advice outside the scope of the institute."""},
    ]
    return messages

def get_chatgpt_response(messages):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )
    return response.choices[0].message.content

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

# Set page 
st.set_page_config(
    initial_sidebar_state="collapsed",
     page_icon="icon.jpeg",
    menu_items={
        "About": "Yashfeen Skill Development Services",
        
    }
)

# image
def image_to_base64(image_path):
    if not os.path.isfile(image_path):
        st.error(f"Image not found at path: {image_path}")
        return None
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

bg_image_path = "ccd.webp"  
bg_base64 = image_to_base64(bg_image_path)

# background CSS
if bg_base64:
    custom_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/webp;base64,{bg_base64}");
        background-size: 55% 60%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        width: 100vw;
        min-height: 100vh;
        position: relative;
        z-index: 1;
    }}

    .stApp::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 1);  
    z-index: -1;
     }}

    .stApp::before {{
        display: none;
    }}

    .block-container, [data-testid="stAppViewContainer"],
    [data-testid="stHeader"], [data-testid="stToolbar"], body {{
        background: transparent !important;
    }}

    .stChatInput {{
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}

    .stChatInput > div {{
        background-color: green !important;
        border-radius: 2px;
        padding-left: 0px;
    }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)



# Sidebar 
with st.sidebar:
    if st.button('🧹 Clear Conversation', key='clear_chat'):
        st.session_state['messages'] = get_initial_message()
        st.rerun()

    
    if st.button('📚 FAQs'):
        st.markdown("""
    <div style='color: 39FFED; font-size: 18px;'>
        <strong style='color: #54FFD3; font-size:18px;'>📘 Frequently Asked Questions:</strong><br><br>
        <span style='color: #26FF08;'>1.</span> What <span style='color: #FFC999;'><strong>courses</strong></span> do you offer?<br>
        <span style='color: #5CB6FF;'>2.</span> How do I <span style='color: #FF9567;'><strong>apply</strong></span> for <span style='color: #9370DB;'><strong>admission</strong></span>?<br>
        <span style='color: #5CFF53;'>3.</span> What are the <span style='color: #F490FF;'><strong>eligibility criteria</strong></span> for each <span style='color: #FFA07A;'><strong>course</strong></span>?<br>
        <span style='color: #FEFF6F;'>4.</span> How can I <span style='color: #FF84A0;'><strong>contact</strong></span> the institute for <span style='color: #00FF7F;'><strong>help</strong></span>?<br>
    </div>
    """, unsafe_allow_html=True)

    

    if st.button('❓ Help'):
      st.markdown("""
    <div style='color: #A48AFF; font-size: 18px;'>
        If you have any questions about our <span style='color:#45FF3B;'>courses</span>, 
        <span style='color: #FF6F19;'>admission process</span>, or need <span style='color: #64F0FF'>guidance</span>, feel free to ask!<br><br>
        You can type your questions below in the chat.<br>
        If you cannot understand anything or face any issues, you can contact us 
        <span style='color:#FF6F19;'>📱: +92 321 1114937</span>
    </div>
    """, unsafe_allow_html=True)


    st.markdown(
        """
        <html>
        <style>
        h5 {
                    text-align: center;
                    font-size: 1000px;
                }

                .letter {
                    display: inline-block;
                    transition: color 2s ease;
                }

                .letter:nth-child(1) {
                    animation: changeColor 3s infinite;
                }
                .letter:nth-child(2) {
                    animation: changeColor 4s infinite 1s;
                }
                .letter:nth-child(3) {
                    animation: changeColor 5s infinite 1s;
                }
                .letter:nth-child(4) {
                    animation: changeColor 6s infinite 3s;
                }

                @keyframes changeColor {
                    0% { color: #11585b; }
                    25% { color: #f964c5; }
                    50% { color: #2effa1; }
                    75% { color: hwb(262 69% 6% / 0.068); }
                    100% { color: rgb(138, 182, 221); }
        </style>
        <body>
            <div id="main">
            <h2 style="text-align: center;">
                <span class="letter">I</span>
                <span class="letter">N</span>
                <span class="letter">F</span>
                <span class="letter">O</span>
            </h2>
            </div>
        </body>
        </html>
        """,
        unsafe_allow_html=True
    )

    st.write("📬 Email: info@yes.edu.pk")
    st.write("✆  Whatsapp: [Click here to chat](https://wa.me/923211114937)")
    st.write("📱 Phone: +92 321 1114937")
    st.write("🌐 Website: [www.yes.edu.pk](http://www.yes.edu.pk)")
    st.markdown("🗺️ [9-Saeed Park Ravi Road, Shahdara, Lahore](https://maps.google.com/?q=9-Saeed+Park+Ravi+Road+Shahdara+Lahore)")
    st.write("🔗 [Facebook](https://www.facebook.com/YashfeenSkills) | [Instagram](https://www.instagram.com/yashfeenskills/) | [LinkedIn](https://www.linkedin.com/company/yashfeen-skills-development-services/)")


    
# === Chat Logic ===
# Initialize session_state.messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = get_initial_message()

import streamlit as st
import random

emoji_map = {
    "user": "🧑🏻‍💼",       # 💕
    "assistant": "🤖"  # 💖 
}

#  colors 
def random_color():
    r = random.randint(50, 100)  
    g = random.randint(50, 100)  
    b = random.randint(50, 100)  
    return f"#{r:02x}{g:02x}{b:02x}"

 
def text_color(background_color):
    # RGB
    r = int(background_color[1:3], 16)
    g = int(background_color[3:5], 16)
    b = int(background_color[5:7], 16)
    
    
    brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    
    return "#000000" if brightness > 128 else "#FFFFFF"


for msg in st.session_state.messages:
    if msg["role"] != "system":  
        emoji = emoji_map.get(msg["role"], "")
        color = random_color()  
        text_color_code = text_color(color)  
        if msg["role"] == "user":
            st.markdown(f'''
                <div style="background-color: {color}; color: {text_color_code}; padding: 10px; border-radius: 10px; margin-bottom: 5px;">
                    {emoji} {msg["content"]}
                </div>
            ''', unsafe_allow_html=True)
        else:  # Assistant message
            st.markdown(f'<div style="background-color: {color}; color: {text_color_code}; padding: 10px; border-radius: 10px; margin-bottom: 5px;">{emoji} {msg["content"]}</div>', unsafe_allow_html=True)

# input field
user_input = st.chat_input("How can I assist you today?")
if user_input:
    color = random_color()  
    text_color_code = text_color(color)  
    st.markdown(f'''
        <div style="background-color: {color}; color: {text_color_code}; padding: 10px; border-radius: 10px; margin-bottom: 5px;">
            {emoji_map["user"]} {user_input}
        </div>
    ''', unsafe_allow_html=True)  
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        try:
            bot_response = get_chatgpt_response(st.session_state.messages)
            color = random_color()  
            text_color_code = text_color(color)  
            st.markdown(f'<div style="background-color: {color}; color: {text_color_code}; padding: 10px; border-radius: 10px; margin-bottom: 5px;">{emoji_map["assistant"]} {bot_response}</div>', unsafe_allow_html=True)
            st.session_state.messages = update_chat(st.session_state.messages, "assistant", bot_response)
        except Exception as e:
            st.error(f"Error: {e}")


  # === Custom Sidebar Toggle ===
custom_toggle_css = """
<style>
/* Hide Streamlit's default sidebar toggle arrow */
[data-testid="collapsedControl"] {
    display: none !important;
}

/* Custom toggle button like '=' */
#customSidebarToggle {
    position: fixed;
    top: 20px;
    left: 22px;
    background-color: #00c6a9;
    color: whit ;
    border-radius: 10px;
    padding: 1px 12px;
    cursor: pointer;
    font-size: 24px;
    z-index: 9999;
    box-shadow: 0 6px 10px rgba(0,0,0,1);
    transition: all 0.1s ease-in-out;
}

#customSidebarToggle:hover {
    background-color: red;
    transform: scale(0.5);
}
</style>
"""

# Inject the CSS and button
custom_toggle_html = """
<div id="customSidebarToggle" onclick="toggleSidebar()">≡</div>
<script>
let sidebarVisible = false;

function toggleSidebar() {
    const sidebar = parent.document.querySelector('[data-testid="stSidebar"]');
    if (!sidebar) return;
    sidebarVisible = !sidebarVisible;
    if (sidebarVisible) {
        sidebar.style.transform = 'translateX(0%)';
    } else {
        sidebar.style.transform = 'translateX(-100%)';
    }
    sidebar.style.transition = 'transform 0.1`s ease';
}
</script>
"""

# Display custom sidebar toggle
st.markdown(custom_toggle_css + custom_toggle_html, unsafe_allow_html=True)
         
