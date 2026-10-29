rows = ["Казань,120", "Воронеж,250", "Казань,", "Самара,abc", "Казань,300", "Воронеж,90,лишнее", "Новосибирск,410"]


def sum_by_city(rows):
    sales_by_city = {}
    bad_rows = 0
    for row in rows:
        try:
            city, amount = row.split(",")
            if city not in sales_by_city:
                sales_by_city[city] = int(amount)
            else:
                sales_by_city[city] += int(amount)
        except ValueError:
            bad_rows += 1
    return sales_by_city, bad_rows


totals, bad = sum_by_city(rows)
print(totals)
print("плохих строк:", bad)