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