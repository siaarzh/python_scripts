my_list = [
{'name': 'chair', 'price': 10},
{'name': 'table', 'price': 12}
]


def get_item(name):
	item = next(filter(lambda input_list: input_list['name'] == name, my_list), None)
	return {'item': item}

print(get_item('chair'))