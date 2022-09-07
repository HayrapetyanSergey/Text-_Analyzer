from  PyQt5 import QtWidgets,QtCore
from  PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog,QMessageBox
import text_analyzer 
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.filename = None

        self.setWindowTitle("Analyzer Window")
        self.setFixedSize(320, 300)
        self.setGeometry(500, 350, 350, 200)

        # Creating MenuBar
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        fileMenu = QMenu("File", self)
        self.menuBar.addMenu(fileMenu)
        fileMenu.addAction("Open", self.menu_action_clicked)

        self.words_number_btn = QtWidgets.QPushButton(self)
        self.words_number_btn.move(60, 150)
        self.words_number_btn.setText("The number of words")
        self.words_number_btn.setFixedWidth(200)

        self.letters_number_btn = QtWidgets.QPushButton(self)
        self.letters_number_btn.move(60, 180)
        self.letters_number_btn.setText("The number of letters")
        self.letters_number_btn.setFixedWidth(200)

        self.sentences_number_btn = QtWidgets.QPushButton(self)
        self.sentences_number_btn.move(60, 210)
        self.sentences_number_btn.setText("The number of sentences")
        self.sentences_number_btn.setFixedWidth(200)

        self.most_letter_btn = QtWidgets.QPushButton(self)
        self.most_letter_btn.move(60, 240)
        self.most_letter_btn.setText("The most used letter in a text")
        self.most_letter_btn.setFixedWidth(200)

        self.most_word_btn = QtWidgets.QPushButton(self)
        self.most_word_btn.move(60, 270)
        self.most_word_btn.setText("The most used word in a text")
        self.most_word_btn.setFixedWidth(200)

        self.words_number_btn.clicked.connect(self.words_number_clicked)
        self.letters_number_btn.clicked.connect(self.letters_number_clicked)
        self.sentences_number_btn.clicked.connect(self.sentences_number_clicked)
        self.most_letter_btn.clicked.connect(self.most_letter_clicked)
        self.most_word_btn.clicked.connect(self.most_word_clicked)

        # Error box
        self.error = QMessageBox()
        self.error.setWindowTitle("Error")
        self.error.setIcon(QMessageBox.Warning)

    def words_number_clicked(self):
        if self.filename == "" or self.filename == None:
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("Give me a file!")
            self.error.exec_()
        else:
            message = f'The number of words is {text_analyzer.count_of_words(self.filename)}'
            QMessageBox.about(self, "", message)
    
    def letters_number_clicked(self):
        if self.filename == "" or self.filename == None:
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("Give me a file!")
            self.error.exec_()
        else:
            message = f'The number of letters is {text_analyzer.count_of_letters(self.filename)}'
            QMessageBox.about(self, "", message)

    def sentences_number_clicked(self):
        if self.filename == "" or self.filename == None:
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("Give me a file!")
            self.error.exec_()
        else:
            message = f'The number of sentences is {text_analyzer.count_of_sentences(self.filename)}'
            QMessageBox.about(self, "", message)

    def most_letter_clicked(self):
        if self.filename == "" or self.filename == None:
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("Give me a file!")
            self.error.exec_()
        else:
            message = f'The most used letter in a text is "{text_analyzer.common_letters(self.filename)}"'
            QMessageBox.about(self, "", message)
    
    def most_word_clicked(self):
        if self.filename == "" or self.filename == None:
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("Give me a file!")
            self.error.exec_()
        else:
            message = f'The most used letter in a word is "{text_analyzer.common_word(self.filename)}"'
            QMessageBox.about(self, "", message)

    @QtCore.pyqtSlot()
    def menu_action_clicked(self):
        self.filename = QFileDialog.getOpenFileName(self)[0]
        if self.filename == '':
            pass
        elif not self.filename.endswith(".txt"):
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("File must have .txt extentions")
            self.error.exec_()
        else:
            pass

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()