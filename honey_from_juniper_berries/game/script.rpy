# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gg = Character("Ты")
define narrator = nvl_narrator

#Declare music
define audio.gamemusic = "audio/background-music-1.mp3"

default player_name = ""

# The game starts here.

label start:
    play music gamemusic

    $ player_name = renpy.input("Введите ваше имя:").strip()

    while player_name == "" or len(player_name) > 16:
        if player_name == "":
            $ renpy.notify("Имя не может быть пустым. Пожалуйста, введите имя.")
        elif len(player_name) > 16:
            $ renpy.notify("Имя не может превышать 16 символов. Пожалуйста, введите имя.")

        $ player_name = renpy.input("Введите ваше имя:").strip()

    # Здесь можете использовать player_name в вашем сценарии
    # """[player_name] грустно листал бумаги, держа в руках счёты. Его жизнь была настолько скучной, насколько могла - каждый день одно и тоже.
    # Цифры уже стали мерещиться во снах. И ведь нельзя просто уйти - долги давили. Начальник требовал вернуть 100 золотых крон - страшную сумму.
    # [player_name] помнил это как вчера - 20 лет назад, когда старик Вилод еще варил мёд, [player_name] занимался транспортировкой мёда через Медолесье...
    # Но Вилод пропал вместе с его рецептом мёда, а Медолесье стало Чернолесьем. Долги росли, а фестиваль летнего солнцестояния отменялся каждый год.
    # И теперь пришлось пойти работать счётоводом, дабы выжить и оплатить долги.

    narrator """[player_name] сидел в душном подвале конторы в городе Винмор, перебирая кипы пожелтевших (и не очень) бумаг. Счёты в его руках разбивали тишину своим монотонным пощелкиванием.
    Каждый новый день был копией предыдущего - бесконечные колонки цифр, претензии ростовщиков и кредиторов, отчеты и бесконечные расписки, документы и просто бумага.

    Мысли о старом Вилоде и его волшебном мёде из можжевеловых ягод были единственным светом в этой кромешной тьме.
    [player_name] отчетливо помнил тот роковой день двадцать лет назад, когда они вместе везли последнюю партию мёда через Медолесье.
    Тогда ещё лес жил полной жизнью - деревья шептались на ветру, река звенела как хрусталь, а воздух был напоен ароматами дикого мёда и цветущих трав.
    """

    nvl clear

    narrator """Но Вилод исчез. Мёд быстро иссяк, а рецепта он не оставил. Фестивали солнцестояния начали отменять, напряжение росло. Медолесье стала поглащать тьма междоусобных войн между Винмором и соседним Тельмором, превратив его в Чернолесье.
    С тех пор люди не слышали звонкие голоса детей, пение птиц и шелест листвы - только мрачная, даже пугающая растительность.

    [player_name] надеялся что вот-вот Вилод вернется. Но день за днем, декада за декадой, никто не приходил. Он оказался в долговой яме глубиной в сто золотых крон.
    Даже в те времена такую сумму было тяжело заработать, а сейчас подавно. Начальник грозил отобрать имущество и дом.

    Теперь вместо ароматных медовых троп он блуждал в лабиринтах бухгалтерских отчётов, а вместо душистого ветра Медолесья вдыхал запах плесени и пыли.
    Его пальцы машинально перебирали костяшки счёт, а глаза безжизненно скользили по колонкам цифр, не видя в них ни смысла, ни надежды.

    [player_name] ждал чуда, не зная какого. Он просто мечтал чтобы было как раньше...

    Вот так и проходит жизнь: в ожидании чуда, которое, кажется, никогда не случится.
    """

    nvl clear

    gg "Опять недоимка по курятнику! Черт, да когда эти крестьяне поймут что я просто считаю!"
    gg "Еще и этот Гусо требует быстрее посчитать сумму за его кобыл. Мда..."

    "[player_name] взглянул на пустую склянку мёда из можжевеловых ягод от Вилода. Он берет ослабшими руками и смотрит на нее, будто она поможет ему."

    gg "Эх, Вилод... Помнится, ты говорил что настоящий мёд варится из свободы, а не из купленных ингридиентов. Варится на природе, а не в затлухом подвале..."
    gg "А теперь я здесь. Сижу в сыром подвале, утяжеленный долгами..."
    gg "Испить бы твоего доброго мёда... Фирменного, с можжевеловыми ягодами..."

    # # Show a background. This uses a placeholder by default, but you can
    # # add a file (named either "bg room.png" or "bg room.jpg") to the
    # # images directory to show it.

    # scene bg room

    # # This shows a character sprite. A placeholder is used, but you can
    # # replace it by adding a file named "eileen happy.png" to the images
    # # directory.

    # show eileen happy

    # # These display lines of dialogue.

    # s "Привет."

    # s "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat erat libero, ac feugiat diam pharetra tincidunt.
    # Nullam tellus sem, semper sit amet tincidunt ac, dapibus at mauris."

    # menu:
    #     "Option 1":
    #         "You chose option 1."
    #     "Option 2":
    #         "You chose option 2."
    #     "Option 3":
    #         "You chose option 3."
    #     "Option 4 is a bit longer, a tiny tiny bit longer so the button is bigger but just a bit":
    #         "You chose option 4 which is a bit longer I admit."
    #     "Unlock some Gallery images":
    #         ##Condition defined in gallery/galleryA.rpy, gallery/galleryB.rpy etc...)
    #         $ persistent.pg1_1 = True
    #         $ persistent.pg1_2 = True
    #         $ persistent.pg1_3 = True
    #         $ persistent.pg1_4 = True
    #         $ persistent.pg1_5 = True
    #         $ persistent.pg1_6 = True
    #         $ persistent.pg1_7 = True
    #         $ persistent.pg1_8 = True
    #         $ persistent.pg1_9 = True


    # s "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat erat libero, ac feugiat diam pharetra tincidunt. Nullam tellus sem, semper sit amet tincidunt ac, dapibus at mauris. "
    # s "Donec sit amet placerat risus. Nulla facilisi. Sed maximus nisi et nulla facilisis luctus. Proin velit purus, volutpat id lectus sed, scelerisque fringilla velit."
    # # This ends the game.

    return
