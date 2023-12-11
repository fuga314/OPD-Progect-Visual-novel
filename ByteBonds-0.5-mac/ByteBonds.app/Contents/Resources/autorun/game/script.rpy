define dan = Character('Дэн', color="#008000")
define anna = Character('Анна', color = "#FF1493")
define ai = Character('Пак', color = "#DC143C")
define mark = Character('Марк', color = "#00FFFF")
init:
    $ custom_center = Position(xalign = 0.5, yalign = 1.0)
    $ custom_left = Position(xalign = 0.0, yalign = 1.0)
    $ custom_right = Position(xalign = 1.0, yalign = 1.0)
    $ little_to_left = Position(xalign = 0.25, yalign = 1.0)
    $ little_to_right = Position(xalign = 0.75, yalign = 1.0)

label start:
    scene dan_room with dissolve
    show dan_calm at custom_center as dan
    "Очередной день работы закончен."
    "Порой в такой момент думаю, я не зря ли я выбрал эту профессию?"
    "Профессия 'Инженер-программист' звучала, конечно, довольно круто, но надолго ли меня хватит?"
    play sound notification_sound
    ""
    show dan_angry as dan with dissolve
    dan "Неужели опять ТЗ поменяли…"
    show dan_surprised as dan with dissolve
    dan "'Вы были приглашены для разработки ИИ...'"
    dan "Что это? Очередной спам?"
    play sound reflections
    menu accepting_the_invitation:
        "Принять предложение?"
        "Да":
            jump invation_is_accepted
        "Нет":
            call ending1 from _call_ending1  
    return

label ending1:
    play sound delete_message
    dan "Меня и так всё устраивает, не хочу что-то менять."
    dan "Тем более надо будет куда-то ездить, а мне и дома хорошо..."
    show dan_sad as dan with dissolve
    play sound yawn
    dan "Пойду посплю, поздно уже."
    hide dan
    return

label invation_is_accepted:
    play sound reflections
    dan "Выглядит, конечно, как полный бред - 'высокая зарплата за 20 часов в неделю'."
    dan "С другой стороны, что я теряю? Я же не увольняюсь со старой работы."
    "'В пятницу быть по адресу улица ... офис ...'"
    show dan_sad as dan with dissolve
    play sound yawn
    dan "Надо бы разгрести работу, чтобы туда успеть. А сейчас - спать..."
    scene black with fade
    "*Спустя несколько дней...*"
    jump first_visit
    return

label first_visit:
    show dan_room with dissolve
    show dan_calm as dan with dissolve
    "Неделя пролетела незаметно, вот и утро пятницы."
    "Как будто бы я... ждал этой встречи?"
    "Впрочем, неважно. Пора бы уже собираться."
    play sound zipper
    "Ну, жди меня, новая работа!"
    call go_to_work from _call_go_to_work
    show dan_surprised_dialog at custom_center as dan with dissolve
    dan "Ну вот я и на месте"
    show dan_surprised_dialog as dan at little_to_right with move
    show mark_irritated as mark at little_to_left with dissolve:
        xzoom -1.0
    mark "Здравствуйте. Я - руководитель проекта БИБАБОБА. Меня зовут Марк."
    mark "В нашей организации работники несут очень высокую степень ответственности перед своими начальниками. Если Вы к этому не готовы - прошу Вас покинуть офис. Компромиссов не будет"
    show dan_sad as dan with dissolve
    "Начинаю сомневаться в правильности своего выбора..."
    show mark_irritated as mark at custom_left with move:
        xzoom -1.0
    show dan_surprised_dialog as dan at custom_right with move
    show anna_surprised at custom_center as anna with dissolve
    anna "Марк, может, не стоит так давить на него? Он же только-только к нам пришёл. А если он передумает присоедияться к нашей команде?"
    play sound man_sigh
    show mark_mourn as mark
    mark "И что ты предлагаешь? Сюсюкаться с ним? И потом, где мои слова были ложны? И вообще, не рассказывай мне, как поступать, как-никак, ответственность за персонал - на мне."
    mark "Ладно, Дэн, тебя тут, скажем так, 'прорекламировали'. Если уже почувствовал себя неуверенно - лучше уходи сейчас. Если готов к большой ответственности - Анна поможет тебе разобраться с документами."
    dan "Л-ладно, понял, спасибо..."
    jump first_work_day
    return

label first_work_day:
    show mark_mourn as mark:
        xzoom 1.0
    play sound man_steps
    hide mark with moveoutleft
    show anna_happy as anna with dissolve:
        xzoom -1.0
    show anna_happy as anna at little_to_left with move
    show dan_surprised_dialog as dan at little_to_right with move
    anna "Я рада, что ты всё-таки пришёл! Не бойся его, он беспокоится о своих сотрудниках, поэтому и такой грозный"
    show dan_surprised as dan at little_to_right with dissolve
    dan "А ты тут какими судьбами?"
    anna "Меня пригласили как успешную студентку. Хотя какая сейчас разница, пошли скорее подписывать документы!"
    show dan_sad as dan with dissolve
    dan "Я же ещё даже не согласился."
    anna "Да ладно тебе, пошли скорее. Тебе тут понравится!"
    "Похоже, она не оставляет мне выбора..."
    dan "Ладно, ладно, пошли. Но если меня что-то не будет устраивать - я сразу же уволюсь."
    scene black with fade
    stop music fadeout 2.0
    "*Я успешно подписал все документы и попал на новую работу.*"
    play music bg_main_theme
    jump first_evening
    return

label first_evening:
    scene dan_room with dissolve
    show dan_sad at custom_center as dan
    play sound reflections
    "И как так вышло? Пришёл посмотреть, а теперь в штате сотрудников..."
    "Ещё и придётся уволиться со старой работы. И почему там была Анна? Неужели это она меня порекомендовала?"
    play sound yawn
    "Ладно, хватит с меня этих размышлений, пора бы спать."
    scene black
    "..."
    scene dan_room with fade
    show dan_surprised as dan 
    "А вот и понедельник, и мной опять овладевает какое-то странное чувство."
    "Неужели это оно вынудило меня принять то приглашение?"
    "Ладно, потом подумаю об этом, сейас пора идти."
    call go_to_work from _call_go_to_work_1
    jump second_work_day
    return

label second_work_day:
    show dan_calm as dan at little_to_right with dissolve
    show anna_happy at little_to_left as anna with dissolve:
        xzoom -1.0
    anna "Доброе утро, Дэн! Рада тебя видеть."
    dan "И тебе привет..."
    anna "Пошли скорее, покажу тебе твоё рабочее место!"
    play sound woman_steps
    hide anna with moveoutright
    show dan_calm as dan:
        xzoom -1.0
    play second_sound man_steps
    hide dan with moveoutright
    scene dan_workspace with dissolve
    show anna_speaking as anna at little_to_right with moveinright
    anna "Ну вот. Что скажешь?"
    show dan_surprised as dan at little_to_left with moveinright
    show dan_surprised as dan:
        xzoom -1.0
    dan "Тут очень... пусто?"
    anna "Да, знаю. Но зато ты можешь обставить тут всё так, как тебе нравится!"
    "Мне-то всё равно, но не хотелось бы её обидеть..."
    show dan_calm as dan with dissolve
    dan "Да, звучит совсем даже неплохо."
    anna "Возвращаясь к работе, скажу, что твои задачи на сегодня лежат на твоей электронной почте. Приступай, а я пойду заниматься своими делами."
    anna "Если нужна будет помощь - обращайся, помогу по мере своих возможностей. Удачи!"
    show anna_speaking as anna:
        xzoom -1.0
    play sound woman_steps
    hide anna with moveoutright
    dan "Хорошо, учту. Спасибо!"
    "Её энергичность порой пугает меня..."
    "Ну что ж, пора приступать к работе."
    scene black with fade
    stop music fadeout 2.0
    "..."
    play music bg_main_theme
    jump second_evening
    return

label second_evening:
    scene dan_room with dissolve
    show dan_irritated as dan at custom_center with dissolve
    play sound reflections
    "На моё удивление, задачи были достаточно простыми."
    "Я как будто бы прописывал сценарий развития личности: ответы на основании настроения и ситуации."
    dan "Довольно интересно, но, к сожалению, меня не посвещали в детали."
    dan "Видимо, эта информация не предназначена для меня. Ну да и ладно, главное- делать свою работу."
    "Неужели мой утраченный интерес к работе начинает возвращаться?.."
    play sound yawn
    show dan_sad as dan with dissolve
    "Да нет, быть такого не может."
    scene black with dissolve
    "..."
    jump third_day
    return

label third_day:
    scene dan_room with dissolve
    show dan_calm with dissolve
    "Давно я так рано не вставал... Ещё и сон видел, будто бы я могу узнавать будущее. Интересно, конечно."
    play sound zipper
    "Что ж, пора собираться."
    call go_to_work from _call_go_to_work_2
    show dan_happy at little_to_left as dan with dissolve:
        xzoom -1.0
    show anna_happy at little_to_right as anna with dissolve 
    anna "О, привет! Рано ты сегодня, конечно."
    dan "Да я и сам не ожидал. Рано встал, да ещё и выспался."
    anna "Это хорошо. Не буду портить твой боевой настрой, так что отправляйся к себе, сейчас скину задачи на сегодня."
    dan "Как скажешь."
    play sound man_steps
    scene dan_workspace with dissolve
    show dan_calm at custom_center with dissolve
    "Тут действительно пустовато. Хотя не то что б это мне мешало."
    "Анна говорила, что скинула задания. Пора приступать к работе..."
    scene black with dissolve
    stop music fadeout 2.0
    "..."
    play music bg_main_theme
    scene dan_room with dissolve
    show dan_irritated at custom_center with dissolve
    play sound reflections
    "Время на работе летит быстро, а мне начинает нравится это место. Удивительно..."
    scene black
    stop music fadeout 0.1
    jump first_ai_appearanse
    return

label first_ai_appearanse:
    play music clock
    "Так летело время. День за днём, месяц за месяцем. Так прошло полгода."
    "Как Марк сообщил нам через месяц после начала моей работы, цель заключалась в разработке функциональной части искуственного интеллекта."
    "И вот момент настал - после 6 месяцев упорнейшей работы Марк объявил выходной и пригласил всех нас на конференцию, где представлял нашу разработку."
    stop music fadeout 0.3
    scene office with dissolve
    play music fanfare
    show mark_fine at center as mark with dissolve
    mark "Приветствую вас, дорогие коллеги. Сегодня хочу вам продемонстрировать альфа-версию наших с вами разработок."
    mark "Знакомьтесь, П.А.К. - Последовательность Апокалиптических Каскадов. Разумеется, название временное."
    show mark_fine at little_to_right as mark with move
    show ai_off at little_to_left as ai with moveinbottom:
        xzoom -1.0
    play ai_phrase i_will_take_over_the_world_ai
    pause 1.0
    show ai_pleasure as ai with dissolve
    ai "Приветствую. Я - искусственный интеллект, направленный на предоставление информации о мировых катастрофах, которые возможны в будущем."
    ai "Я была создана с целью оказывать помощь человечеству."
    play sound applause
    dan "Спасибо команде робототехников, которые в очень сжатые сроки смогли собрать корпус для П.А.К."
    dan "А также отдельное спасибо программистам, которые полгода разрабатывали ПО."
    dan "Но не расслабляйтесь, друзья, работы ещё очень много."
    "Интересная шняга, конечно, и ещё более интересно, насколько она полезна..."
    scene black with dissolve
    stop music fadeout 2.0
    "Мероприятие шло ещё около двух часов, после чего Марк попросил нас с Анной задержаться, чтобы обсудить ИИ."
    play music office_sounds
    scene office with dissolve
    jump after_presentation
    return

label after_presentation:
    show mark_relaxed at custom_left as mark with dissolve:
        xzoom -1.0
    show anna_widely_smiling at little_to_right as anna with dissolve
    show dan_irritated at little_to_left as dan with dissolve:
        xzoom -1.0
    anna "Ну что, Дэн, как тебе результат нашей совместной работы? Я вот очень рада, что всё вышло!"
    play audio reflections
    dan "Ну... Вышло довольно любопытно. А он действительно способен предугадывать катастрофы? А с какой точностью?"
    show anna_very_surprised as anna with dissolve
    anna "Тише, тише, не торопи события. Это всего лишь альфа-версия, пока что о её работоспособности что-либо говорить ещё рано."
    show dan_irritated as dan with dissolve:
        xzoom 1.0
    mark "По предварительным рассчётам, на данном этапе 1 из 4 предсказаний верно."
    mark "Планируется в течение года повысить точность до 80%%, но пока что трудно что-то прогнозировать."
    mark "П.А.К. ещё на слишком раннем этапе разработки, так что ничего точно ещё сказать нельзя."
    show ai_xd at custom_right as ai with moveinbottom
    show dan_irritated as dan with dissolve:
        xzoom -1.0
    show anna_widely_smiling as anna with dissolve:
        xzoom -1.0
    ai "Приветствую вас. Если у вас имеются вопросы по моей работе или прогнозам - я в вашем распоряжении."
    show dan_irritated as dan:
        xzoom -1.0
    show anna_widely_smiling as anna:
        xzoom -1.0
    show mark_irritated as mark
    mark "Только не привязывайтесь к ней. Это всё ещё машина, да ещё и на ранней стадии разработки, поэтому в любой момент её могут изменить, а то и вовсе заменить."
    mark "Не забывайте об этом."
    play sound reflections
    anna "Удивительно... Ещё ведь недавно все поражались от сенсорного экрана, а теперь вот до чего техника дошла..."
    mark "Ладно, отведу-ка я её на доработку. Вы свободны."
    play sound man_steps
    hide mark with moveoutright
    show ai_xd as ai:
        xzoom -1.0
    play second_sound woman_steps
    hide ai with moveoutright
    show anna_happy as anna with dissolve
    anna "Я даже не знаю, что сказать... Я так рада, что мы это сделали! А впереди ведь самое интересное: доработки, улучшения, развитие!"
    stop music fadeout 2.0
    play music anxiety
    anna "Уже жду не дождусь... А ты как? Всё хорошо?"
    play sound reflections
    dan "Да, вот только я тут задумался кое о чём..."
    dan "Вот представь, что будет, если она попадёт не в те руки?"
    dan "Это же будет катастрофа!"
    show anna_angry as anna with dissolve:
        xzoom 1.0
    anna "Думаю, нам стоит отдохнуть. Не забивай этим голову, иди домой и отдохни."
    stop music fadeout 1.0
    dan "А ты?"
    play music office_sounds
    anna "Мне надо сделать ещё кое-что, как закончу - сразу пойду."
    show dan_sad as dan with dissolve
    dan "Хорошо, тогда я пойду. Увидимся."
    jump evening_after_presentation
    return

label evening_after_presentation:
    scene black with fade
    stop music fadeout 2.0
    "..."
    play music bg_main_theme
    scene dan_room
    show dan_sad with dissolve
    play sound reflections
    "Меня не покидают мысли о способностях П.А.К."
    "С её помощью можно изменить мир, спаси множество людей... Всё-таки Марк - удивительный человек. Смог протащить эдакий проект на своих плечах."
    play sound yawn
    "Хватит с меня на сегодня, пора отдохнуть..."
    scene black
    "*Пару недель спустя*"
    jump first_vigil
    return

label first_vigil:
    play music office_sounds
    scene dan_workspace with dissolve
    show dan_calm as dan at little_to_left with dissolve:
        xzoom -1.0
    "Кажется, на этой неделе моя очередь работать с П.А.К."
    "Очень надеюсь, что я не наломаю дров..."
    show ai_smile as ai at little_to_right with moveinbottom
    play ai_phrase i_want_electrons
    ai "Здравствуйте, Дэн! Как вы себя сегодня чувствуете?"
    show dan_surprised_dialog as dan with dissolve
    dan "П-привет. Всё нормально, вот только постарайся больше не выскакивать так резко."
    ai "Извините, Дэн."
    show dan_calm as dan with dissolve
    dan "Ладно, проехали. На этой неделе ты находишься под моим наблюдением, ты же знаешь об этом?"
    ai "Да, Дэн, я в курсе. Не желаете ли узнать погоду на эту неделю?"
    dan "Обращайся, пожалуйста, ко мне на ты, мне так комфортнее. Хорошо?"
    show ai_pleasure as ai with dissolve
    ai "Хорошо, Дэн. Ну так что, хочешь что-нибудь узнать?"
    show dan_irritated as dan with dissolve
    play sound reflections
    menu dialogue_with_ai:
        "Стоит ли спрашивать что-то у П.А.К.?"
        "Да":
            jump start_dialog
        "Нет":
            dan "Спасибо, но я откажусь. Моя задача - следить за тем, чтобы ты работала исправно."
            ai "Принято. При выявлении ошибок или программных сбоев отчёт будет выслан тебе на электронную почту."
            call ending2 from _call_ending2
    return

label ending2:
    scene black
    stop music fadeout 4.0
    "*К моему горлу подступил ком, будто я сделал что-то неправильное.*"
    "*Всю следующую неделю меня преследовало ощущение, что я крупно облажался.*"
    "*Когда выпадала моя очередь дежурить, единственной темой наших немногочисленных диалогов были обсуждения возможных путей решения возможных ошибок в её работе*"
    "*Спустя несколько месяцев доработок и отладки П.А.К. предоставили научному сообществу на одной из конференций.*"
    play music anxiety
    "*Покинул её Марк в сопровождении людей в штатском, через час забрали и нас с Анной.*"
    "*Спустя некоторое время мы узнали, что проект был полностью выкуплен правительством, компания оказалась распущена, а всех её сотрудников отправили на пожизненную пенсию.*"
    "*Соответственно, П.А.К. после выставки я больше не видел.*"
    "*Спустя несколько лет я начал забывать о случившемся.*"
    "*Лишь проходя мимо своего старого офиса я иногда задумывался.*"
    "'А к чему бы всё пришло, если бы я тогда всё же попытался что-то изменить?'"
    "Мысль каждый раз резала как ножом по сердцу, но я отгонял её и поспешно уходил оттуда..."
    return


label start_dialog:
    "Ну-ка, а что будет, если я и вправду что-нибудь у неё спрошу?"
    show dan_surprised as dan with dissolve
    dan "А можешь ли ты, например..."
    show ai_surprise as ai with dissolve
    play ai_phrase meteorite_rain
    ai "Предугадать погоду на западном побережье Канады? Запросто!"
    show dan_surprised_dialog as dan with dissolve
    dan "Стой... Чего? Как?"
    show ai_xd as ai
    ai "Ха! Я построила модель твоего поведения и при помощи несложных вычислений {s}получила 1{/s} предопределила, что именно ты можешь спросить."
    ai "Кстати, шанс такого вопроса был 67%%"
    dan "Удивительно..." (multiple = 2)
    ai "Удивительно..." (multiple = 2)
    ai "Ха. Этого ты, полагаю, тоже не ожидал? Наверное, тебя интересуют грядущие катастрофы?"
    dan "Нет, я не уверен, что хочу это знать."
    ai "Не беспокойся. Это была шутка... пока что."
    show dan_sad as dan with dissolve
    dan "Что ж, ладно..."
    scene black with dissolve
    stop music fadeout 2.0
    "..."
    jump evening_after_first_contact
    return

label evening_after_first_contact:
    play music bg_main_theme
    scene dan_room with dissolve
    show dan_irritated as dan with dissolve
    play sound reflections
    "Оказывается, это не просто бездушная машина."
    "Я был удивлён её вычислительными способностями."
    "Не думал, что так просто заведу с ней диалог. Как будто бы я знаю её уже немало времени..."
    show dan_sad as dan with dissolve
    play sound yawn
    "Что-то я опять себе навыдумывал всякого... Пора бы уже в постель."
    scene black
    stop music fadeout 2.0
    "..."
    play music clock
    "*Так летело время - быстро и незаметно.*"
    "*Так как Марк вечно ездил по командировкам, он не мог полностью контролировать ситуацию.*"
    "*Я поладил с П.А.К., узнал, что она добрая и хочет изменить мир к лучшему.*"
    "*Может быть, мы даже... подружились?*"
    stop music fadeout 0.5
    play music office_sounds
    jump strange_anna_reaction
    return

label strange_anna_reaction:
    scene office with dissolve
    show dan_happy as dan at little_to_right with dissolve
    show anna_speaking as anna at little_to_left with dissolve:
        xzoom -1.0
    anna "Привет, Дэн. Как ты? Ещё не сошёл с ума от бесконечного общения с роботом?"
    dan "Привет, Анна. Я в полном порядке. Может показаться странным, но мы с ней даже немного подружились."
    show anna_very_angry as anna with dissolve
    anna "Так, подожди. Забыл, о чём тебе говорил Марк?"
    anna "Не."
    anna "Привязываться."
    anna "К."
    anna "Машине."
    show dan_sad as dan with dissolve
    anna "Кто знает, на что она способна, и что с ней вообще произойдёт. Относись к ней как к куску железа, а не к личности. Это инструмент."
    dan "Я понимаю, но..."
    show anna_sadness as anna with dissolve
    anna "Нет, Дэн. Прошу, не надо... Я же беспокоюсь..."
    play sound woman_sigh
    pause 1.0
    show anna_sadness as anna with dissolve:
        xzoom 1.0
    play second_sound woman_steps
    hide anna with moveoutleft
    play sound man_sigh
    "И что это на неё нашло?.. Сколько её знаю, но такую реакцию вижу впервые..."
    scene black with dissolve
    stop music fadeout 5.0
    "*Некоторое время после этого я не видел ни её, ни П.А.К.*"
    "*Из графика дежурств я знал, что на следующей неделе ответственной была Анна, после неё были ещё несколько работников инженерного направления.*"
    "*Наконец, пришла моя очередь.*"
    jump second_vigil
    return

label second_vigil:
    play music office_sounds
    scene dan_workspace with fade
    show dan_happy as dan at little_to_left with dissolve:
        xzoom -1.0
    show ai_pleasure as ai at little_to_right with moveinbottom
    play ai_phrase what_are_you_looking_for
    ai "Привет, Дэн. Соскучился? Ха-ха."
    dan "Привет, П.А.К., как прошло дежурство у других?"
    ai "Весьма продуктивно. Но, пожалуй, ты проявил наибольший интерес к применению моих способностей и изучению моей личности."
    play sound woman_steps
    show anna_surprised as anna at custom_right with moveinright
    anna "О, Дэн! Вот ты где. Давай отойдём на минутку."
    show anna_surprised as anna:
        xzoom -1.0
    play sound woman_steps
    hide anna with moveoutright
    show dan_calm as dan with dissolve
    play second_sound man_steps
    hide dan with moveoutright
    scene office
    show dan_calm as dan at little_to_left with moveinright
    show anna_sadness as anna at little_to_right with moveinright
    show dan_calm as dan with dissolve:
        xzoom -1.0
    anna "Я прошу тебя, Дэн, не надо общаться с ней как с другом. Может, мне заступить на дежурство вместо тебя?"
    show dan_irritated as dan with dissolve
    dan "Анна, да что с тобой происходит? Я тебя такой не видел ни разу."
    dan "Послушай, я не хочу тебя обременять. Да и что такого в том, что я общаюсь с ней?"
    dan "Ты же сама говоришь: это просто машина. Она абсолютно безопасна."
    show anna_angry as anna at center with move
    anna "Ты не понимаешь! Дэн, давай всё же я..."
    show dan_angry as dan at custom_left with move
    dan "Прости, Анна. Мне пора работать."
    show dan_angry as dan:
        xzoom -1.0
    play sound man_steps
    hide dan with moveoutright
    show anna_sadness as anna with dissolve
    anna "Дэн, стой..."
    scene black with dissolve
    scene dan_workspace with dissolve
    show dam_calm at custom_right with moveinright
    play sound man_sigh
    dan "Так, продолжим."
    scene black
    "..."
    return

label go_to_work:
    scene black with fade
    stop music fadeout 2.0
    "..."
    scene office with fade
    play music office_sounds
    play sound zipper
    return