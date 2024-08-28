def send_email(massage, recipient, *, sender="university.help@gmail.com"):
    i = "@"
    while 1 > 0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if i not in recipient and sender:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                break
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            break
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            break
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            break
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
            break

send_email('hi', 'university.help@gmail.com')
send_email('hi', 'university.help@nmail.ua')
send_email('hi', 'absoluteracist2009@mail.ru')
send_email('hi', 'pivo@gmail.lol')