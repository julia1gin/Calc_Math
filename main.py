import wx
from const import *
class windowIntegral(wx.Frame):
    def __init__(self, parent, title, metId):
        super().__init__(parent, title=title)
        self.id = metId

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(5, 2, 15, 15)
        self.atext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.xtext = wx.TextCtrl(panel)
        self.ntext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")

        fb.AddMany([(wx.StaticText(panel, label="Подыинтегральная функция:")),
                    self.xtext,
                    (wx.StaticText(panel, label="Нижний предел интегрирования:")),
                    self.atext,
                    (wx.StaticText(panel, label="Верхний предел интегрирования:")),
                    self.btext,
                    (wx.StaticText(panel, label="Количество разбиений:")),
                    self.ntext, self.result])
        self.result.Bind(wx.EVT_BUTTON, self.integrate, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def integrate(self, event):
        print(self.id)
        match self.id:
            case 1: print(left_rectangle(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue())))
            case 2: print(right_rectangle(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue())))
            case 3: print(parabola(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue())))
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        methodMenu = wx.Menu()
        method2Menu = wx.Menu()

        methodMenu.Append(1, "Метод прямоугольников левых частей")
        methodMenu.Append(2, "Метод прямоугольников правых частей")
        methodMenu.Append(3, "Метод парабол")
        methodMenu.Append(4, "Метод трапеций")

        method2Menu.Append(5, "Алгоритм №1")
        method2Menu.Append(6, "Алгоритм №2")

        fileMenu.AppendSubMenu(methodMenu, "С переменным шагом")
        fileMenu.AppendSubMenu(method2Menu, "С постоянным шагом")
        fileMenu.Append(7, 'Кратный интеграл')

        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 1)
        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 2)
        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 3)
        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 4)

        menubar.Append(fileMenu, "Численное интегрирование")
        self.SetMenuBar(menubar)

    def window_integral(self, event):
        id = event.GetId()
        title = ''
        match id:
            case 1: title = "Метод левых прямоугольников"
            case 2: title = "Метод правых прямоугольников"
            case 3: title = "Метод парабол"
            case 4: title = "Метод трапеций"
        frame2 = windowIntegral(None, title, id)
        frame2.Centre()
        frame2.Show(True)

app = wx.App()
frame = MyFrame(None, "Вычислительная математика")
frame.Centre()
frame.Show(True)
app.MainLoop()