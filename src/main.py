import sys
import traceback

import elevate
import PyQt5

import nitrosensual


def exception_handler(exc_type, exc_value, exc_tb):
    traceback.print_exception(exc_type, exc_value, exc_tb)
    with open('error_log.txt', 'a', encoding='utf-8') as f:
        traceback.print_exception(exc_type, exc_value, exc_tb, file=f)
        f.write("\n")
    sys.exit(1)


def main():
    try:
        pass
        elevate.elevate(show_console=False)
    except OSError as ex:
        print(ex, '\n\nERROR: The program requires administrator rights.\n')
        sys.exit(1)

    sys.excepthook = exception_handler
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = nitrosensual.MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()