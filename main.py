import sys

import elevate
import PyQt5

import nitrosensual


def main():
    try:
        elevate.elevate(show_console=False)
    except OSError as ex:
        print(ex, "\n\nERROR: The program requires administrator rights.\n")
        sys.exit(1)

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = nitrosensual.MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()