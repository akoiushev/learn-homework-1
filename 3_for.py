"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
from optparse import Values


lists = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    index_element = 0
    for value in lists:
        sum_of_values = lists[index_element].get('items_sold')
        print(f"Общее количество продаж {lists[index_element]['product']} = {sum(sum_of_values)}")
        print(f"Среднее количество продаж {lists[index_element]['product']} = {(sum(sum_of_values)) / len(lists[index_element].get('items_sold')):.2f}")
        index_element += 1
    all_sales = lists[0]['items_sold'] + lists[1]['items_sold'] + lists[2]['items_sold']
    print(f"Суммарное количество продаж всех товаров = {sum(lists[0]['items_sold'] + lists[1]['items_sold'] + lists[2]['items_sold'])}")
    print(f"Cреднее количество продаж всех товаров = {sum(all_sales) / len(all_sales)}")
    
if __name__ == "__main__":
    main()
