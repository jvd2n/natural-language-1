from django.shortcuts import render
from nl_prcs.nl_prcs.models import Reader, FileDTO, Printer
from icecream import ic
import matplotlib.pyplot as plt
import platform
from wordcloud import WordCloud, STOPWORDS


class NLService(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()

    def show_alice(self):
        f = self.f
        r = self.r
        p = self.p
        f.context = './data/'
        f.fname = '09. alice.txt'
        f.img = '09. alice_mask.png'
        text = r.txt(f)
        alice_mask = r.img(f)
        # ic(text)
        # ic(type(alice_mask))

        stopwords = set(STOPWORDS)
        stopwords.add("said")

        path = "c:/Windows/Fonts/malgun.ttf"
        from matplotlib import font_manager, rc
        if platform.system() == 'Darwin':
            rc('font', family='AppleGothic')
        elif platform.system() == 'Windows':
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            print('Unknown system... sorry~~~~')

        plt.figure(figsize=(8, 8))  # 최초 창의 크기를 설정
        plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
        plt.axis('off')
        # plt.show()

        wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask,
                       stopwords=stopwords)
        wc = wc.generate(text)
        # ic(wc.words_)
        plt.figure(figsize=(12, 12))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    nls = NLService()
    nls.show_alice()
