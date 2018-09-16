#/usr/local/bin/python3
from win32api import GetSystemMetrics
from pymouse import PyMouse

m = PyMouse()


def get_real_x_y(x, y):
    x_whole = GetSystemMetrics(0)
    y_whole = GetSystemMetrics(1)
    print(x_whole)
    print(y_whole)

    if x_whole == 1920 and y_whole == 1080:
        return x, y
    else:
        x_real = (x * y_whole) / x_whole
        y_real = (y * x_whole) / y_whole
        return int(x_real), int(y_real)


x1, y1 = get_real_x_y(1715, 1056)
print(x1, y1)
m.click(x1, y1)
