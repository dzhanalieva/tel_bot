from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler
)
from cred import TOKEN
from menu import main_menu_keyboard
from key_buttons import tele_button


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Добро пожаловать, {update.effective_user.username}", 
        reply_markup = main_menu_keyboard()
    )

def first_dish_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton("Куриный суп", callback_data="first_dish_куриный суп"),
        InlineKeyboardButton("Борщ", callback_data="first_dish_борщ")
        ],
        [InlineKeyboardButton("Гороховый суп", callback_data="first_dish_гороховый суп" ),
            InlineKeyboardButton("Сырный суп", callback_data="first_dish_сырный суп")],
            [
        InlineKeyboardButton("Фасолевый суп", callback_data="first_dish_фасолевый суп"),
        InlineKeyboardButton("Жаренные пельмени", callback_data="first_dish_жаренные пельмени")
        ],
        [
        InlineKeyboardButton("Солянка", callback_data="first_dish_солянка"),
        InlineKeyboardButton("Лагман", callback_data="first_dish_лагман")
        ]

    ]
    reply_marcup = InlineKeyboardMarkup(keyboard)#　это  кнопки в самом чате
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_marcup
    )


def second_dish_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton("Гнезда тальятелле", callback_data="second_dish_гнезда тальятелле"),
        InlineKeyboardButton("Котлеты", callback_data="second_dish_котлеты")
        ],
        [InlineKeyboardButton("Курица карри", callback_data="second_dish_курица карри" ),
            InlineKeyboardButton("Паста карбонара", callback_data="second_dish_паста карбонара")],
            [
        InlineKeyboardButton("Паста с курицей", callback_data="second_dish_паста с курицей"),
        InlineKeyboardButton("Плов", callback_data="second_dish_плов")
        ],
        [
        InlineKeyboardButton("Ризотто", callback_data="second_dish_ризотто"),
        InlineKeyboardButton("Чахохбили", callback_data="second_dish_чахохбили")
        ]

    ]
    reply_marcup = InlineKeyboardMarkup(keyboard)#　это  кнопки в самом чате
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_marcup
    )


def salads_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton("Греческий", callback_data="salads_греческий"),
        InlineKeyboardButton("Капустный", callback_data="salads_капустный")
        ],
        [InlineKeyboardButton("Кобб салат", callback_data="salads_кобб салат" ),
            InlineKeyboardButton("Мимоза", callback_data="salads_мимоза")],
            [
        InlineKeyboardButton("Нисуаз", callback_data="salads_нисуаз"),
        InlineKeyboardButton("Салат из баклажанов", callback_data="salads_салат из баклажанов")
        ],
        [
        InlineKeyboardButton("Цезарь", callback_data="salads_цезарь"),
        InlineKeyboardButton("Яичный", callback_data="salads_яичный")
        ]

    ]
    reply_marcup = InlineKeyboardMarkup(keyboard)#　это  кнопки в самом чате
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_marcup
    )


def dessert_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
        InlineKeyboardButton("Банановый кекс", callback_data="dessert_банановый кекс"),
        InlineKeyboardButton("Домашнее мороженое", callback_data="dessert_домашнее мороженое")
        ],
        [InlineKeyboardButton("Меренговый рулет", callback_data="dessert_меренговый рулет" ),
            InlineKeyboardButton("Пончики", callback_data="dessert_пончики")],
            [
        InlineKeyboardButton("Тирамису", callback_data="dessert_тирамису"),
        InlineKeyboardButton("Шоколадная лава", callback_data="dessert_шоколадная лава")
        ],
        [
        InlineKeyboardButton("Шоколадные кексы", callback_data="dessert_шоколадные кексы"),
        InlineKeyboardButton("Яблочная шарлотка", callback_data="dessert_яблочная шарлотка")
        ]

    ]
    reply_marcup = InlineKeyboardMarkup(keyboard)#　это  кнопки в самом чате
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_marcup
    )


def beverages_inline_menu(update: Update, context: CallbackContext):
    keyboard = [ 
        [
        InlineKeyboardButton("Арбузный напиток", callback_data="beverages_арбузный напиток"),
        InlineKeyboardButton("Бананово-шоколадный коктейль", callback_data="beverages_бананово-шоколадный коктейль")
        ],
        [InlineKeyboardButton("Глинтвейн", callback_data="beverages_глинтвейн" ),
            InlineKeyboardButton("Клубнично-молочный коктейль", callback_data="beverages_клубнично-молочный коктейль")],
            [
        InlineKeyboardButton("Клюквенный напиток", callback_data="beverages_клюквенный напиток"),
        InlineKeyboardButton("Молочный коктейль из киви", callback_data="beverages_молочный коктейль из киви")
        ],
        [
        InlineKeyboardButton("Мохито безалькогольный", callback_data="beverages_мохито безалькогольный"),
        InlineKeyboardButton("Шоколадный коктейль", callback_data="beverages_шоколадный коктейль")
        ]

    ]
    reply_marcup = InlineKeyboardMarkup(keyboard)#　это  кнопки в самом чате
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_marcup
    )
                
def inline_button(update: Update, context: CallbackContext):
    keyboard1 = [
        [
        InlineKeyboardButton("Куриный суп", callback_data="first_dish_куриный суп"),
        InlineKeyboardButton("Борщ", callback_data="first_dish_борщ")
        ],
        [InlineKeyboardButton("Гороховый суп", callback_data="first_dish_гороховый суп" ),
            InlineKeyboardButton("Сырный суп", callback_data="first_dish_сырный суп")],
            [
        InlineKeyboardButton("Фасолевый суп", callback_data="first_dish_фасолевый суп"),
        InlineKeyboardButton("Жаренные пельмени", callback_data="first_dish_жаренные пельмени")
        ],
        [
        InlineKeyboardButton("Солянка", callback_data="first_dish_солянка"),
        InlineKeyboardButton("Лагман", callback_data="first_dish_лагман")
        ]

    ]
    reply_marcup1 = InlineKeyboardMarkup(keyboard1)
    query = update.callback_query

    if query.data == "first_dish_куриный суп":
        file = open('/home/ihyfyugfyugyugiu/Куриный суп.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/qhH131jxdvQ',
            reply_markup=reply_marcup1
        )
    
    if query.data == "first_dish_борщ":
        file = open('/home/ihyfyugfyugyugiu/Борщ.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/_-9nH4zFThs",
           reply_markup=reply_marcup1
        )

    if query.data == "first_dish_гороховый суп":
        file = open('/home/ihyfyugfyugyugiu/Гороховый суп.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/pw2tyLYkrWg",
           reply_markup=reply_marcup1
        )

    if query.data == "first_dish_сырный суп":
        file = open('/home/ihyfyugfyugyugiu/Сырный суп.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/frBEtB7w_LI",
           reply_markup=reply_marcup1
        )

    if query.data == "first_dish_фасолевый суп":
        file = open('/home/ihyfyugfyugyugiu/Фасолевый суп.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/YjcM_LEs4wE",
           reply_markup=reply_marcup1
        )

    if query.data == "first_dish_жаренные пельмени":
        file = open('/home/ihyfyugfyugyugiu/Жаренные пельмени.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/N__aobUfOC4",
           reply_markup=reply_marcup1
        )

    if query.data == "first_dish_солянка":
        file = open('/home/ihyfyugfyugyugiu/Солянка.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/wXiK9Qoce8A",
           reply_markup=reply_marcup1
        )

    if query.data == "first_dish_лагман":
        file = open('/home/ihyfyugfyugyugiu/Лагман.txt', 'r', encoding='utf-8')
        text = file.read()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/pF0MiqYUxLw",
           reply_markup=reply_marcup1
        )

    keyboard2 = [
        [
        InlineKeyboardButton("Гнезда тальятелле", callback_data="second_dish_гнезда тальятелле"),
        InlineKeyboardButton("Котлеты", callback_data="second_dish_котлеты")
        ],
        [InlineKeyboardButton("Курица карри", callback_data="second_dish_курица карри" ),
            InlineKeyboardButton("Паста карбонара", callback_data="second_dish_паста карбонара")],
            [
        InlineKeyboardButton("Паста с курицей", callback_data="second_dish_паста с курицей"),
        InlineKeyboardButton("Плов", callback_data="second_dish_плов")
        ],
        [
        InlineKeyboardButton("Ризотто", callback_data="second_dish_ризотто"),
        InlineKeyboardButton("Чахохбили", callback_data="second_dish_чахохбили")
        ]

    ]
    reply_marcup2 = InlineKeyboardMarkup(keyboard2)

    if query.data == "second_dish_гнезда тальятелле":
        file = open('/home/ihyfyugfyugyugiu/second/Гнезда тальятелле.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/Fezg1R3tW1s",
           reply_markup=reply_marcup2
        )

    if query.data == "second_dish_котлеты":
        file = open('/home/ihyfyugfyugyugiu/second/Котлеты.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/nIXI6riLXf8",
           reply_markup=reply_marcup2
        )

    if query.data == "second_dish_курица карри":
        file = open('/home/ihyfyugfyugyugiu/second/Курица карри.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/RNIGZ7oAJcQ",
           reply_markup=reply_marcup2
        )

    if query.data == "second_dish_паста карбонара":
        file = open('/home/ihyfyugfyugyugiu/second/Паста карбонара.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/0jRxAf7GpUs",
           reply_markup=reply_marcup2
        )

    if query.data == "second_dish_паста с курицей":
        file = open('/home/ihyfyugfyugyugiu/second/Паста с курицей.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/X3o4hybQm6c",
           reply_markup=reply_marcup2
        )

    if query.data == "second_dish_плов":
        file = open('/home/ihyfyugfyugyugiu/second/Плов.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/Cnesswm1RJI",
           reply_markup=reply_marcup2
        )

    if query.data == "second_dish_ризотто":
        file = open('/home/ihyfyugfyugyugiu/second/Ризотто.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/fKM2bN-pYQY",
           reply_markup=reply_marcup2
        )

    if query.data == "second_dish_чахохбили":
        file = open('/home/ihyfyugfyugyugiu/second/Чахохбили.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/rfSBhEsELBA",
           reply_markup=reply_marcup2
        )


    keyboard3 = [
        [
        InlineKeyboardButton("Греческий", callback_data="salads_греческий"),
        InlineKeyboardButton("Капустный", callback_data="salads_капустный")
        ],
        [InlineKeyboardButton("Кобб салат", callback_data="salads_кобб салат" ),
            InlineKeyboardButton("Мимоза", callback_data="salads_мимоза")],
            [
        InlineKeyboardButton("Нисуаз", callback_data="salads_нисуаз"),
        InlineKeyboardButton("Салат из баклажанов", callback_data="salads_салат из баклажанов")
        ],
        [
        InlineKeyboardButton("Цезарь", callback_data="salads_цезарь"),
        InlineKeyboardButton("Яичный", callback_data="salads_яичный")
        ]

    ]
    reply_marcup3 = InlineKeyboardMarkup(keyboard3)


    if query.data == "salads_греческий":
        file = open('/home/ihyfyugfyugyugiu/salads/Греческий.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/t401o9Hhm_M",
           reply_markup=reply_marcup3
        )
    
    if query.data == "salads_капустный":
        file = open('/home/ihyfyugfyugyugiu/salads/Капустный.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/HMAHrJXYXe4",
           reply_markup=reply_marcup3
        )

    if query.data == "salads_кобб салат":
        file = open('/home/ihyfyugfyugyugiu/salads/Кобб салат.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/QAruKeKWcTI",
           reply_markup=reply_marcup3
        )

    if query.data == "salads_мимоза":
        file = open('/home/ihyfyugfyugyugiu/salads/Мимоза.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/s6UsL6vj-T0",
           reply_markup=reply_marcup3
        )


    if query.data == "salads_нисуаз":
        file = open('/home/ihyfyugfyugyugiu/salads/Нисуаз.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/WR_hRTYe-O4",
           reply_markup=reply_marcup3
        )

    if query.data == "salads_салат из баклажанов":
        file = open('/home/ihyfyugfyugyugiu/salads/Салат из баклажанов.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/vtFYPOuDYtA",
           reply_markup=reply_marcup3
        )


    if query.data == "salads_цезарь":
        file = open('/home/ihyfyugfyugyugiu/salads/Цезарь.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/U31tXg9ULa0",
           reply_markup=reply_marcup3
        )

    if query.data == "salads_яичный":
        file = open('/home/ihyfyugfyugyugiu/salads/Яичный.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/O4GaU5TwZ1Q",
           reply_markup=reply_marcup3
        )

    
    keyboard4 = [
        [
        InlineKeyboardButton("Банановый кекс", callback_data="dessert_банановый кекс"),
        InlineKeyboardButton("Домашнее мороженое", callback_data="dessert_домашнее мороженое")
        ],
        [InlineKeyboardButton("Меренговый рулет", callback_data="dessert_меренговый рулет" ),
            InlineKeyboardButton("Пончики", callback_data="dessert_пончики")],
            [
        InlineKeyboardButton("Тирамису", callback_data="dessert_тирамису"),
        InlineKeyboardButton("Шоколадная лава", callback_data="dessert_шоколадная лава")
        ],
        [
        InlineKeyboardButton("Шоколадные кексы", callback_data="dessert_шоколадные кексы"),
        InlineKeyboardButton("Яблочная шарлотка", callback_data="dessert_яблочная шарлотка")
        ]

    ]
    reply_marcup4 = InlineKeyboardMarkup(keyboard4)

    if query.data == "dessert_банановый кекс":
        file = open('/home/ihyfyugfyugyugiu/dessert/Банановый кекс.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/n2Z_t4vGjQU",
           reply_markup=reply_marcup4
        )
    
    if query.data == "dessert_домашнее мороженое":
        file = open('/home/ihyfyugfyugyugiu/dessert/Домашнее мороженое.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/coqYF0RGtC4",
           reply_markup=reply_marcup4
        )

    if query.data == "dessert_меренговый рулет":
        file = open('/home/ihyfyugfyugyugiu/dessert/Меренговый рулет.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/x77tB_SHb7M",
           reply_markup=reply_marcup4
        )

    if query.data == "dessert_пончики":
        file = open('/home/ihyfyugfyugyugiu/dessert/Пончики.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/vQFonpS_90k",
           reply_markup=reply_marcup4
        )

    if query.data == "dessert_тирамису":
        file = open('/home/ihyfyugfyugyugiu/dessert/Тирамису.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/UqswbeGreWw",
           reply_markup=reply_marcup4
        )

    if query.data == "dessert_шоколадная лава":
        file = open('/home/ihyfyugfyugyugiu/dessert/Шоколадная лава.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/FcvIAqUiIQE",
           reply_markup=reply_marcup4
        )

    if query.data == "dessert_шоколадные кексы":
        file = open('/home/ihyfyugfyugyugiu/dessert/Шоколадные кексы.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/A5WxhLw7L80",
           reply_markup=reply_marcup4
        )

    if query.data == "dessert_яблочная шарлотка":
        file = open('/home/ihyfyugfyugyugiu/dessert/Яблочная шарлотка.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/h50k7Jls48k",
           reply_markup=reply_marcup4
        )

    keyboard5 = [ 
        [
        InlineKeyboardButton("Арбузный напиток", callback_data="beverages_арбузный напиток"),
        InlineKeyboardButton("Бананово-шоколадный коктейль", callback_data="beverages_бананово-шоколадный коктейль")
        ],
        [InlineKeyboardButton("Глинтвейн", callback_data="beverages_глинтвейн" ),
            InlineKeyboardButton("Клубнично-молочный коктейль", callback_data="beverages_клубнично-молочный коктейль")],
            [
        InlineKeyboardButton("Клюквенный напиток", callback_data="beverages_клюквенный напиток"),
        InlineKeyboardButton("Молочный коктейль из киви", callback_data="beverages_молочный коктейль из киви")
        ],
        [
        InlineKeyboardButton("Мохито безалькогольный", callback_data="beverages_мохито безалькогольный"),
        InlineKeyboardButton("Шоколадный коктейль", callback_data="beverages_шоколадный коктейль")
        ]

    ]
    reply_marcup5 = InlineKeyboardMarkup(keyboard5)

    if query.data == "beverages_арбузный напиток":
        file = open('/home/ihyfyugfyugyugiu/beverages/Арбузный напиток.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/373ZWQobUWU",
           reply_markup=reply_marcup5
        )
    
    if query.data == "beverages_бананово-шоколадный коктейль":
        file = open('/home/ihyfyugfyugyugiu/beverages/Бананово-шоколадный коктейль.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/YgOPruKi8bM",
           reply_markup=reply_marcup5
        )

    if query.data == "beverages_глинтвейн":
        file = open('/home/ihyfyugfyugyugiu/beverages/Глинтвейн.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/MMnBmzirTo4",
           reply_markup=reply_marcup5
        )

    if query.data == "beverages_клубнично-молочный коктейль":
        file = open('/home/ihyfyugfyugyugiu/beverages/Клубнично-молочный коктейль.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/6MM447kP6h4",
           reply_markup=reply_marcup5
        )

    if query.data == "beverages_клюквенный напиток":
        file = open('/home/ihyfyugfyugyugiu/beverages/Клюквенный напиток.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/-zlei5ZwCeY",
           reply_markup=reply_marcup5
        )

    if query.data == "beverages_молочный коктейль из киви":
        file = open('/home/ihyfyugfyugyugiu/beverages/Молочный коктейль из киви.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/EUUEMCvUm-0",
           reply_markup=reply_marcup5
        )

    if query.data == "beverages_мохито безалькогольный":
        file = open('/home/ihyfyugfyugyugiu/beverages/Мохито безалкогольный.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/oKODXLxXtqE",
           reply_markup=reply_marcup5
        )

    if query.data == "beverages_шоколадный коктейль":
        file = open('/home/ihyfyugfyugyugiu/beverages/Шоколадный коктейль.txt', 'r', encoding='utf-8')
        text = file.read()
        update.callback_query.message.edit_text(
            text=text
        )
        context.bot.send_message(
           update.effective_chat.id,
           text = "https://youtu.be/8y7LCehjB3s",
           reply_markup=reply_marcup5
        )


FIRSTDISH = tele_button[0]
SECONDDISH = tele_button[1]
SALADS = tele_button[2]
DESSERT = tele_button[3]
BEVERAGES = tele_button[4]




updater = Updater(TOKEN, persistence=PicklePersistence(filename="bot_data"))
updater.dispatcher.add_handler(CommandHandler("start", start))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(FIRSTDISH),
    first_dish_inline_menu
    
))  

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SECONDDISH),
    second_dish_inline_menu
    
))  

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SALADS),
    salads_inline_menu
    
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(DESSERT),
    dessert_inline_menu
    
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BEVERAGES),
    beverages_inline_menu
    
))  
                            
updater.dispatcher.add_handler(CallbackQueryHandler(inline_button))
updater.start_polling()
updater.idle() 
