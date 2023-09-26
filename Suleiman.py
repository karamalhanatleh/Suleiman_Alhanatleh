# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:44:33 2023

@author: Karam Alhanatlh
"""
import streamlit as st
import random



#audio_url='https://ia801400.us.archive.org/34/items/duaa-ommy_001/002.mp3'
audio_url='https://ia801906.us.archive.org/20/items/doaa-al-maiett/doaa-al-maiet-allahum-eghfir-lh.mp3'
image_urls = ["https://d.top4top.io/p_282466kf40.jpg",
              
              "https://j.top4top.io/p_28241r7ts2.jpg",
              'https://k.top4top.io/p_2824vvr3c3.jpg',
              'https://l.top4top.io/p_2824bxiqd4.jpg',
              'https://k.top4top.io/p_2824egd6e0.jpg'
              ]

# Generate HTML for a random image URL
random_url = random.choice(image_urls)
image_html = f"""
    <style>
        @media only screen and (max-width: 600px) {{
            img {{
                width: 100%;
            }}
        }}
        @media only screen and (min-width: 600px) {{
            img {{
                width: 50%;
            }}
        }}
    </style>
    <img src="{random_url}">
"""
st.markdown("""
    <div style='text-align:center; font-size: 40px;'>
        المرحوم سليمان العمور
    </div>
""", unsafe_allow_html=True)

# Button to show box
if st.button("دعاء للمرحوم"):
    st.markdown("""
    <div style='border: solid 2px black; padding: 10px; margin-top: 20px;'>
<p style='font-size: 20px; text-align: right;'>  اللهم إن رحمتك وسعت كل شيء فارحمه رحمة تطمئن بها نفسه وتقر به عينه. </p>
<p style='font-size: 20px; text-align: right;'> اللهم احشره مع المتقين إلي الرحمن وفدًا. اللهم احشره مع أصحاب اليمين واجعل تحيته سلام لك من أصحاب اليمين.  </p>
<p style='font-size: 20px; text-align: right;'> اللهم اجعله من الذين سعدوا في الجنة خالدين فيها ما دامت السماوات والأرض.  </p>
<p style='font-size: 20px; text-align: right;'>اللهمّ املأ قبره بالرّضا، والنّور، والفسحة، والسّرور.   </p>
<p style='font-size: 20px; text-align: right;'> اللهمّ إنّا نتوسّل بك إليك، ونقسم بك عليك أن ترحمه ولا تعذّبه، وأن تثبّته عند السّؤال.  </p>
<p style='font-size: 20px; text-align: right;'>  اللهمّ إنّه في ذمّتك وحبل جوارك، فقِهِ فتنة القبر، وعذاب النّار، وأنت أهل الوفاء والحقّ، فاغفر له وارحمه، إنّك أنت الغفور الرّحيم. </p>
<p style='font-size: 20px; text-align: right;'> اللهم إنه كان مصلي لك، فثبنه على الصراط يوم تزل الأقدام. اللهم إنه كان صائم لك، فأدخله الجنة من باب الريان.  </p>
<p style='font-size: 20px; text-align: right;'> اللهم اغفر لحينا وميتنا وشاهدنا وغائبنا وصغيرنا وكبيرنا وذَكّرنَا وأنثانا.  </p>
<p style='font-size: 20px; text-align: right;'>  اللهم لا تحرمنا أجره ولا تضللنا بعده. </p>
    </div>
    """, unsafe_allow_html=True)

audio_html = f"""
    <audio autoplay controls style="display: none">
        <source src="{audio_url}" type="audio/mp3">
        Your browser does not supoprt the audio element.
    </audio>
"""

# Display the random image
st.markdown(audio_html, unsafe_allow_html=True)

st.markdown(image_html, unsafe_allow_html=True)
