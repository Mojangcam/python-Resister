class Resistor(object):
    def __init__(self) -> None:
        self.resistor_value = 0
        self.resistor_percent = 0
        self.resistor_color_value_list = []
        self.color_value = "검갈빨주노초파보회흰금은없"
       
    # 저항의 값을 계산하는 함수
    def resistor_value_calculate(self, color_num:int) -> dict:
            #문자열로 합치고 정수로 변환하여 계산하는 방식 선택
            # 컬러 개수가 4개인 경우
        if color_num == 4:
            string = str(self.resistor_color_value_list[0]) + str(self.resistor_color_value_list[1])
            power = self.resistor_color_value_list[2]
            #컬러 개수가 5개인 경우
        if color_num == 5:
            string = str(self.resistor_color_value_list[0]) + str(self.resistor_color_value_list[1]) + str(self.resistor_color_value_list[2])
            power = self.resistor_color_value_list[3]
           
        if power > 11 or self.resistor_percent == 0:
            raise Exception("Resistor color value Error")
        value = int(string) * (10 ** power)
        plma = value / 100 * self.resistor_percent
        resistor_min = int(value - plma)
        resistor_max = int(value + plma)
        # 값을 전달할때 dictionary로 전달
        context = {
            "resistor_min" : resistor_min,
            "resistor_max" : resistor_max,
            "resistor_value" : value,
            "resistor_percent" : self.resistor_percent
        }
        return context

    # 저항의 값을 구하는 함수
    def resistor_value_get(self, colors:str) -> None:
        if len(colors) < 4 and len(colors) > 5 and colors[0] == "검":
            raise Exception(f"Resistor color Error : {colors}")
     
        for i in range(len(colors)):
            if colors[i] in self.color_value:
                find_color_index = self.color_value.find(colors[i])
                self.resistor_color_value_list.append(find_color_index)
                # 마지막 컬러가 오차범위를 나타내는 컬러일 경우
                if i == len(colors) - 1:
                    if find_color_index == 1:
                        self.resistor_percent = 1
                    elif find_color_index == 2:
                        self.resistor_percent = 2
                    elif find_color_index == 5:
                        self.resistor_percent = 0.5
                    elif find_color_index == 6:
                        self.resistor_percent = 0.25
                    elif find_color_index == 7:
                        self.resistor_percent = 0.1
                    elif find_color_index == 8:
                        self.resistor_percent = 0.05
                    elif find_color_index == 10:
                        self.resistor_percent = 5
                    elif find_color_index == 11:
                        self.resistor_percent = 10
                    elif find_color_index == 12:
                        self.resistor_percent = 20
        for i in range(len(self.resistor_color_value_list)):
            if i == 0:
                #첫번째 색깔은 검은색,금색,은색,없음이 올수 없기 때문에 에러 발생
                if self.color_value[self.resistor_color_value_list[i]] in "검금은없":
                    raise Exception(f"Resistor color Error : {colors}")
                # 금은없 은 숫자가 아닌 오차범위 (%)를 나타내기 때문에 올수 없어서 에러 발생
            if i < len(self.resistor_color_value_list) - 1:
                if self.color_value[self.resistor_color_value_list[i]] in "금은없":
                    raise Exception(f"Resistor color Error : {colors}")
                   
        return self.resistor_value_calculate(len(colors))
        # 저항의 값을 Giga, Mega, kilo 옴으로 변환해주는 함수
    def resistor_unit_convert(self, context:dict):
        res_min = context['resistor_min']
        res_max = context['resistor_max']
        res_value = context['resistor_value']
        res_percent = context['resistor_percent']
        if res_value > 1000000000:
            return "GΩ", res_min/1000000000, res_max/1000000000, res_value/1000000000, res_percent
       
        elif res_value > 1000000:
            return "MΩ", res_min/1000000, res_max/1000000, res_value/1000000, res_percent
       
        elif res_value > 1000:
            return "kΩ", res_min/1000, res_max/1000, res_value/1000, res_percent
       
        return "Ω", res_min, res_max, res_value, res_percent
