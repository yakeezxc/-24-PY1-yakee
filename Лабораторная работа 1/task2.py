capacity_Mb = 1.44
page_count = 100
str_count = 50
symb_count = 25
bite_per_symb = 4

capacity_b = capacity_Mb * 1024 * 1024 #объем дискеты в байтах
book_capacity = bite_per_symb * symb_count * str_count * page_count #объем одной книги в байтах

print("Количество книг, помещающихся на дискету:", int(capacity_b // book_capacity))
