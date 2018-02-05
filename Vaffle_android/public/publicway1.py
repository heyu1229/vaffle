import unittest


class Publicway(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

        # 向左滑

    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)

        # 向右滑

    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

        # 向上滑

    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.4)
        self.driver.swipe(x1, y1, x1, y2, t)

        # 向下滑

    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.7)
        self.driver.swipe(x1, y1, x1, y2, t)


if __name__ == '__main__':
    unittest.main()
