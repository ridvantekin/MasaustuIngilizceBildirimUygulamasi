from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle  # Yeni eklendi
import random

class BildirimUygulamasi(BoxLayout):
    def __init__(self, kelimeler, **kwargs):
        super(BildirimUygulamasi, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.ingilizce = Label(text='', font_size='20sp')
        self.turkce = Label(text='', font_size='20sp')
        self.add_widget(self.ingilizce)
        self.add_widget(self.turkce)
        self.kelimeler = kelimeler
        self.bildirim_goster()


        # Arka plan rengini ayarla
        with self.canvas.before:
            Color(0,0,0.2, 1)  # mavi arkaplan rengi (RGBA formatında)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def bildirim_goster(self, *args):
        kelime = random.choice(self.kelimeler)
        self.ingilizce.text = f'İngilizce: {kelime["ingilizce"]}'
        self.turkce.text = f'Türkçe: {kelime["turkce"]}'
        Clock.schedule_once(self.kapat, 7)

    def kapat(self, *args):
        self.ingilizce.text = ''
        self.turkce.text = ''
        Clock.schedule_once(self.bildirim_goster, 4)

class MainApp(App):
    def build(self):
        kelimeler = self.load_words_from_file('kelimeler.txt')
        Window.size = (200, 100)
        self.title = "RVM"
        return BildirimUygulamasi(kelimeler)


    def load_words_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        kelimeler = []
        for line in lines:
            ingilizce, turkce = line.strip().split(',')
            kelimeler.append({"ingilizce": ingilizce, "turkce": turkce})

        return kelimeler

if __name__ == '__main__':
    MainApp().run()
