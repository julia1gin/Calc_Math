import wx
import const
class windowIntegral(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

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
        print(const.right_rectangle(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue())))
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

        methodMenu.Bind(wx.EVT_MENU, self.window_Integral, None, 1)
        methodMenu.Bind(wx.EVT_MENU, self.window_Integral, None, 2)
        methodMenu.Bind(wx.EVT_MENU, self.window_Integral, None, 3)
        methodMenu.Bind(wx.EVT_MENU, self.window_Integral, None, 4)

        menubar.Append(fileMenu, "Численное интегрирование")
        self.SetMenuBar(menubar)

    def window_Integral(self, event):
        frame2 = windowIntegral(None, "Произведем рассчеты")
        frame2.Centre()
        frame2.id = event.GetId
        frame2.Show(True)

app = wx.App()
frame = MyFrame(None, "Вычислительная математика")
frame.Centre()
frame.Show(True)
app.MainLoop()