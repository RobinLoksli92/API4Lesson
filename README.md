# Публикация фотографий космоса в телеграмм канал

Скрипт, который сохраняет по указанному вами пути фотографии с сайтов NASA и SpaceX и публикует их в телеграм канале раз в сутки.

## Установка

Для установки зависимостей в командной строке введите:

```
pip install -r requirements.txt
```
Также, необходим токен для взаимодействия с Telegram. Для этого напишите Отцу Ботов `@BotFather` :
```
/newbot
```
Далее дайте ему имя и не забудьте скопировать токен, который пришлет вам Отец Ботов после создания.
Ваш токен необходимо "спрятать". Поэтому в репозитории со скриптом создаем файл `.env`,
а в него записываем 
```
Название токена=Токен, который вы получили от @BotFather
```
Далее, вам нужно создать телеграмм канал и сделать вашего бота в нем администратором.

## Запуск

Для того,чтобы запустить сайт, в командной строке необходимо написать(для пользователей Windows):
```
python main.py
``` 
 или (для Linux):
```
python3 main.py
```
Не торопитесь выключать программу, ей нужно какое-то время, чтобы скачать фото. Только потом бот пришлет вам первую фотографию в телеграмм канал

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).