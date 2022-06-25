def open_or_senior(data):
    MyData = []
    for datas in data:
        value1 = datas[0]
        value2 = datas[1]
        
        if value1 >= 55 and value2 >= 7:
            MyData.append("Senior")
        else:
            MyData.append("Open")
    return MyData
open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])