def total_revenue(purchases): #Рассчитайте и верните общую выручку (цена * количество для всех записей)
  return sum(i['price']*i['quantity'] for i in purchases)

def items_by_category(purchases): #Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории
  category_list = {}
  for i in purchases:
    category_list.setdefault(i['category'], set()).add(i['item'])
  return category_list
  return {key: list(value) for key, value in category_list.items()}

def expensive_purchases(purchases, min_price): #Выведите все покупки, где цена товара больше или равна min_price
  return [i for i in purchases if i['price'] >= min_price]

def average_price_by_category(purchases): #Рассчитайте среднюю цену товаров по каждой категории
  avg_price = {}
  for i in purchases:
    category = i['category']
    if category not in avg_price:
      avg_price[category] = [0.0, 0]
    avg_price[category][0] += i['price']
    avg_price[category][1] += 1
  return {key: value[0]/value[1] for key, value in avg_price.items()}

def most_frequent_category(purchases): #Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity)
  top_category = {}
  for i in purchases:
    top_category[i['category']] = top_category.get(i['category'], 0) + i['quantity']
  return (max(top_category, key=top_category.get))

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
print('Общая выручка:', total_revenue(purchases))
print('Товары по категориям:', items_by_category(purchases))
print('Покупки дороже 1.0:', expensive_purchases(purchases, 1.0))
print('Средняя цена по категориям:', average_price_by_category(purchases))
print('Категория с наибольшим количеством проданных товаров:', most_frequent_category(purchases))
