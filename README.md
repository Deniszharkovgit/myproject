Гугл диск https://docs.google.com/spreadsheets/d/1Xc13UDoPCHh1_yQoNwfieFMovmhAcrzsqU_XsQz44SM/edit#gid=0
1. Открыть в терминале либо в IDE проект.
2. В корневой папке проекта создать виртуальную среду и установить библиотеки из req.txt
3. В корневой папке проекта, где находится manage.py, выполнить в терминале python manage.py runserver 0.0.0.0:8000
4. После запуска сервера бэкенда перейти в папку myproject_ui и выполнить npm start

Бэк и фронт запущен, посмотреть работу апи в джанге можно перейдя по адресу 0.0.0.0:8000/api/numbers, в реакте localhost:3000
Для отправки уведомлений в телеграм вам необходимо зайти в данный бот @getmyid_bot, скопировать Current chat ID и поместить этот полученый id в файл
корневаяПапкаПроекта/myproject_app/views.py. Заменить chat_id в функции send_from_user в 16 строке на тот id который вы получили из бота @getmyid_bot

Есть баги в работе реакта. Скрипт питона работает отлично.


Вот так выоглядят сообщения от бота:
![изображение](https://user-images.githubusercontent.com/107854659/174807200-13f54737-204e-4d29-9e5e-0ca3d6af41d4.png)
