#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import (ObjectProperty, ListProperty,
                             StringProperty)

import exifread


class Files(FileChooserListView):

    selectedFiles = ListProperty([])

    def __init__(self, **kwargs):
        super(Files, self).__init__(**kwargs)

    def add2list(self, selection, touch):
        pass


class SelectedFilesRow(BoxLayout):
    color = ListProperty([])
    type = StringProperty()
    text = StringProperty()

    def __init__(self, **kwargs):
        super(SelectedFilesRow, self).__init__(**kwargs)


class SelectedFiles(BoxLayout):
    selectedFiles = ListProperty([])

    def __init__(self, **kwargs):
        super(SelectedFiles, self).__init__(**kwargs)
        self.orientation = "vertical"

    def _update(self):
        lab = SelectedFilesRow(text=self.selectedFiles[-1])
        self.add_widget(lab)


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