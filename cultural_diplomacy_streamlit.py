
import streamlit as st

# ---- TITLE ----
st.title("🌍 Cultural Diplomacy Bot: Egypt & MENA Edition")

# ---- INTRO ----
st.markdown("""
<div style="font-size:20px; line-height:1.6; text-align:justify;">
🇪🇬 من أم الدنيا، إلى كل ركن من أركان الوطن العربي... أهلاً بيك.<br><br>

Egypt has always been more than a place — she's <em>om el-dunya</em>, the mother of the world, the storyteller of the region. Her voice is familiar to all; her wit, unmistakable.<br><br>

Generations across the Arab world grew up with her cinema, studied in her universities, sang her songs, and fell a little in love with her charm.<br><br>

Here, we celebrate how every country in MENA has left its mark on Egypt — and how Egypt has quietly left hers too.<br><br>

Whether it's food, language, festivals or love stories, we're more connected than we think.<br><br>

🧭 Choose a country below to explore the thread that ties it to Cairo’s heart — and yours.
</div>
""", unsafe_allow_html=True)

# ---- COUNTRY SELECTION ----
countries= ["🇩🇿 الجزائر — Algeria", "🇧🇭 البحرين — Bahrain", "🇮🇶 العراق — Iraq",
           "🇯🇴 الأردن — Jordan", "🇰🇼 الكويت — Kuwait", "🇱🇧 لبنان — Lebanon", "🇱🇾 ليبيا — Libya", "🇲🇷 موريتانيا — Mauritania",
           "🇲🇦 المغرب — Morocco", "🇴🇲 عُمان — Oman", "🇵🇸 فلسطين — Palestine", "🇶🇦 قطر — Qatar", "🇸🇦 السعودية — Saudi Arabia","🇸🇩 السودان — Sudan", "🇹🇳 تونس — Tunisia", "🇦🇪 الإمارات — UAE", "🇸🇾 سوريا    — Syria"
           ]


st.subheader("🌍 اختر الدولة (Choose the country to connect Egypt with)")
country = st.selectbox("Country", countries)
country_cleaned = country.split("—")[-1].strip()


st.markdown("""
<div style="font-size:20px; line-height:1.6;">
🎭 .... من رهافة فيروز في الصباح، لقوة أم كلثوم المخملية في المساء<br>
Love, pride, and connection have many voices. Some declare, some explain, some tease.<br><br>
Choose how you’d like Egypt to speak today — and don’t be shy to come back and hear her say it differently next time.
</div>
""", unsafe_allow_html=True)

# ---- TONES ----
tones = [
    ("🧑‍⚖️ Formal", "Tone 1: Formal – Like a polished diplomat at a summit", "#164187"),
    ("🎓 Academic", "Tone 2: Academic – Footnotes optional, depth guaranteed", "#174512"),
    ("🍵 Warm & Personal", "Tone 3: Warm – Like an aunt over tea", "#9C6A0E"),
    ("💌 Cheeky and Fun", "Tone 4: Flirty – Respectful, playful, charming", "#852E1C")
]

st.subheader("🧭 اختر نكهة التواصل (Select the tone)")
tone_col1, tone_col2 = st.columns(2)
selected_tone = None

# Store selected tone in session state
if "selected_tone" not in st.session_state:
    st.session_state["selected_tone"] = None

for i, (tone_name, tooltip, color) in enumerate(tones):
    with (tone_col1 if i % 2 == 0 else tone_col2):
        if st.button(tone_name, help=tooltip, key=tone_name):
            st.session_state["selected_tone"] = tone_name

selected_tone = st.session_state["selected_tone"]




# ---- TRIGGER GENERATION ----
st.subheader("📝 Output")

st.button("🔮 Generate Cultural Link") 


# ---- MOCK RESPONSES ----
mock_responses = {
  ("Morocco", "🍵 Warm & Personal"): """<div style="background-color:#fef3dd; color:#2d2d2d; padding:20px; border-radius:10px; font-size:17px; line-height:1.9; text-align:justify; font-family:'Segoe UI', sans-serif;">
<b>“عارفة لما زرت المغرب، حسيت إني رايحة جارتنا اللي بيوتها بتشبه بيوتنا.”</b><br><br>

Back in the early 80s, Moroccan students flooded Cairo’s bustling universities, bringing with them their vibrant culture and, of course, their beautiful traditional garments. The Moroccan caftan, with its intricate embroidery and luxurious fabrics, caught the eye of Egyptian designers who couldn’t resist incorporating its elegance into their creations. Egyptian fashion shows in the famous Heliopolis Club started featuring these stunning designs, and before long, it wasn’t unusual to see Egyptian brides wearing caftans at their wedding celebrations.<br><br>

<i>مرة شفت بنت مصرية في فرح صديقتها لابسة قفطان مغربي، وكانت بتقول:<br>
“دا مش بس فستان… دا حكاية من بلاد الحجايات”</i><br><br>

Meanwhile, somewhere in Casablanca, Egyptian movies were being screened in cozy salons, and young Moroccans began mimicking the Egyptian dialect they’d hear on screen.<br><br>

<i>“كل ما أسمعهم يقولوا: ‘إيه يا عم إنت’، أضحك وأقول: دي لهجتنا الجديدة”</i><br><br>

And just like that, a cross-cultural fashion exchange blossomed. An Egyptian designer once said:<br>
<i>“القفاطين مش مجرد أزياء… دي جسر بين الحكايات”</i><br><br>

And in a cozy café in Giza, a Moroccan friend confided:<br>
<i>“لما لبست جلابة مصرية، حسيتني لافسة كلمة بحبك”</i><br><br>

From Cairo’s catwalks to Casablanca’s cinemas, the Moroccan caftan has become an emblem of shared beauty and elegance, illustrating a tale that ties us in more ways than one.<br><br>

<b>من قماش القفطان لحكايات المقاهي، مصر والمغرب مش بس جيران… إحنا أهل بنحكي سوا.</b>
</div>""",

    ("Palestine", "🎓 Academic"): """<div style="background-color:#fef3dd; color:#2d2d2d; padding:20px; border-radius:10px; font-size:17px; line-height:1.9; text-align:justify; font-family:'Segoe UI', sans-serif;">
<b>🧠 “الروابط الثقافية بين مصر وفلسطين مش مجرد تاريخ، دي كمان جغرافيا فنية.”</b><br><br>

The artistic collaboration between Egypt and Palestine has long served as a cultural beacon, illuminating shared struggles and aspirations through cinema and poetry. Egyptian cinema, particularly in the mid-20th century, provided an influential platform for Palestinian narratives. The film “The Dupes” (المخدوعون), directed by the Egyptian filmmaker Tewfik Saleh in 1972, is a renowned example. This film, based on the novel “Men in the Sun” by Palestinian author Ghassan Kanafani, poignantly explores the plight of Palestinian refugees. The collaboration was not just cinematic; it was a profound statement of solidarity — an artistic interweaving of Egyptian directorial prowess with Palestinian storytelling.<br><br>

<i>“الفيلم دا مش مجرد عمل سينمائي، دا صرخة ضد الظلم”</i><br><br>

Ghassan Kanafani’s works found resonance in Egyptian cultural discourse, becoming a staple in academic settings and public discussions. The film’s critical acclaim and enduring impact are evident in its continued study within Arab universities, highlighting its role as a cultural artifact that transcends borders.<br><br>

<i>“الطلاب كانوا يقولوا: كل مشهد من الفيلم دا بيحكي وجع كل لاجئ فلسطيني”</i><br><br>

In 1975, screenings of “The Dupes” across Egyptian cultural centers sparked discussions that bridged national divides, merging Egyptian patriotism with Palestinian resistance.<br><br>

<i>“في كل عرض، كنا كأننا بنشهد ميلاد وعي جديد”</i><br><br>

This fusion of Egyptian cinematic skill and Palestinian narrative depth underscores the enduring cultural symbiosis between the two nations. Through their shared creative endeavors, Egypt and Palestine have continuously reaffirmed their kinship, uniting audiences in empathy and action.<br><br>

<b>من دور العرض المصرية، كانت فلسطين دايمًا حاضرة بالقصة والصورة.</b><br>
<i>From Egyptian cinema screens, Palestine was always present in story and image.</i>
</div>""",

    ("Lebanon", "🎓 Academic"): """<div style="background-color:#fef3dd; color:#2d2d2d; padding:20px; border-radius:10px; font-size:17px; line-height:1.9; text-align:justify; font-family:'Segoe UI', sans-serif;">
<b>🎨 “فن الخط العربي: جسر بين القاهرة وبيروت.”</b><br><br>

The art of Arabic calligraphy has long been more than mere decoration; it is a profound medium of cultural expression and political significance. During the late 20th century, Egypt and Lebanon became pivotal centers for the revival and evolution of this intricate art form. In the 1970s, the Lebanese civil war drove many artists, including calligraphers, to seek refuge in Cairo, where their artistry found new audiences and contexts.<br><br>

<b>الخطاط اللبناني كمال بلاطه</b>، الذي اضطر للرحيل عن بيروت، أقام معرضًا مشتركًا في القاهرة عام 1985 مع الفنان المصري <b>حامد عويس</b>. كان المعرض يحمل عنوان “نقطة، خط، مسار”، حيث مزج بين التقاليد والخبرات الجديدة المكتسبة في مصر.<br><br>

In Cairo, calligraphy workshops began to include Lebanese techniques and motifs, echoing the cultural symbiosis between the two nations. Egyptian calligraphers like <b>Ahmed Moustafa</b> drew inspiration from Lebanese peers, creating works that celebrated a broader Arab identity.<br><br>

The 1990s saw Lebanese calligraphy further influencing Egyptian advertising and graphic design, with Lebanese artists contributing to urban art installations across Cairo. This artistic exchange wasn’t just a matter of aesthetics; it was a dialogue about identity and resistance, with calligraphy serving as a canvas for political expression through pieces that celebrated unity and resilience.<br><br>

<i>“كلمة واحدة كتبت بالخط العربي كانت ترتجف وتنبض كأنها نبض قلب مشترك بين مصر ولبنان.”</i><br><br>

Such collaborative efforts in calligraphy not only enriched the artistic language of both countries but also highlighted the profound connectivity of their cultural heritage.<br><br>

<b>من بيروت للقاهرة، الحروف حكاية حضارية.</b><br>
<i>From Beirut to Cairo, letters tell a story of civilization.</i>
</div>""",
("Algeria", "🧿 Formal"): """<div style="background-color:#f9f9f9; color:#222222; padding:20px; border-radius:10px; font-size:17px; line-height:1.9; text-align:justify; font-family:'Segoe UI', sans-serif;">
<b>🎬 “هل كنتم تعلمون أن جسر السينما كان يعبر فوق البحر ليصل الجزائر بمصر؟”</b><br><br>

In the mid-20th century, during Algeria’s struggle for independence, a profound cultural connection was forged between Egypt and Algeria through the medium of cinema. Egyptian filmmakers provided a cinematic voice that echoed across the Mediterranean. In 1962, just as Algeria gained its independence, Egyptian director <b>Youssef Chahine</b> offered his expertise to train Algerian filmmakers in Cairo, recognizing the power of film in shaping national identity. This collaboration was not merely artistic; it was a political statement of unity.<br><br>

Algerian director <b>Mohammed Lakhdar-Hamina</b>, influenced by Chahine, later crafted award-winning films that portrayed Algeria’s fight for freedom with Egyptian cinematic techniques. In 1975, Lakhdar-Hamina’s “Chronicle of the Years of Fire” won the Palme d’Or at Cannes, hailed by Egyptian critics as a triumph shared across borders. An Egyptian filmmaker once remarked:<br><br>

<i>“لما عملنا أفلامنا مع إخوتنا الجزائريين، كنا بنصنع التاريخ معًا.”</i><br><br>

Similarly, Egyptian actors found audiences in Algiers eager to see their familiar faces on screen, leading to joint film festivals that celebrated shared narratives of resilience. This cinematic bridge reinforced a mutual recognition of the arts as a powerful tool for cultural and political solidarity.<br><br>

<b>عبر الفن السابع وقيوده، كانت السينما هي لغة الوحدة بين الأشقاء.</b><br>
<i>Through the seventh art and its boundaries, cinema was the language of unity between brothers.</i>
</div>""",


}
# ---- DISPLAY MOCK OUTPUT IF MATCH FOUND ----
if country_cleaned and selected_tone:
    mock = mock_responses.get((country_cleaned, selected_tone))
    if mock:
        st.markdown(mock, unsafe_allow_html=True)
    else:
        st.info("No mock response available yet for this combo. Try another!")
