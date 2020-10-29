class My_road():
    lenth = 10
    width = 20
    thickness = 10
    def __init__(self, lenth, width, thickness):
        self.lenth = int(lenth)
        self.width = int(width)
        self.thickness = int(thickness)
        print(f' Требуемая масса асфальта для данной дороги составляет {self.lenth * self.width * self.thickness * 25} т')


m_5 = My_road(20, 30, 10)
m_6 = My_road(10, 30, 10)


