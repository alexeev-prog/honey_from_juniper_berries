# Файл: interface.rpy
# Основной игровой интерфейс с инвентарем, монетами, записками и дневником в фэнтези-стиле

default gold_coins = 5
default vilod_notes = ["Записки вилода"]
default diary_entries = ["Дневник"]
default inventory = [None] * 9  # 9 слотов инвентаря

init python:
    # Класс для предметов инвентаря
    class InventoryItem:
        def __init__(self, name, icon=None, description="", stackable=False, quantity=1):
            self.name = name
            self.icon = icon
            self.description = description
            self.stackable = stackable
            self.quantity = quantity

    # Функции для работы с системой
    def add_coins(amount, source=""):
        global gold_coins
        gold_coins += amount
        add_diary_entry(f"Получено {amount} крон: {source}")

    def add_vilod_note(note_text):
        global vilod_notes
        vilod_notes.append(note_text)
        add_diary_entry(f"Найдена новая записка Вилода")

    def add_diary_entry(entry_text):
        global diary_entries
        diary_entries.append(entry_text)

    def add_to_inventory(item, slot=None):
        global inventory

        # Поиск свободного слота или стека
        if slot is None:
            for i in range(len(inventory)):
                if inventory[i] is None:
                    inventory[i] = item
                    return True
                elif inventory[i].name == item.name and inventory[i].stackable:
                    inventory[i].quantity += item.quantity
                    return True
        elif 0 <= slot < len(inventory):
            if inventory[slot] is None:
                inventory[slot] = item
                return True
            elif inventory[slot].name == item.name and inventory[slot].stackable:
                inventory[slot].quantity += item.quantity
                return True

        return False  # Нет места

# Стили для интерфейса
init:
    style interface_frame:
        background Frame("gui/frame.png", 25, 25)
        padding (15, 12)  # Уменьшенные отступы
        xmargin 0
        ymargin 0

    style interface_button:
        background Frame("gui/button/idle_background.png", 12, 12)
        hover_background Frame("gui/button/hover_background.png", 12, 12)
        selected_background Frame("gui/button/hover_background.png", 12, 12)
        padding (12, 8)  # Уменьшенные отступы
        xminimum 250  # Увеличенная минимальная ширина
        yminimum 45  # Немного уменьшенная высота

    style interface_button_text:
        font gui.interface_text_font
        size 22  # Немного уменьшенный размер
        color "#f0e6d2"
        hover_color "#ffffff"
        outlines [(1, "#3c1f14", 0, 0)]
        text_align 0.5
        xalign 0.5
        yalign 0.5

    style slot_button:
        background Frame("gui/button/slot_idle_background.png", 8, 8)
        hover_background Frame("gui/button/slot_hover_background.png", 8, 8)
        selected_background Frame("gui/button/slot_hover_background.png", 8, 8)
        padding (0, 0)
        xsize 100  # Немного уменьшенный размер
        ysize 100  # Немного уменьшенный размер

    style slot_button_text:
        font gui.interface_text_font
        size 16  # Немного уменьшенный размер
        color "#f0e6d2"
        outlines [(1, "#3c1f14", 0, 0)]
        text_align 0.5
        xalign 0.5

    # Новые стили для ячеек с другими цветами
    style bronze_slot_button:
        background Solid("#8c7853")  # Бронзовый цвет
        hover_background Solid("#a89776")  # Светло-бронзовый
        padding (0, 0)
        xsize 100  # Немного уменьшенный размер
        ysize 100  # Немного уменьшенный размер

    style silver_slot_button:
        background Solid("#c0c0c0")  # Серебряный цвет
        hover_background Solid("#d9d9d9")  # Светло-серебряный
        padding (0, 0)
        xsize 100  # Немного уменьшенный размер
        ysize 100  # Немного уменьшенный размер

    style info_header:
        font gui.name_text_font
        size 28  # Немного уменьшенный размер
        color "#f0e6d2"
        outlines [(2, "#3c1f14", 0, 0)]
        text_align 0.5
        xalign 0.5

    style info_text:
        font gui.text_font
        size 22  # Немного уменьшенный размер
        color "#f0e6d2"
        outlines [(1, "#3c1f14", 0, 0)]
        text_align 0.5
        xalign 0.5

# Экран основного игрового интерфейса
screen game_interface():
    zorder 100
    fixed:
        # Верхняя панель - монеты и записки (слева)
        frame:
            style "interface_frame"
            pos (15, 15)  # Уменьшенные отступы
            hbox:
                spacing 20  # Уменьшенный промежуток

                # Отображение золотых монет
                button:
                    style "interface_button"
                    background Frame("gui/button/idle_background.png", 12, 12)
                    hover_background Frame("gui/button/hover_background.png", 12, 12)
                    text "Кроны: [gold_coins]" style "interface_button_text"
                    xminimum 220  # Увеличенная ширина

                # Кнопка записок Вилода
                button:
                    style "interface_button"
                    action Show("vilod_notes_screen")
                    vbox:
                        text "Записки Вилода" style "interface_button_text"
                        text "([len(vilod_notes)])" style "interface_button_text" size 18
                    xminimum 220  # Увеличенная ширина

        # Кнопка дневника (справа)
        frame:
            style "interface_frame"
            pos (1550, 15)  # Перемещена выше и левее
            button:
                style "interface_button"
                action Show("diary_screen")
                text "Дневник" style "interface_button_text"
                xminimum 150

        # Панель инвентаря справа (вертикально)
        frame:
            style "interface_frame"
            background Frame("gui/frame.png", 25, 25)
            align (1.0, 0.5)  # Правая сторона, по центру вертикально
            offset (-30, 0)   # Сдвиг от края
            ysize 900         # Уменьшенная высота
            xsize 140         # Уменьшенная ширина

            vbox:
                align (0.5, 0.5)
                spacing 12  # Уменьшенный промежуток между слотами

                # 9 слотов инвентаря
                for i, item in enumerate(inventory):
                    button:
                        # Чередование цветов ячеек
                        if i % 2 == 0:
                            style "bronze_slot_button"
                        else:
                            style "silver_slot_button"

                        action If(item, true=Show("item_info", item=item))

                        if item:
                            vbox:
                                align (0.5, 0.5)
                                spacing 4

                                if item.icon:
                                    add item.icon size (50, 50) align (0.5, 0.5)
                                else:
                                    text "?" size 30 style "slot_button_text" align (0.5, 0.5)

                                text item.name size 18 style "slot_button_text"

                                if item.stackable and item.quantity > 1:
                                    text "x[item.quantity]" size 16 style "slot_button_text" align (1.0, 1.0) offset (40, -30)
                        else:
                            text "Пусто" size 18 style "slot_button_text" align (0.5, 0.5)

# Экран просмотра записок Вилода
screen vilod_notes_screen():
    zorder 200
    modal True

    default current_note = 0

    frame:
        style "interface_frame"
        background Frame("gui/frame.png", 25, 25)
        xalign 0.5
        yalign 0.5
        xsize 1300  # Немного уменьшенный размер
        ysize 750   # Немного уменьшенный размер

        vbox:
            spacing 20  # Уменьшенный промежуток
            xfill True

            # Заголовок
            label "Записки Вилода" style "info_header"

            # Область с текстом записки
            frame:
                background Frame("gui/button/idle_background.png", 20, 20)
                padding (20, 20)  # Уменьшенные отступы
                xfill True
                ysize 550  # Немного уменьшенная высота

                viewport:
                    id "notes_viewport"
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    yinitial 0.0

                    text vilod_notes[current_note] style "info_text" slow_cps 30

            # Навигация
            hbox:
                xalign 0.5
                spacing 40  # Уменьшенный промежуток

                textbutton "< Предыдущая":
                    style "interface_button"
                    action If(current_note > 0, SetScreenVariable("current_note", current_note - 1))
                    sensitive current_note > 0
                    xminimum 150  # Увеличенная ширина

                textbutton "Закрыть":
                    style "interface_button"
                    action Hide("vilod_notes_screen")
                    xminimum 150

                textbutton "Следующая >":
                    style "interface_button"
                    action If(current_note < len(vilod_notes)-1, SetScreenVariable("current_note", current_note + 1))
                    sensitive current_note < len(vilod_notes)-1
                    xminimum 150

            # Индикатор текущей записки
            text "Записка [current_note+1] из [len(vilod_notes)]" style "info_text" size 22 xalign 0.5

# Экран дневника игрока
screen diary_screen():
    zorder 200
    modal True

    default current_entry = 0

    frame:
        style "interface_frame"
        background Frame("gui/frame.png", 25, 25)
        xalign 0.5
        yalign 0.5
        xsize 1300  # Немного уменьшенный размер
        ysize 750   # Немного уменьшенный размер

        vbox:
            spacing 20  # Уменьшенный промежуток
            xfill True

            # Заголовок
            label "Дневник [player_name]" style "info_header"

            # Область с текстом записи
            frame:
                background Frame("gui/button/idle_background.png", 20, 20)
                padding (20, 20)  # Уменьшенные отступы
                xfill True
                ysize 550  # Немного уменьшенная высота

                viewport:
                    id "diary_viewport"
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    yinitial 0.0

                    text diary_entries[current_entry] style "info_text" slow_cps 30

            # Навигация
            hbox:
                xalign 0.5
                spacing 40  # Уменьшенный промежуток

                textbutton "< Предыдущая":
                    style "interface_button"
                    action If(current_entry > 0, SetScreenVariable("current_entry", current_entry - 1))
                    sensitive current_entry > 0
                    xminimum 150

                textbutton "Закрыть":
                    style "interface_button"
                    action Hide("diary_screen")
                    xminimum 150

                textbutton "Следующая >":
                    style "interface_button"
                    action If(current_entry < len(diary_entries)-1, SetScreenVariable("current_entry", current_entry + 1))
                    sensitive current_entry < len(diary_entries)-1
                    xminimum 150

            # Индикатор текущей записи
            text "Запись [current_entry+1] из [len(diary_entries)]" style "info_text" size 22 xalign 0.5

# Экран информации о предмете
screen item_info(item):
    zorder 300
    modal True

    frame:
        style "interface_frame"
        background Frame("gui/frame.png", 25, 25)
        xalign 0.5
        yalign 0.5
        xsize 600  # Немного уменьшенный размер
        ysize 450  # Немного уменьшенный размер

        vbox:
            spacing 20  # Уменьшенный промежуток
            align (0.5, 0.5)

            # Название предмета
            label item.name style "info_header"

            # Иконка предмета
            if item.icon:
                add item.icon size (80, 80) align (0.5, 0.5)
            else:
                text "?" size 50 style "info_text" align (0.5, 0.5)

            # Описание предмета
            frame:
                background Frame("gui/button/idle_background.png", 20, 20)
                padding (20, 20)  # Уменьшенные отступы
                xfill True
                ysize 160  # Немного уменьшенная высота

                text item.description style "info_text" align (0.5, 0.5)

            # Количество (для стакаемых предметов)
            if item.stackable and item.quantity > 1:
                text "Количество: [item.quantity]" style "info_text" size 22

            # Кнопка закрытия
            textbutton "Закрыть":
                style "interface_button"
                action Hide("item_info")
                xalign 0.5
