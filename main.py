import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox


class StudyMateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StudyMate")
        self.setWindowIcon(QIcon('rasm.png'))

        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Create check triangle section
        check_triangle_label = QLabel("To check whether it is possible to make a triangle with the three input numbers.")
        check_triangle_label.setObjectName("checkTriangleLabel")
        main_layout.addWidget(check_triangle_label)

        # Create input fields
        self.side1_input = QLineEdit()
        self.side1_input.setPlaceholderText("Side 1")
        self.side1_input.setValidator(QDoubleValidator())
        self.side1_input.setObjectName("sideInput")
        main_layout.addWidget(self.side1_input)

        self.side2_input = QLineEdit()
        self.side2_input.setPlaceholderText("Side 2")
        self.side2_input.setValidator(QDoubleValidator())
        self.side2_input.setObjectName("sideInput")
        main_layout.addWidget(self.side2_input)

        self.side3_input = QLineEdit()
        self.side3_input.setPlaceholderText("Side 3")
        self.side3_input.setValidator(QDoubleValidator())
        self.side3_input.setObjectName("sideInput")
        main_layout.addWidget(self.side3_input)

        # Create check button
        check_button = QPushButton("Check")
        check_button.clicked.connect(self.check_triangle)
        check_button.setObjectName("checkButton")
        main_layout.addWidget(check_button)

        # Create menu
        menu = self.menuBar()
        organization_menu = menu.addMenu("Our Organization")

        # Add organization information action
        org_info_action = organization_menu.addAction("Organization Information")
        org_info_action.triggered.connect(self.show_organization_info)

        # Add other projects action
        other_projects_action = organization_menu.addAction("Other Projects")
        other_projects_action.triggered.connect(self.open_website)

        # Set the central widget
        self.setCentralWidget(main_widget)

    def check_triangle(self):
        side1 = self.side1_input.text()
        side2 = self.side2_input.text()
        side3 = self.side3_input.text()

        if side1 == '' or side2 == '' or side3 == '':
            QMessageBox.warning(self, "Triangle Check", "Please fill all three sides.")
        else:
            side1 = float(side1)
            side2 = float(side2)
            side3 = float(side3)

            if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
                QMessageBox.information(self, "Triangle Check", "It is possible to form a triangle with these sides.")
            else:
                QMessageBox.warning(self, "Triangle Check", "It is not possible to form a triangle with these sides.")

    def show_organization_info(self):
        QMessageBox.information(self, "Our Organization", "This is StudyMate. Unlock your potential!")

    def open_website(self):
        import webbrowser
        webbrowser.open("https://matestudy.netlify.app")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Apply style sheet for custom designs
    style_sheet = """
        #checkTriangleLabel {
            font-size: 16px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        #sideInput {
            height: 30px;
            font-size: 14px;
            padding: 5px;
        }
        #checkButton {
            height: 30px;
            font-size: 14px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 3px;
        }
        QMessageBox {
            font-size: 14px;
            color: #333;
        }
        QMessageBox QLabel {
            margin-bottom: 10px;
        }
        """
    app.setStyleSheet(style_sheet)

    study_mate_app = StudyMateApp()
    study_mate_app.show()
    sys.exit(app.exec())
