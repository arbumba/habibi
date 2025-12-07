class Engine:
    def start(self):
        print("The engine has started")

class ElectroEngine():
    def charge(self):
        print("The engine has charged")

class Hybrid(Engine, ElectroEngine):
    def drive(self):
        print("Hybrid driving")

car = Hybrid()
car.start()
car.charge()
car.drive()

"""
class Audio:
    def play_audio(self):
        print("Playing audio.")

class Video:
    def play_video(self):
        print("Playing video.")

class Multi(Audio, Video):
    def play_multi(self):
        print("Playing multimedia.")

player = Multi()
player.play_audio()
player.play_video()
player.play_multi()
"""