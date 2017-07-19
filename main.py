#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.properties import ObjectProperty

import exifread


class Files(FileChooserListView):
    def __init__(self, **kwargs):
        super(Files, self).__init__(**kwargs)

class P2sApp(App):
    def build(self):
        pass

    @staticmethod
    def tieneGPS(img):
        """ metodo para verificar la existencia de datos GPS

        :param img: ruta de la imagen a verificar
        :type img: str
        :return: si la imagen tiene datos GPS o no
        :rtype: bool
        """
        imagen = open(img, 'rb')
        losTags = exifread.process_file(imagen)

        return True if 'GPS GPSLongitude' in losTags.keys() else False

if __name__ == "__main__":
    P2sApp().run()