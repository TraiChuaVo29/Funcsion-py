def leap_year(year):
    # Xác định năm đó có phải là năm nhuận hay không
    # Nếu là năm nhuận sẽ trả về kết quả là True
    # Nếu không là năm nhuận sẽ trả về kết quả là False
    result = False
    if year % 100 == 0:
        if year % 400 == 0:
            result = True
        else:
            result = False
    else:
        if year % 4 == 0:
            result = True
        else:
            result = False
    return result