from telegram import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

voting_button = ReplyKeyboardMarkup([["🎲 Ovoz berish"]], resize_keyboard=True)


groups = InlineKeyboardMarkup([[InlineKeyboardButton(text="Data Science", callback_data="data science"),
          InlineKeyboardButton(text="Full sctack", callback_data="full stack"),
          InlineKeyboardButton(text="Software", callback_data="software")],
          [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")]])


mentors = {
    "data science": InlineKeyboardMarkup([[InlineKeyboardButton(text="Komiljon Xamidjonov", callback_data="Komiljon Xamidjonov"),
                                           InlineKeyboardButton(text="Arslanova Nodira", callback_data="Arslanova Nodira"),
                                           InlineKeyboardButton(text="Alimbayeva Asalbonu", callback_data="Alimbayeva Asalbonu")],
                                           [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")],
                                          ]),

    "full stack": InlineKeyboardMarkup([[InlineKeyboardButton(text="Dehqonov Lochinbek", callback_data="Dehqonov Lochinbek")],
                                           [InlineKeyboardButton(text="Anduqodir Nortojiyev", callback_data="Anduqodir Nortojiyev")],
                                           [InlineKeyboardButton(text="Humoyun Qosimov", callback_data="Humoyun Qosimov")],
                                           [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")],
                                        ]),

    "software": InlineKeyboardMarkup([[InlineKeyboardButton(text="Sarvar Ozodov", callback_data="Sarvar Ozodov")],
                                           [InlineKeyboardButton(text="Ilesov Azamat", callback_data="Ilesov Azamat")],
                                           [InlineKeyboardButton(text="Abduraimov Sherzod", callback_data="Abduraimov Sherzod")],
                                           [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")],
                                      ])
}


result = InlineKeyboardMarkup([[InlineKeyboardButton(text="qoniqarli", callback_data="qoniqarli")],
                                [InlineKeyboardButton(text="qoniqarsiz", callback_data="qoniqarsiz")],
                                [InlineKeyboardButton(text="namunali", callback_data="namunali")],
                                [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")],
                               ])


because_of = {
    "namunali": InlineKeyboardMarkup([[InlineKeyboardButton(text="o'z vaqtida ish joyida", callback_data="o'z vaqtida ish joyida")],
                                       [InlineKeyboardButton(text="barcha savolimga javob berdi", callback_data="barcha savolimga javob berdi")],
                                       [InlineKeyboardButton(text="juda ham yaxshi tushuntirdi", callback_data="juda ham yaxshi tushuntirdi")],
                                       [InlineKeyboardButton(text="yangicha va qiziqarli usulda taqdimot qilib tushuntirdi", callback_data="yangicha va qiziqarli usulda taqdimot qilib tushuntirdi")],
                                       [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")],
                                      ]),

    "qoniqarsiz": InlineKeyboardMarkup([[InlineKeyboardButton(text="o'z vaqtida ish joyida yo'q", callback_data="o'z vaqtida ish joyida yo'q")],
                                         [InlineKeyboardButton(text="umuman yordam bera olmadi", callback_data="umuman yordam bera olmadi")],
                                         [InlineKeyboardButton(text="yordam berishdan bosh tortdi", callback_data="yordam berishdan bosh tortdi")],
                                         [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")],
                                        ]),

    "qoniqarli": InlineKeyboardMarkup([[InlineKeyboardButton(text="darsni kechroq boshladi", callback_data="o'z vaqtida ish joyida yo'q")],
                                         [InlineKeyboardButton(text="kamroq yordam berdi", callback_data="umuman yordam bera olmadi")],
                                         [InlineKeyboardButton(text="amamilyot qo'llamadi", callback_data="yordam berishdan bosh tortdi")],
                                         [InlineKeyboardButton(text="🔙 orqaga 🔙", callback_data="🔙 orqaga 🔙")],
                                       ]),
}


submit = InlineKeyboardMarkup([[InlineKeyboardButton(text="✅Tasdiqlash", callback_data="tasdiqlandi"),
                                InlineKeyboardButton(text="❌Tasdiqlamaslik", callback_data="tasdiqlanmadi")]])
