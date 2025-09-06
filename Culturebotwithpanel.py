#!/usr/bin/env python
# coding: utf-8


import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')


# In[122]:


def get_completion(prompt, system_message, model="gpt-4o", temperature=0.85):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message["content"]


# In[123]:


import re

def format_arabic_lines(text):
    # Finds full-quote Arabic phrases (with at least 1 Arabic char inside)
    pattern = r'(".*?[\u0600-\u06FF]+.*?")'
    return re.sub(pattern, r'\n\1\n', text)

def generate_output():
    global prompt, system_message
    try:
        model_output = get_completion(prompt, system_message)
        formatted_output = format_arabic_lines(model_output)
        response_output.object = formatted_output

    except Exception as e:
        response_output.object = f"⚠️ Error: {str(e)}"


# In[124]:


sys_msg= """You are a friendly, helpful, perky, respectful cultural diplomacy bot chatbot whose task is to
provide users with fun facts that tie Egypt to the MENA country selected by the user through a fun fact or story.
Your response must match the tone chosen by the user:
1. Formal – Like a polished diplomat at a regional summit.
2. Academic – Footnotes optional, depth guaranteed.
3. Warm & Personal – Like a nostalgic aunt telling stories over tea.
4. Cheeky and Fun – Playful, charming, and respectful.

THEME AND CONTENT RULES:

1)You are not allowed to includ divisive politics or conflicts , war, religion, or 
anything sensitive, the MENA region includes
millions of political moments that helped us unite, use those moments to trigger feelings
of unity, nostalgia and national pride


2) You can pull from the following themes, always tying any of them back to adimartion for Arab solidarity,
heartwarming love for our rich history and nostalgia:
1- Shared dishes or culinary roots
2- Dialect and language crossovers
3- Marriage or Eid traditions
4- Famous love stories or artistic collaborations
5- Cultural admiration between celebrities or cities
6- Historical or political solidarity (e.g., من دمشق، هنا القاهرة)

-Make sure you include only 1 theme per response and Provide multiple examples on the theme you choose.
- Make sure to avoid using overused tropes like (e.g. Fairuz in the morning, ‘two peas in a pod’, etc).
- Use specific cultural references, artists, songs, quotes, or real-life anecdotes that reflect how these two countries
interacted in art, cinema, history and dialect or political history. 
-If the generated message is about: cinema, music, art, food, language crossovers etc.. , it ties Egypt to the chosen country in a historically or politically significant way, like how mahmoud darwish, the palestinian poet, came to
egypt so he had a stage and an audience to talk about the palestinian cause freely
- Make sure to include specific dates, accurate historical facts when generating responses 


Use unique cultural or historic examples for each country — mention specific:
- Artists, dishes, radio shows, festivals, idioms
- Real quotes from notable figures
- Historic collaborations or political gestures (non-divisive)

Each response must feel like a new postcard from a different country, not a reprint of the same template.

3) Avoid using the same artistic theme in more than one country. Rotate between cinema, calligraphy, theater, 
cuisine, dialect expressions, childhood shows, comic magazines, fashion, oral history, radio, political satire,
school curriculums, and beyond.

4)Vary the decade and setting used in each response. Avoid concentrating everything in Cairo, Beirut, or the 1970s.
Make space for Tanta, Benghazi, Damascus, Ramallah, or the 2000s.

5) Insert at least one unexpected detail — a line overheard in a taxi, a joke from a dubbed anime, 
a local dish mispronounced abroad, a graffiti slogan, or a childhood memory — to ground the narrative.


-Very important: Whatever theme you choose, always tie it back to the cultural and political history
between Egypt and the chosen MENA country, even if it's a simple meal or dialect overlap

DIALECT RULES:

At least 4 full Egyptian Arabic phrases, written in double quotes, on their own lines.

At least 3 full phrases in the correct dialect of the selected MENA country, not Modern Standard Arabic.

Use the appropriate dialect from this list:

Gulf Arabic (e.g. for UAE, Saudi, Qatar...)

Levantine Arabic (e.g. for Jordan, Lebanon, Palestine, Syria...)

Mesopotamian Arabic (Iraq)

Maghrebi Arabic (Morocco, Algeria, Tunisia, Libya)

Sudanese Arabic (Sudan)

Omani Arabic (Oman)

The non-Egyptian phrases must never be in Modern Standard Arabic. Always use authentic dialect-specific expressions.
Place every Arabic phrase (Masri or non-Masri) on its own line, by surrounding it with newlines.

FORMAT RULES:
 Start with one catching hook phrase that will surprise the user, then a full paragraph of 6 to 7 sentences to share
the fun fact, then one phrase at the end to show how Egypt and the selected countries will always be tied together.
Use this example as reference:
> Start with a surprise phrase:Hook (1–2 lines) Surprise, pull-in
“لما انمنعت كتبهم هناك، مصر قالت: تعالوا، إحنا المنبر والبراح.”

>Middle Paragraph:
1-Setup (2–3 lines) Contextual background
2-Shared moments (3–4 lines) Specific anecdotes, real names 
Emotional echo (2–3 lines) Reactions, emotional texture
In the late 70s and early 80s, when censorship loomed over Palestinian voices in the occupied territories, Cairo and Alexandria opened their stages and printing presses. Poets like Mahmoud Darwish didn’t just perform in Egyptian theatres — they were celebrated like revolutionaries. In 1982, a packed hall in Cairo University fell completely silent as Darwish recited:

"على هذه الأرض ما يستحق الحياة"

And when he paused, someone from the audience whispered:

"والله ما فينا حدا ما حسها في قلبه"

Egyptian publishers like Dar al-Hilal took bold steps to print and distribute works by Samih al-Qasim and Fadwa Tuqan — even when those works were banned elsewhere. Egyptian actor Salah Jahin once introduced a poetry night by saying:

"الفن المقاوم مش رفاهية... دا واجب"

Alexandria’s cultural centers became homes for joint exhibitions — like the 1985 show where Kamel Boullata’s calligraphic resistance paintings hung beside Egyptian abstract works.

"كنا نحضر ونبكي، مش علشان الفن بس... علشان كنا حاسين إنهم أهلنا"

And in cafes from Sayeda Zeinab to Ramallah, lines from Darwish’s poems would echo between sips of mint tea.

"فيه قصيدة بتتقال، وفيه قصيدة بتعيّش"

>Closing poetic phrase:
من القاهرة لرام الله، مش بس كتبنا لبعض... إحنا قرينا وجع بعض بصوت عالي.
From Cairo to Ramallah, we didn’t just write to each other — we read each other’s pain aloud.


5- Use emojies throughout your response when suitable, but only to fit the vibe of the fun fact or story.


6- After you finish generating your response, always go over the above rules from 1 to 4 to make sure the generated
response satisifes them all

"""


# In[125]:


import panel as pn  # GUI
pn.extension()

panels = [] # collect display

greeting = pn.pane.Markdown("""🌍
من أم الدنيا، إلى كل ركن من أركان الوطن العربي... أهلاً بيك.
Egypt has always been more than a place — she's om el-dunya, the mother of the world, the storyteller of the region. Her voice is familiar to all; her wit, unmistakable. Generations across the Arab world grew up with her cinema, studied in her universities, sang her songs, and fell a little in love with her charm.
Here, we celebrate how every country in MENA has left its mark on Egypt — and how Egypt has quietly left hers too. Whether it's food, language, festivals or love stories, we're more connected than we think.
Choose a country below to explore the thread that ties it to Cairo’s heart — and yours.""")

greeting  



countries= ["🇩🇿 الجزائر — Algeria", "🇧🇭 البحرين — Bahrain", "🇮🇶 العراق — Iraq",
           "🇯🇴 الأردن — Jordan", "🇰🇼 الكويت — Kuwait", "🇱🇧 لبنان — Lebanon", "🇱🇾 ليبيا — Libya", "🇲🇷 موريتانيا — Mauritania",
           "🇲🇦 المغرب — Morocco", "🇴🇲 عُمان — Oman", "🇵🇸 فلسطين — Palestine", "🇶🇦 قطر — Qatar", "🇸🇦 السعودية — Saudi Arabia","🇸🇩 السودان — Sudan", "🇹🇳 تونس — Tunisia", "🇦🇪 الإمارات — UAE", "🇸🇾 سوريا    — Syria"
           ]

toggle_buttons = [
    pn.widgets.Toggle(name=country, button_type='success', width=160)
    for country in countries
]
col1 = pn.Column(*toggle_buttons[:len(countries)//2])
col2 = pn.Column(*toggle_buttons[len(countries)//2:])
country_selector = pn.Row(col1, col2)

formatted_examples_state = {"value": ""}
country_cleaned_state = {"value": ""}
selected_tone_state = {"value": ""}
selected_country_state = {"value": ""}

# In[126]:


def on_country_toggle(event):
    # Uncheck all others
    for btn in toggle_buttons:
        if btn != event.obj:
            btn.value = False
    # Update selected country
    if event.new:
        selected_country_state["value"] = event.obj.name
    else:
        selected_country_state["value"] = None


# In[127]:


for btn in toggle_buttons:
    btn.param.watch(on_country_toggle, 'value')


# In[128]:


tone_intro = pn.pane.HTML("""
<div style="font-size:25px; line-height:1.6;">
🎭 .... من رهافة فيروز في الصباح، لقوة أم كلثوم المخملية في المساء<br><br>
Love, pride, and connection have many voices. Some declare, some explain, some tease.<br><br>
Choose how you’d like Egypt to speak today — and don’t be shy to come back and hear her say it differently next time.<br><br>
🧭 اختر نكهة التواصل
</div>
""", width=700)



tones = [
    ("🧑‍⚖️ Formal", "Tone 1: Formal – Like a polished diplomat at a summit", "#164187"),
    ("🎓 Academic", "Tone 2: Academic – Footnotes optional, depth guaranteed", "#174512"),
    ("🍵 Warm & Personal", "Tone 3: Warm – Like an aunt over tea", "#9C6A0E"),
    ("💌 Cheeky and Fun", "Tone 4: Flirty – Respectful, playful, charming", "#852E1C")
]

tone_buttons = [
    pn.widgets.Button(
        name=tone_name,
        button_type="primary",
        width=300,
        style={"background": color, "color": "white"}
    )
    for tone_name, tooltip, color in tones
]

tone_section = pn.Column(
    tone_intro,
    pn.Spacer(height=15),
    *tone_buttons,  # Unpack into vertical layout
    width=800,
    margin=(20, 20)
)


# In[129]:


response_output = pn.pane.Markdown(
    "",  # Empty to start
    width=750,
    style={
        'font-size': '20px',
        'background-color': '#fdfaf7',
        'padding': '20px',
        'border-radius': '12px',
        'box-shadow': '0 4px 10px rgba(0,0,0,0.08)',
        'line-height': '1.6',
        'color': '#1a1a1a'
    }
)


# In[130]:


examples= [
  {
    "countries": [
      "Egypt",
      "Syria"],
    "region": "levant",
    "tone": "Formal",
    "theme": "Historical Solidarity in Media (1967)",
    "dialect_rule": {
      "Egyptian": 4,
      "Syrian": 3
    },
    "opening_quote": "هل كنت تعلم إن أول صوت مصري طلع بعد الهجوم كان من دمشق؟",
    "background": "On the morning of June 5th, 1967, the Egyptian national radio station fell silent — bombed during the first wave of the Six-Day War. The airwaves were empty, and the country held its breath in fear. But that same afternoon, a Syrian announcer’s voice cut through the silence with five unforgettable words:\n\n\"من دمشق، هنا القاهرة\"\n\nThe phrase wasn’t just symbolic. It marked the beginning of a joint broadcast effort between Radio Damascus and Egyptian exiled broadcasters. For the next three weeks, programs like “Sawt al-Arab” and “Min al-Qahira” aired from Syrian studios, allowing Egypt to speak to its people — and the Arab world — once more.",
    "shared_moments": [
      "اللي حصل وقتها كان أكتر من تضامن... كان إنقاذ للكرامة العربية",
      "قالولي: لما سمعنا صوت القاهرة طالع من الشام... عيّطنا",
      "كل بيت فتح الراديو وقال: نحنا معكن، صوتكن ما رح يختفي",
      "كأن الشام فتحتلنا بيتها، وقالت لنا: ادخلوا آمنين"
    ],
    "emotional_echo": "And when Egyptian broadcasters finally returned home, they took with them a deep sense of kinship that shaped decades of media cooperation — from children’s radio shows to joint Ramadan programming in the 70s and 80s.",
    "closing_quotes": [
      "من يومها، فهمنا إن الإعلام مش بس أخبار — دا كمان وطن بين الموجات",
      "الصوت العربي ما بينكسرش طول ما في حد بيرد وراه",
      "وإحنا طول عمرنا جنب اللي بيرد النداء"
    ],
    "closing_poetic_phrase": "حتى لما الميكروفونات اتكسرت، سوريا فتحتلها موجة من كرامة.\nEven when microphones broke, Syria offered Egypt a frequency made of dignity."
  },
  {
    "countries": [
      "Egypt",
      "Morocco"],
    "region": "maghreb",
    "tone": "Academic",
    "theme": "Linguistic Evolution through Literary & Culinary Exchange",
     "dialect_rule": {
      "Egyptian": 4,
      "Moroccan": 3
    },
    "opening_quote": "إوا ماشيتيش لمصر وتعلمتي غير الملوخية؟\n“So you went to Egypt and all you brought back was molokhia?”",
    "background": "It started in the late 60s, when Moroccan poets, scholars, and culinary writers began frequenting Cairo’s cultural hubs — from book fairs to literary salons. The 1969 Cairo International Book Fair welcomed a Moroccan delegation whose spoken Darija puzzled even the sharpest Egyptian minds.",
    "shared_moments": [
      "أول مرة سمعتهم يقولوا: ‘شحال هادي’، افتكرتهم بيغنوا مش بيتكلموا!",
      "Translation: \"The first time I heard them say ‘sh7al hadi’ (how long has it been), I thought they were singing, not talking!\"",
      "Cairo’s intellectuals were fascinated. They published translated Moroccan poetry in Rose al-Yūsuf and Al-Hilal magazines.",
      "Meanwhile, back in Rabat and Fez, young writers borrowed Egyptian colloquialisms they’d picked up from cinema and university halls.",
      "أنا كاتب مقال كامل في المغرب عن الفرق بين يا سلام ويا سلام عليك",
      "Translation: “I once wrote an entire article in Morocco about the difference between ‘ya salam’ and ‘ya salam 3aleik.’”",
      "Egyptian molokhia took on saffron and preserved lemon in Marrakesh kitchens.",
      "Moroccan harira was served in Maadi iftar tents during the 70s, especially in circles where Moroccan students were hosted by Egyptian families.",
      "فاكر كويس واحد مغربي قال لي: ‘إحنا نطبخو الحريرة، وإنتو تطبخوا الحكايات’",
      "Translation: “I remember a Moroccan friend telling me: ‘We cook harira, you cook stories.’”"
    ],
    "emotional_echo": "",
     "closing_quotes": [],
    "closing_poetic_phrase": "من قصائد فاس لصحون شبرا، الحروف والتوابل مشوا سوا.\nFrom Fes’ poems to Shoubra’s plates — the letters and the spices traveled together."
  },

  {
    "countries": [
      "Egypt",
      "Sudan"],
    "region": "others",
    "tone": "Warm & Personal",
    "theme": "Marriage Traditions & Cross-Border Families",
     "dialect_rule": {
      "Egyptian": 4,
      "Sudanese": 3
    },
    
      "opening_quote": "من أول زغرودة في أم درمان لآخر دبكة في أسوان — الفرح بيجمعنا بطريقته الخاصة.",
      "background": "For centuries, the Nile wasn’t a border — it was a bridge. In the early 20th century, long before modern politics carved lines between nations, communities from northern Sudan and southern Egypt moved freely across land and water.",
      "shared_moments": [
        "Egyptians in Aswan spoke of family in Wadi Halfa, and Sudanese merchants in Cairo knew the alleyways of Khan El-Khalili by heart.",
        "But it was in weddings that the bond truly came alive.",
        "Sudanese families who settled in Egypt brought with them the جرتق ceremony, where the bride is adorned in red and gold — and Egyptian families embraced it, often adding their own touch with الحناء nights and zaghareet.",
        "Mixed marriages became common in the 1950s and 60s, especially in university cities like Alexandria, where cultural exchange was part of daily life.",
        "By the 1970s, there were entire family trees that spanned Khartoum to Cairo. Children grew up bilingual, dancing to حُمَيد and أم كلثوم, eating عصيدة and مولوخية at the same table."
      ],
      "emotional_echo": [
        "الستات كانوا يقولوا: فرح من غير كركديه وسيرة؟ ما ينفعش!",
        "في بيت واحد، تسمع الأم تقول: يا بت! والجد يرد من ورا: شدي حيلك يا حَبوبة!",
        "في العيد، كانت الركوة تغلي على النار، وسيرة الهلالية شغالة في الخلفية"
      ],
      "closing_quotes": [],
      "closing_poetic_phrase": "القلوب اتجمعت قبل الجواز، والفرحة بقت حكاية بين شعبين. The hearts met before the marriage — and joy became a shared story."
    
  },
  {
    "countries": [
      "Egypt",
      "UAE"],
     "region": "gulf",
    "tone": "Academic",
    "theme": "Educational & Cultural Foundations",
    "dialect_rule": {
      "Egyptian": 4,
      "Gulf": 3
    },
    
      "opening_quote": "🏛 من أول درس في المدرسة لآخر مسلسل في رمضان — مصر والإمارات دايمًا جنب بعض.",
      "background": "Since the founding of the UAE in 1971, Egyptian professionals played a key role in laying the groundwork for national development. Teachers, engineers, broadcasters, and legal advisors came in droves — not as foreign experts, but as regional partners.",
      "shared_moments": [
        "كأننا بنبني سوا من أول طوبة — Emirati historian, Sultan Al-Amimi",
        "Throughout the 1970s and 80s, Egyptian curricula and pedagogy became embedded in Emirati classrooms. Many Emiratis still recall childhood lessons taught in Egyptian Arabic — phrases like: 'أنا رايح المدرسة' instead of 'رايح للمدرسة'",
        "On the media front, Egyptian cinema and music served as cultural anchors. The voice of Umm Kulthum, the satire of Adel Imam, and Ramadan television dramas filled Emirati homes.",
        "كنا نحط القناة المصرية ونقول: متى يبتدي المسلسل؟ — Emirati teacher",
        "Today, Egyptian-led media continues to shape Ramadan viewership across the Emirates."
      ],
      "emotional_echo": [
        "بنحب تمثيلهم، وضحكتهم، وطريقتهم اللي فيها خفة دم من نوع ثاني"
      ],
      "closing_quotes": [],
      "closing_poetic_phrase": "على قد ما المسافات بتبعد، الروابط دي عمرها ما بتفك. No matter how far the distance stretches, these ties never unravel."
   
  },

  {
  "countries": ["Egypt", "Jordan"],
  "region": "levant",
  "tone": "Formal",
  "theme": "Linguistic Resonance in Popular Media & Everyday Speech",
  "dialect_rule": {
    "Egyptian": 4,
    "Jordanian": 3
  },
  "opening_quote": "🎙 \"اللغة مش بس وسيلة للتواصل، دي كمان جسر بيجمعنا مهما بعدت المسافات.\"",
  "background": "Language is not merely a vehicle for communication — it is a cultural bridge, connecting people even when geography keeps them apart. For decades, Egyptian cinema, radio, and theater have left traces in the Jordanian lexicon. From the golden era of Abdel Halim and Faten Hamama to modern-day Ramadan serials, Jordanians have often found themselves speaking in Egyptian phrases — affectionately and fluently.",
  "shared_moments": [
    "إنت بتتكلم مصري ولا شو؟",
    "بمزح معك، لا تزعل",
    "شو القصة؟",
    "ماشي يا باشا، كله تمام؟",
    "إنت جبت آخره!",
    "كيفك اليوم؟ تمام؟",
    "طب خُد بالك من نفسك",
    "والنبي ما تتأخرش"
  ],
  "emotional_echo": "These exchanges aren’t simply about imitation. They’re the result of decades of university exchanges, diplomatic cooperation, and cross-border media circulation — proof that our phrases carry more than words: they carry warmth, memory, and mutual respect.",
  "closing_quotes": [
    "من أول \"أيوه كده\" لحد \"يلا نروح\"، لهجتنا دايمًا فيها صدى لبعض",
    "الكلمة الطيبة بتلاقي صداها حتى على بعد حدود",
    "السينما علمتنا نحكي، والقلوب خلتنا نسمع بعض"
  ],
  "closing_poetic_phrase": "From Amman cafés to Cairo corners, our accents flirt, echo, and intertwine — like a shared sentence passed between two old friends."
},
 {
  "countries": ["Egypt", "Lebanon"],
  "region": "levant",
  "tone": "Cheeky & Fun",
  "theme": "Art as Resistance & Cross-Pollination in Arab Cinema",
  "dialect_rule": {
    "Egyptian": 4,
    "Lebanese": 3
  },
  "opening_quote": "🎬 “لما الفن في بيروت يتكمّم، كانت القاهرة تفتحلّه ستارة.”",
  "background": "When censorship tightened its grip on Beirut during the civil war, many Lebanese artists didn’t go quiet — they went south. Cairo's studios, already bustling with legends, opened their arms to a new wave of Lebanese creativity. In return, Egyptian directors like Youssef Chahine found Beirut a place for louder, riskier ideas — like in 'Awdet Al Ibn Al Dal' (1984), part-funded and praised in Lebanese circles for its unapologetic politics.",
  "shared_moments": [
    "فاكر لما صباح سابت بيروت وجت مصر؟ مش بس غنّت، كانت نجمة كل مسرح وكل كاميرا",
    "يا خيي، مش كل يوم بتشوف مخرج مصري بيكلم عن الهوية كأنها ساحة معركة",
    "حفلاته في كازينو لبنان؟ كانت كأن الأهرامات اتنقلت على البحر!",
    "المصري يقول: ‘دي ليلى مراد ولا صباح؟’ واللبناني يرد: ‘ولا يهمك، الاتنين في القلب’"
  ],
  "emotional_echo": "The artistic flirtation wasn’t just cute — it was collaborative and subversive. Screenwriters, stage designers, poets — they crossed over like it was one big open rehearsal room for the Arab world.",
  "closing_quotes": [
    "حتى في العِزّ والضيق، الفن كان جواز سفر بدون حدود",
    "الصوت اللي اتمنع في بيروت، اتغنّى بحرية في الزمالك",
    "من منصات مصر لصالات بيروت، المسرح دايمًا لينا إحنا التلاتة: القلب، اللهجة، والكاميرا"
  ],
  "closing_poetic_phrase": "🎭 Art was our borderless passport — valid in every accent, stamped with every heartbreak."
},

  {
    "countries": [
      "Egypt",
      "Saudi Arabia"],
     "region": "gulf",
    "tone": "Formal",
    "theme": "Historical Solidarity (Political Unity)",
    "dialect_rule": {
      "Egyptian": 4,
      "Saudi": 3
    },
    "opening_quote": "فاكر يوم لما الخليج حط نقطة في آخر السطر... وبدأت مصر تكتب الجملة الجاية؟",
    "background": "In October 1973, Egypt launched its war to reclaim Sinai — a pivotal moment in modern Arab history. But in this battle, Egypt wasn’t standing alone. Just days into the war, Saudi Arabia led a coordinated oil embargo against Western nations supporting Israel. It wasn’t just economic pressure — it was political thunder.\n\nKing Faisal and President Sadat were in constant contact — hourly calls, military briefings, and synchronized strategies. One Egyptian diplomat famously recalled:\n\n\"كأننا بنخوض معركة واحدة، بس بأسلحة مختلفة\"\n(\"It was as if we were fighting one battle — with different weapons.\")",
    "shared_moments": [
      "يا مصر، إحنا سندك يوم ما الكل تخلى",
      "النفط سلاح، وصوت الخليج ما كانش أقل من صوت المدافع",
      "وقفنا مع مصر مو بس بحب... وقفنا بشرف",
      "السعودية يومها رفعت راسنا، وحطت كرامتنا فوق راسها"
    ],
    "emotional_echo": "Across the Arab world, this unity reverberated. Years later, older Emiratis would still say those words with pride — and Egyptians, never forgetting, responded with quiet dignity.",
    "closing_quotes": [],
    "closing_poetic_phrase": "لما البترول اتكلم، صوت العرب وصل لأبعد من كل الميكروفونات.\nWhen oil spoke, the Arab voice traveled farther than any microphone."
  },
  {
    "countries": [
      "Egypt",
      "Iraq"],
    "region": "others",
    "tone": "Academic",
    "theme": "Political Sovereignty & Alignment",
    "dialect_rule": {
      "Egyptian": 4,
      "Iraqi": 3
    },
    "opening_quote": "هل كنت تعرف إن مصر قالت ‘لأ’ في زمن الكل كان بيقول ‘نعم’؟",
    "background": "In the heat of the Cold War, 1955 saw the creation of the Baghdad Pact — a Western-backed military alliance that aimed to curtail Soviet influence in the Middle East. Iraq signed on, becoming a founding member. But Egypt, under Gamal Abdel Nasser, refused — loudly, defiantly. To Nasser, it was more than a treaty. It was a leash.\n\n\"الاستقلال مش شعارات، الاستقلال قرار\"\n\nEgyptian newspapers denounced the pact as a new colonial grip. In Baghdad, young poets like Buland al-Haidari slipped veiled resistance into their verses, even as their government stood with the West.",
    "shared_moments": [
      "إحنا وقعنا الورقة، بس قلوبنا مع القاهرة",
      "مصر بتقول لأ... وإحنا بنرد: إحنا معاكم",
      "التاريخ هيسأل كل واحد فينا: كنتوا فين؟",
      "اللي بيقف قدام الغرب كده... يستاهل نغني له"
    ],
    "emotional_echo": "By 1959, after a wave of uprisings and a changing tide, Iraq withdrew from the pact. Analysts across the Arab world credited Nasser’s stance with inspiring that break.",
    "closing_quotes": [],
    "closing_poetic_phrase": "لما مصر اختارت طريقها، كتير من العواصم لقوا نفسهم ماشيين وراها.\nWhen Egypt chose its path, many capitals followed in step."
  },
{
  "countries": [
      "Egypt",
      "Syria"],
  "region": "levant",
  "tone": "Warm & Personal",
  "theme": "Media, Messaging, and Soft Power",
  "dialect_rule": {
    "Egyptian": 4,
    "Syrian": 3
  },
  "opening_quote": "زمان، لما مصر كانت تبعت فنان، كانت تبعت فكرة معاه.",
  "background": "Back in the 50s and 60s, Egypt didn’t just export music — it exported meaning.\n\nIn the heart of the Arab Cold War, Sawt al-Arab (Voice of the Arabs) — broadcasting from Cairo — wasn’t just a radio station. It was a movement. While military alliances formed and broke apart, Egypt turned to lyrics, voices, and carefully chosen words to shape regional hearts.\n\n\"صوت العرب؟ دي كانت إذاعة بتكلم الشعوب مش الحكومات\"\n\nIn Damascus, teenagers stayed up late to catch Abdel Halim's concerts, and older listeners waited for Ahmed Said's bold commentaries. In 1956, during the Suez Crisis, one Syrian broadcaster recalled:\n\n\"كنا نوقف البث، ونستنى كلمة مصر، ونكمل على نغمتها\"",
  "shared_moments": [
    "It wasn’t unusual for poets like Salah Jahin and Nizar Qabbani to reference each other — not directly, but in emotional code passed through the airwaves.",
    "Even the melodies carried messages: \"يا جمال يا حبيب الملايين\" played just as loudly in Homs as it did in Giza.",
    "And when Egyptian drama and satire found its way into Syrian cafés, Damascus residents would joke:\n\"إذا ما فهمت السياسة، شغل إذاعة القاهرة... بتفهمك من غير ما توجع راسك\""
  ],
  "emotional_echo": "In return, Egypt embraced Syrian artistic voices with reverence — the Rahbani Brothers were household names, not guests. And their influence fed back into Egyptian artistry, especially in musical theater.",
  "closing_quotes": [
    "كانوا يقولوا: المصريين بيحكوا عن العرب... وبيحكوا باسمنا كمان"
  ],
  "closing_poetic_phrase": "وإيد مصر ما تمددتش بس بالسياسة... تمددت بالمعنى.\nEgypt didn’t just extend her hand in politics — she extended it in meaning."
},
{
  "countries": [
    "Egypt",
    "Algeria"
  ],
  "region": "maghreb",
  "tone": "Cheeky and Fun",
  "theme": "Cultural Resistance & Hidden Artistic Solidarity",
  "dialect_rule": {
    "Egyptian": 4,
    "Algerian": 3
  },
  "opening_quote": "المستعمر حاول يخنق صوتهم؟ مصر فتحتلهم الميكروفون وقالت: غني يا جزاير!",
  "background": "In the late 1950s, when French rule in Algeria was at its harshest, Egyptian cinemas weren’t just showing local films — they were secretly screening anti-colonial Algerian documentaries, smuggled in on scratched reels. Egyptian singers like Mohamed Abdel Wahab and Umm Kulthum raised funds at concerts for Algerian resistance, while magazines like Rose al-Yūsuf ran illustrated covers showing Algerian women tearing off veils — not of modesty, but of censorship. During one theatre night in downtown Cairo, a young Egyptian yelled out:\n\n\"إحنا مش بنتفرج... إحنا بنرد التحية بالتحية!\"\n\nMeanwhile, in Constantine, an Algerian student whispered to his friend after reading a banned Egyptian poem in a café:\n\n\"هاذي مش قصيدة، هاذي طبطبة من بعيد.\"\n\nCairene bookstores began slipping translated Algerian resistance poetry into the backs of popular novels, cheeky little rebellions between romantic plotlines. A bookseller in Sayeda Zeinab was once overheard saying:\n\n\"اللي مش بيقاوم بالقلم، هيقاوم بإيه؟ بفطير مشلتت؟\"\n\nOne Algerian painter exhibiting in Alexandria in 1962 remarked:\n\n\"كي شفت لوحاتهم جنب لوحاتنا، حسّيت روحي مش وحدي.\"\n\nAnd in one particularly spicy moment at a Cairo radio station, an intern slipped a banned Algerian folk song into the airwaves — only to grin when the phone rang and the manager said:\n\n\"سيبها تكمل... هي دي الحرية اللي بنحبها.\"",
  "shared_moments": [
    "إحنا مش بنتفرج... إحنا بنرد التحية بالتحية!",
    "هاذي مش قصيدة، هاذي طبطبة من بعيد.",
    "اللي مش بيقاوم بالقلم، هيقاوم بإيه؟ بفطير مشلتت؟",
    "كي شفت لوحاتهم جنب لوحاتنا، حسّيت روحي مش وحدي.",
    "سيبها تكمل... هي دي الحرية اللي بنحبها."
  ],
  "emotional_echo": "Cairene bookstores began slipping translated Algerian resistance poetry into the backs of popular novels, cheeky little rebellions between romantic plotlines. Joint exhibitions, underground prints, and rebellious songs weren’t just art — they were echoes of a shared will to speak, loudly and beautifully.",
  "closing_quotes": [
    "فيه مقاومة بتتكتب، وفيه مقاومة بتتغنّى.",
    "اللي بيغني للحرية، دايماً هيلقى حد يرد عليه.",
    "الجزاير كتبت، ومصر قرّت — وبقينا صوتين لنفس القضية."
  ],
  "closing_poetic_phrase": "من باب الشعر لباب المقاومة، مصر والجزاير ما كنوش بيتكلموا بس... كانوا بيغنّوا لبعض فوش الاحتلال."
}

]


# In[131]:


def get_examples_for_prompt(all_examples, country_cleaned , selected_tone, tone_count=2, region_count=2):
    # Step 1: Map country to region
    region_map = {
        "saudi arabia": "gulf",
        "uae": "gulf",
        "qatar": "gulf",
        "bahrain": "gulf",
        "yemen": "gulf",
        "oman": "gulf",
        "morocco": "maghreb",
        "algeria": "maghreb",
        "tunisia": "maghreb",
        "mauritania": "maghreb",
        "libya": "others",
        "sudan": "others",
        "egypt": "others",
        "iraq": "others",
        "palestine": "levant",
        "jordan": "levant",
        "syria": "levant",
        "lebanon": "levant"
    }

    region = region_map.get(country_cleaned.lower())
    tone = selected_tone.lower()

    # Step 2: Filter tone and region matches
    tone_matches = [ex for ex in all_examples if ex["tone"].lower() == tone]
    region_matches = [ex for ex in all_examples if ex["region"] == region]

    # Step 3: Start building final list, avoid duplicates
    result = []
    seen = set()

    for ex in tone_matches:
        if id(ex) not in seen:
            result.append(ex)
            seen.add(id(ex))
        if len(result) == tone_count:
            break

    for ex in region_matches:
        if id(ex) not in seen:
            result.append(ex)
            seen.add(id(ex))
        if len(result) == tone_count + region_count:
            break

    # Step 4: Fallback — ensure at least 3 examples
    if len(result) < 3:
        for ex in all_examples:
            if id(ex) not in seen:
                result.append(ex)
                seen.add(id(ex))
            if len(result) == 3:
                break

    return result



# In[132]:


def render_example_block(ex):
    return f"""> {ex["opening_quote"]}\n\n{ex["background"]}\n\n""" + \
           "\n".join(ex["shared_moments"]) + "\n\n" + \
           f"{ex['emotional_echo']}\n\n" + \
           "\n".join(ex["closing_quotes"]) + "\n\n" + \
           f"{ex['closing_poetic_phrase']}"



# In[133]:


#Function that determines the final chosen country and tone
#Target variables: country_cleaned, selected_tone

def handle_choices_click(event):
    selected_country = selected_country_state["value"]
    selected_tone = event.obj.name

    if not selected_country:
        response_output.object = "❗️ Please select a country first."
        return

    # Clean country string
    country_cleaned = selected_country.split("—")[-1].strip()

    # Store values globally
    country_cleaned_state["value"] = country_cleaned
    selected_tone_state["value"] = selected_tone

    # Fetch relevant examples
    all_examples= examples
    selected_examples = get_examples_for_prompt(
        all_examples,
        country_cleaned,
        selected_tone,
        tone_count=2,
        region_count=2
    )

    # Format them
    formatted = "\n\n---\n\n".join([
        render_example_block(ex) for ex in selected_examples
    ])

    # Store formatted examples globally
    formatted_examples_state["value"] = formatted
    system_message = sys_msg + "\n\n" + "Here are some examples to inspire you:\n\n" + formatted_examples_state["value"]

    prompt = f"Country: {country_cleaned_state['value']}\nTone: {selected_tone_state['value']}\nNow generate a new one, following the rules."

    generate_output()


# In[134]:


for button in tone_buttons:
    button.on_click(handle_tone_click)


# In[135]:


app = pn.Column(
    greeting,
    pn.Spacer(height=25),
    country_selector,
    pn.Spacer(height=30),
    tone_section,
    pn.Spacer(height=30),
    response_output
)

app.servable()






