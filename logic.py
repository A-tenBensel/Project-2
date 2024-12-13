from PyQt6.QtWidgets import *
from gui import *
import random


class Logic(QMainWindow, Ui_MainWindow):
    attempts: int
    correct: int
    operator: tuple[str, str]
    answer: int
    val_1: int
    val_2: int

    def __init__(self) -> None:
        """
        Method to set default state of the window.
        """
        super().__init__()
        self.setupUi(self)
        self.attempts = 0
        self.correct = 0
        self.operator = ('self.addition()', '+')
        self.answer = 0
        self.val_1 = 0
        self.val_2 = 0
        self.button_add.clicked.connect(lambda: self.operation(('self.addition()', '+')))
        self.button_subtract.clicked.connect(lambda: self.operation(('self.subtraction()', '-')))
        self.button_multiply.clicked.connect(lambda: self.operation(('self.multiplication()', '*')))
        self.button_divide.clicked.connect(lambda: self.operation(('self.division()', '/')))
        self.button_return.clicked.connect(lambda: self.home())
        self.button_submit.clicked.connect(lambda: self.submit())
        self.input_answer.returnPressed.connect(lambda: self.submit())
        self.frame_2.setVisible(False)

    def operation(self, operator: tuple[str, str]) -> None:
        """
        Method to change window to the operator window and asks an operator question.
        :param operator: Type of operation: addition, subtraction, multiplication, division.
        """
        self.frame_1.setVisible(False)
        self.frame_2.setVisible(True)
        self.operator = operator
        self.input_answer.clear()
        self.val_1, self.val_2, self.answer = eval(self.operator[0])
        self.label_equation.setText(f"{self.val_1} {self.operator[1]} {self.val_2} = ")
        self.input_answer.setFocus()

    def home(self) -> None:
        """
        Method to return to starting window.
        """
        self.frame_1.setVisible(True)
        self.frame_2.setVisible(False)

    def submit(self) -> None:
        """
        Method to submit answer. Updates the number correct of attempts accordingly
        and asks another operator question.
        """
        try:
            if int(self.input_answer.text()) == self.answer:
                self.correct += 1
        except ValueError:
            pass
        finally:
            self.attempts += 1
            self.label_correct.setText(f"{self.correct} out of {self.attempts}")
            self.input_answer.clear()
            self.val_1, self.val_2, self.answer = eval(self.operator[0])
            self.label_equation.setText(f"{self.val_1} {self.operator[1]} {self.val_2} = ")
            self.input_answer.setFocus()

    @staticmethod
    def addition() -> tuple[int, int, int]:
        """
        Method to get a random addition problem.
        :return: the values of the addition problem and the sum.
        """
        val_1: int = random.randint(0, 100)
        val_2: int = random.randint(0, 100)
        return val_1, val_2, val_1 + val_2

    @classmethod
    def subtraction(cls) -> tuple[int, int, int]:
        """
        Method to get a random subtraction problem.
        :return: the values of the subtraction problem and the difference.
        """
        val_3, val_2, val_1 = cls.addition()
        return val_1, val_2, val_3

    @staticmethod
    def multiplication() -> tuple[int, int, int]:
        """
        Method to get a random multiplication problem.
        :return: the values of the multiplication problem and the product.
        """
        val_1: int = random.randint(1, 20)
        val_2: int = random.randint(0, 400 // val_1)
        return val_1, val_2, val_1 * val_2

    @classmethod
    def division(cls) -> tuple[int, int, int]:
        """
        Method to get a random division problem.
        :return: the values of the division problem and the quotient.
        """
        val_2, val_3, val_1 = cls.multiplication()
        return val_1, val_2, val_3
