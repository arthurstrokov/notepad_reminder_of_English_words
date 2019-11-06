import sys
import PyQt5
from PyQt5 import QtWidgets
from ui.mydesign import Ui_MainWindow
from service.abbyy_parse import *
from service.file_handling import *

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # connecting the clicked signal with btnClicked slot
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        file_name = 'data/two_thousand_most_frequently_used_words_of_the_english_language.json'
        word = show_random_word_from_file_json(file_name)
        self.ui.label.setText(word)


    def btnClicked_2(self):
        file_name = 'data/unknown_words_yet.json'
        word = show_random_word_from_file_json(file_name)
        self.ui.label_2.setText(word)


    def btnClicked_3(self):
        word = self.ui.lineEdit.text()
        translated_word = get_a_word_translation_from_abbyy_api(word)
        self.ui.label_4.setText(translated_word)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
