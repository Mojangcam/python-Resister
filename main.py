from resistor import ResistorCalculator
       
if __name__ == '__main__':
    resistor_color = input("저항값을 입력하세요 (4 ~ 5개의 색깔만 허용합니다.) : ")
    resistor1 = Resistor()
    resistor_value = resistor1.resistor_value_get(resistor_color)
    unit, res_min, res_max, res_value, res_percent = resistor1.resistor_unit_convert(resistor_value)
    print(f"저항값의 최솟값 : {res_min}{unit}")
    print(f"저항값의 최댓값 : {res_max}{unit}")
    print(f"저항값 : {res_value}{unit}")
    print(f"저항 오차 : {res_percent}%")
