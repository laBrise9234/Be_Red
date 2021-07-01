import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen



class MainWindow(Screen):
    pass


class FirstQuestion(Screen):
    pass


class SecondQuestion(Screen):
    pass


class ThirdQuestion(Screen):
    pass


class FourthQuestion(Screen):
    pass


class FifthQuestion(Screen):
    pass


class SixthQuestion(Screen):
    pass


class SeventhQuestion(Screen):
    pass


class EighthQuestion(Screen):
    pass


class NinthQuestion(Screen):
    pass


class TenthQuestion(Screen):
    pass


class EleventhQuestion(Screen):
    pass


class TwelfthQuestion(Screen):
    pass

class Death_1_1(Screen):
    pass

class Death_1_2(Screen):
    pass

class Death_2_1(Screen):
    pass

class Death_2_3(Screen):
    pass

class Death_3(Screen):
    pass

class Final(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("bered2.kv")



class BeRed(App):
    def build(self):
        return kv


if __name__ == '__main__':
    BeRed().run()
