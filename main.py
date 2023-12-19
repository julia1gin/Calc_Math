import wx
from const import *
from var import *
from double_integral import *
from Euler_method import *
from RK_integral import *
from Euler_second_order import *
from system_DE import *
from NonLinearSecantMethod import *
from NonLinearTangentMethod import *
from NonLinearSegmentDivisionMethod import *
from iterete_method import *
from Chebyshev import *

class windowIntegralDouble(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(9, 2, 20, 20)

        self.xtext = wx.TextCtrl(panel)
        self.atext = wx.TextCtrl(panel)
        self.ctext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.dtext = wx.TextCtrl(panel)
        self.nxtext = wx.TextCtrl(panel)
        self.nytext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([(wx.StaticText(panel, label="Подынтегральная функция:")),
                    self.xtext,
                    (wx.StaticText(panel, label="Нижний предел внешнего интеграла:")),
                    self.atext,
                    (wx.StaticText(panel, label="Нижний предел внутреннего интеграла:")),
                    self.ctext,
                    (wx.StaticText(panel, label="Верхний предел внешнего интеграла:")),
                    self.btext,
                    (wx.StaticText(panel, label="Верхний предел внутреннего интеграла:")),
                    self.dtext,
                    (wx.StaticText(panel, label="Количество разбиений по х:")),
                    self.nxtext,
                    (wx.StaticText(panel, label="Количество разбиений по у:")),
                    self.nytext,
                    self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.integrateDouble, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def integrateDouble(self, event):
        ans = integral2(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.ctext.GetValue()),
                        float(self.btext.GetValue()), float(self.dtext.GetValue()), int(self.nxtext.GetValue()),
                        int(self.nytext.GetValue()))
        self.answer.SetLabel(str(ans))


class windowIntegral(wx.Frame):
    def __init__(self, parent, title, metId):
        super().__init__(parent, title=title)

        self.id = metId
        if(metId > 4):
            self.ntype = "Точность:"
        else:
            self.ntype = "Количество разбиений:"

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(6, 2, 15, 15)

        self.xtext = wx.TextCtrl(panel)
        self.atext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.ntext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([(wx.StaticText(panel, label="Подынтегральная функция:")),
                    self.xtext,
                    (wx.StaticText(panel, label="Нижний предел интегрирования:")),
                    self.atext,
                    (wx.StaticText(panel, label="Верхний предел интегрирования:")),
                    self.btext,
                    (wx.StaticText(panel, label=self.ntype)),
                    self.ntext, self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.integrate, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def integrate(self, event):
        ans = ''
        match self.id:
            case 1: ans = left_rectangle(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue()))
            case 2: ans = right_rectangle(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue()))
            case 3: ans = parabola(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue()))
            case 4: ans = trap(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), int(self.ntext.GetValue()))
            case 5: ans = double_int(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ntext.GetValue()))
            case 6: ans = double_int_fixed(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ntext.GetValue()))
        self.answer.SetLabel(str(ans))

class windowDU(wx.Frame):
    def __init__(self, parent, title, metId):
        super().__init__(parent, title=title)

        self.id = metId

        if (metId == 9):
            self.ntype = "Шаг:"
        else:
            self.ntype = "Количество разбиений:"


        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(7, 2, 10, 10)

        self.xtext = wx.TextCtrl(panel)
        self.atext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.ytext = wx.TextCtrl(panel)
        self.ntext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([(wx.StaticText(panel, label="Уравнение:")),
                    self.xtext,
                    (wx.StaticText(panel, label="Начало отрезка:")),
                    self.atext,
                    (wx.StaticText(panel, label="Конец отрезка:")),
                    self.btext,
                    (wx.StaticText(panel, label="y0:")),
                    self.ytext,
                    (wx.StaticText(panel, label=self.ntype)), self.ntext, self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.difuri, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def difuri(self, event):
        ans = ''
        match self.id:
            case 8: ans = Euler(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ytext.GetValue()), int(self.ntext.GetValue()))
            case 9: ans = runge_Kutta(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ytext.GetValue()), float(self.ntext.GetValue()))
        self.answer.SetLabel(str(ans))

class secondDU(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(7, 2, 10, 10)

        self.atext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.ytext = wx.TextCtrl(panel)
        self.y2text = wx.TextCtrl(panel)
        self.ntext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([
                    (wx.StaticText(panel, label="Начало отрезка:")),
                    self.atext,
                    (wx.StaticText(panel, label="Конец отрезка:")),
                    self.btext,
                    (wx.StaticText(panel, label="y:")),
                    self.ytext,
                    (wx.StaticText(panel, label="y':")),
                    self.y2text,
                    (wx.StaticText(panel, label="Шаг:")), self.ntext, self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.second_difuri, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def second_difuri(self, event):
        ans = euler_second( float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ytext.GetValue()), float(self.y2text.GetValue()), float(self.ntext.GetValue()))
        self.answer.SetLabel(str(ans))

class systemDU(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(8, 2, 9, 9)

        self.atext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.xtext = wx.TextCtrl(panel)
        self.ytext = wx.TextCtrl(panel)
        self.ztext = wx.TextCtrl(panel)
        self.ntext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([
                    (wx.StaticText(panel, label="Начало отрезка:")),
                    self.atext,
                    (wx.StaticText(panel, label="Конец отрезка:")),
                    self.btext,
                    (wx.StaticText(panel, label="x0:")),
                    self.xtext,
                    (wx.StaticText(panel, label="y0':")),
                    self.ytext,
                    (wx.StaticText(panel, label="z0':")),
                    self.ztext,
                    (wx.StaticText(panel, label="Шаг:")), self.ntext, self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.system_difuri, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def system_difuri(self, event):
        ans = system_DU( float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.xtext.GetValue()), float(self.ytext.GetValue()), float(self.ztext.GetValue()), float(self.ntext.GetValue()))
        self.answer.SetLabel(str(ans))

class NonLine(wx.Frame):
    def __init__(self, parent, title, metId):
        super().__init__(parent, title=title)

        self.id = metId

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(7, 2, 20, 20)

        self.xtext = wx.TextCtrl(panel)
        self.atext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.ntext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([(wx.StaticText(panel, label="Уравнение:")),
                    self.xtext,
                    (wx.StaticText(panel, label="Начало отрезка:")),
                    self.atext,
                    (wx.StaticText(panel, label="Конец отрезка:")),
                    self.btext,
                    (wx.StaticText(panel, label="Точность:")), self.ntext, self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.nonline, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def nonline(self, event):
        ans = ''
        match self.id:
            case 12: ans = SegmentDivision(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ntext.GetValue()))
            case 14: ans = findRootSM(self.xtext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ntext.GetValue()))
        self.answer.SetLabel(str(ans))

class NonLine_Nuton(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(8, 2, 13, 15)

        self.xtext = wx.TextCtrl(panel)
        self.ptext = wx.TextCtrl(panel)
        self.atext = wx.TextCtrl(panel)
        self.btext = wx.TextCtrl(panel)
        self.ntext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([(wx.StaticText(panel, label="Уравнение:")),
                    self.xtext,
                    (wx.StaticText(panel, label="Производная:")),
                    self.ptext,
                    (wx.StaticText(panel, label="Начало отрезка:")),
                    self.atext,
                    (wx.StaticText(panel, label="Конец отрезка:")),
                    self.btext,
                    (wx.StaticText(panel, label="Точность:")), self.ntext, self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.nonlineNuton, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def nonlineNuton(self, event):
        ans = method_tangent(self.xtext.GetValue(), self.ptext.GetValue(), float(self.atext.GetValue()), float(self.btext.GetValue()), float(self.ntext.GetValue()))
        self.answer.SetLabel(str(ans))

class ElemIter(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(8, 2, 13, 15)

        self.ftext = wx.TextCtrl(panel)
        self.xtext = wx.TextCtrl(panel)
        self.ytext = wx.TextCtrl(panel)
        self.etext = wx.TextCtrl(panel)
        self.result = wx.Button(panel, label="Посчитать")
        self.answer = wx.StaticText(panel)
        fb.AddMany([(wx.StaticText(panel, label="Уравнение:")),
                    self.ftext,
                    (wx.StaticText(panel, label="x")),
                    self.xtext,
                    (wx.StaticText(panel, label="y0")),
                    self.ytext,
                    (wx.StaticText(panel, label="Точность:")), self.etext, self.result, self.answer,
                    wx.StaticText(panel)])

        self.result.Bind(wx.EVT_BUTTON, self.ElemIter, None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def ElemIter(self, event):
        ans = iterete_method(self.ftext.GetValue(), float(self.xtext.GetValue()), float(self.ytext.GetValue()), float(self.etext.GetValue()))
        self.answer.SetLabel(str(ans))

class ElemCheb(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        fb = wx.FlexGridSizer(8, 2, 13, 15)

        self.xtext = wx.TextCtrl(panel)
        self.etext = wx.TextCtrl(panel)
        self.resultsin = wx.Button(panel, label="Посчитать sin(x)")
        self.resulte = wx.Button(panel, label="Посчитать e**x")
        self.answer = wx.StaticText(panel)
        fb.AddMany([(wx.StaticText(panel, label="x")),
                    self.xtext,
                    (wx.StaticText(panel, label="Точность:")), self.etext, self.resultsin, self.resulte, self.answer,
                    wx.StaticText(panel)])

        self.resultsin.Bind(wx.EVT_BUTTON, self.ElemChebSin, None)
        self.resulte.Bind(wx.EVT_BUTTON,self.ElemChebE,None)
        panel.SetSizer(fb)
        self.Centre()
        self.Show()

    def ElemChebSin(self, event):
        ans = sin_in_degree_x(float(self.xtext.GetValue()), float(self.etext.GetValue()))
        self.answer.SetLabel(str(ans))
    def ElemChebE(self, event):
        ans = e_in_degree_x(float(self.xtext.GetValue()), float(self.etext.GetValue()))
        self.answer.SetLabel(str(ans))


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

        fileMenu.AppendSubMenu(methodMenu, "С постоянным шагом")
        fileMenu.AppendSubMenu(method2Menu, "С переменным шагом")
        fileMenu.Append(7, 'Кратный интеграл')

        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 1)
        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 2)
        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 3)
        methodMenu.Bind(wx.EVT_MENU, self.window_integral, None, 4)
        method2Menu.Bind(wx.EVT_MENU, self.window_integral, None, 5)
        method2Menu.Bind(wx.EVT_MENU, self.window_integral, None, 6)
        fileMenu.Bind(wx.EVT_MENU, self.window_integral_double, None, 7)

        difurMenu = wx.Menu()
        firstduMenu = wx.Menu()

        firstduMenu.Append(8, 'Метод Эйлера')
        firstduMenu.Append(9, 'Метод Рунге-Кутта')

        difurMenu.AppendSubMenu(firstduMenu, 'ДУ первого порядка')
        difurMenu.Append(10, 'ДУ второго порядка')
        difurMenu.Append(11, 'Система ДУ')

        firstduMenu.Bind(wx.EVT_MENU, self.window_difur, None, 8)
        firstduMenu.Bind(wx.EVT_MENU, self.window_difur, None, 9)
        difurMenu.Bind(wx.EVT_MENU, self.window_seconddifur, None, 10)
        difurMenu.Bind(wx.EVT_MENU, self.window_systemDU, None, 11)


        nonlineMenu = wx.Menu()

        nonlineMenu.Append(12, 'Метод половинного деления')
        nonlineMenu.Append(13, 'Метод Ньютона(касательных)')
        nonlineMenu.Append(14, 'Метод хорд')

        nonlineMenu.Bind(wx.EVT_MENU, self.window_nonline, None, 12)
        nonlineMenu.Bind(wx.EVT_MENU, self.window_nonline_Nuton, None, 13)
        nonlineMenu.Bind(wx.EVT_MENU, self.window_nonline, None, 14)

        elemMenu = wx.Menu()

        elemMenu.Append(15, 'Метод итераций')
        elemMenu.Append(16, 'Метод Чебышева')

        elemMenu.Bind(wx.EVT_MENU, self.window_elem_iter, None, 15)
        elemMenu.Bind(wx.EVT_MENU, self.window_elem_cheb, None, 16)

        menubar.Append(fileMenu, "Численное интегрирование")
        menubar.Append(difurMenu, 'Дифференциальные уравнения')
        menubar.Append(nonlineMenu, 'Нелинейные уравнения')
        menubar.Append(elemMenu, "Вычисление элементарных функций")


        self.SetMenuBar(menubar)



    def window_integral(self, event):
        id = event.GetId()
        title = ''
        match id:
            case 1: title = "Метод левых прямоугольников"
            case 2: title = "Метод правых прямоугольников"
            case 3: title = "Метод парабол"
            case 4: title = "Метод трапеций"
            case 5: title = "Алгоритм №1"
            case 6: title = "Алгоритм №2"
        frame2 = windowIntegral(None, title, id)
        frame2.Centre()
        frame2.Show(True)

    def window_integral_double(self, event):
        frame3 = windowIntegralDouble(None, title="Кратный интеграл")
        frame3.Centre()
        frame3.Show(True)

    def window_difur(self, event):
        id = event.GetId()
        title = ''
        match id:
            case 8:
                title = "Метод Эйлера"
            case 9:
                title = "Метод Рунге-Кутта"
        frame4 = windowDU(None, title, id)
        frame4.Centre()
        frame4.Show(True)

    def window_seconddifur(self, event):
        frame5 = secondDU(None, title='ДУ второго порядка')
        frame5.Centre()
        frame5.Show(True)

    def window_systemDU(self, event):
        frame6 = systemDU(None, title='Система ДУ')
        frame6.Centre()
        frame6.Show(True)

    def window_nonline(self, event):
        id = event.GetId()
        title = ''
        match id:
            case 12:
                title = "Метод половинного деления"
            case 14:
                title = "Метод хорд"
        frame7 = NonLine(None, title, id)
        frame7.Centre()
        frame7.Show(True)

    def window_nonline_Nuton(self, event):
        frame8 = NonLine_Nuton(None, title='Метод Ньютона(касательных)')
        frame8.Centre()
        frame8.Show(True)

    def window_elem_iter(self, event):
        frame9 = ElemIter(None, title='Метод Итераций')
        frame9.Centre()
        frame9.Show(True)

    def window_elem_cheb(self, event):
        frame10 = ElemCheb(None, title='Метод Чебышева')
        frame10.Centre()
        frame10.Show(True)


app = wx.App()
frame = MyFrame(None, "Вычислительная математика")
frame.Centre()
frame.Show(True)
app.MainLoop()