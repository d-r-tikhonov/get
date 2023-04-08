# Руководство по использованию Git
## SSH-ключ
### Создание
    ssh-keygen -t ed25519 -C "имя.фамилия@phystech.edu"
Где ed25519 это просто формат ключа, а после ключа -C идёт ваш email.
### Добавить в аккаунт
Ключи созданы, но наш клиент SSH не знает какой ключ использовать для подключения. Эту информацию клиенту SSH может предоставить программа ssh-agent. Чтобы запустить ее нужно выполнить в терминале команду:
        ```eval "$(ssh-agent -s)"```
А после добавить в агента ваш ключ при помощи команды:
        ```ssh-add ~/.ssh/id_ed25519```
## Команды
### Клонировать репозиторий
    git clone git@github.com:username/repository.git
### Проверить статус репозитория
    git status
### Подготовить новый файл для комита 
    git add git-how-to.md
### Проверить статус репозитория 
    git status
### Сделать коммит 
    git commit -m “initial commit”
### Отправить изменения на сервер 
    git push