#!/usr/bin/env python
# coding: utf-8

from wordcloud import WordCloud
import codecs
import jieba
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def draw_wordcloud():
    comment_text = open(r'69339danmu1.txt','r').read()
    cut_text = " ".join(jieba.cut(comment_text))
    d = path.dirname(__file__)
    color_mask = imread("maps3.png")
    cloud = WordCloud(
        font_path="msyh.ttf",
        background_color='white',
        mask=color_mask,
        max_words=200,
        max_font_size=40
    )
    word_cloud = cloud.generate(cut_text)
    word_cloud.to_file("pjl_cloud2.jpg")
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    draw_wordcloud()
