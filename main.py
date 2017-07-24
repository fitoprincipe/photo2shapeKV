#!/usr/bin/python
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (ObjectProperty, ListProperty,
                             StringProperty)
from kivy.uix.gridlayout import GridLayout

import exifread
import shapefile


class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)


class MainWindow(BoxLayout):
    pass


class SubWindow(BoxLayout):
    pass


class Files(FileChooserListView):

    selectedFiles = ListProperty([])

    def __init__(self, **kwargs):
        super(Files, self).__init__(**kwargs)

    def add2list(self, selection, touch):
        pass


class SelectedFilesRow(BoxLayout):
    """ This is the widget for each selected file. It has its path
    (Label) and a cancell button at its right.
    """
    # TODO: wrap the path label
    color = ListProperty([])
    type = StringProperty()
    text = StringProperty()

    def __init__(self, **kwargs):
        super(SelectedFilesRow, self).__init__(**kwargs)


class SelectedFiles(GridLayout):
    selectedFiles = ListProperty([])

    def __init__(self, **kwargs):
        super(SelectedFiles, self).__init__(**kwargs)

    def _update(self):
        self.clear_widgets()
        for file in self.selectedFiles:
            f = file
            lab = SelectedFilesRow(text=f)
            self.add_widget(lab)


class P2sApp(App):
    title = "Photo 2 Shape KV"
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