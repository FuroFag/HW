import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    videos = []

    def __init__(self, name, duration, time_now, adult_mode):
        self.name = name
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.name == other.name

    def __contains__(self, item):
        return item in self.name

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print (f'Пользователь {nickname} уже зарегистрирован')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == self.nickname and password == user.password:
                self.current_user == user

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, name):
        list_videos = []
        for video in self.videos:
            if name.upper() in video.name.upper():
                list_videos.append(video.name)
        return list_videos

    def watch_video(self, name):
        if not self.current_user:
            print (f'Войдите в аккаунт чтобы продолжить')
            return

        for j in self.videos:
            if j.name == name:
                if j.adult_mode and self.current_user.age < 18:
                    print (f'Данное видео помечено как 18+, вы не можете его посмотреть')

                for g in range (j.duration):
                    print (g, end=' ')
                    j.time_now += 1
                j.time_now = 0
                print ('Конец видео')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video ('Лучший язык программирования 2024', 200, 0, False)
    v2 = Video ('Нижний интернет (пародия на Кинопоиск)', 980, 0, True)

ur.add (v1, v2)

print(ur.get_videos('лУЧШИЙ'))
print(ur.get_videos('нижний интернет'))

ur.watch_video('Нижний интернет (пародия на Кинопоиск)')
ur.register('Lebron James', 'lbrnjms119911', 17)
ur.watch_video('Нижний интернет (пародия на Кинопоиск)')
ur.register('UbiycaNoobov', 'Adolf_Hitler1', 21)
ur.watch_video('Нижний интернет (пародия на Кинопоиск)')

ur.register('Lebron James', 'lbrnjms119911', 17)
print (ur.current_user)

ur.watch_video('Лучший язык программирования 2024')