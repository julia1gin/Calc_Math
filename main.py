import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        methodMenu = wx.Menu()
        method2Menu = wx.Menu()

        methodMenu.Append(wx.ID_ANY, "Метод прямоугольников левых частей")
        methodMenu.Append(wx.ID_ANY, "Метод прямоугольников правых частей")
        methodMenu.Append(wx.ID_ANY, "Метод парабол")
        methodMenu.Append(wx.ID_ANY, "Метод трапеций")

        method2Menu.Append(wx.ID_ANY, "Алгоритм №1")
        method2Menu.Append(wx.ID_ANY, "Алгоритм №2")

        fileMenu.AppendSubMenu(methodMenu, "С переменным шагом")
        fileMenu.AppendSubMenu(method2Menu, "С постоянным шагом")
        fileMenu.Append(wx.ID_ANY, 'Кратный интеграл')

        menubar.Append(fileMenu, "Численное интегрирование")
        self.SetMenuBar(menubar)

app = wx.App()
frame = MyFrame(None, "Вычислительная математика")
frame.Centre()
frame.Show(True)
app.MainLoop()