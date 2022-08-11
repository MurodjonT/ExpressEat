from django.test import TestCase

natija = 0
dict1 = [
	{
		"savol":"1.savol?: ","javoblari": [
			{"matn":"1.javob"},
			{"matn":"2.javob"}
			]
	},
	{
		"savol":"2.savol?: ","javoblari": [
			{"matn":"1s.javob"},
			{"matn":"2s.javob"}
			]
	},
]
# print(dict1[0]['savol'])
# print(dict1[0]['javoblari'][0]['matn'])
print('********************************')


sanoq = 0
while sanoq < len(dict1):
	print(dict1[sanoq]['savol'])
	print(dict1[sanoq]['javoblari'][0]['matn'])
	print(dict1[sanoq]['javoblari'][1]['matn'])
	print(dict1[sanoq]['javoblari'][0])
	print(dict1[sanoq]['javoblari'][1])
	z = input("Javob: ")
	if z == dict1[0]['javoblari'][1]['matn']:
		natija += 1
	elif z == dict1[1]['javoblari'][1]['matn']:
		natija += 1
	sanoq += 1




# for i in dict1:
# 	print(i['savol'])
# 	print(i['javoblari'][0]['matn'])
# 	print(i['javoblari'][1]['matn'])
# 	z = input("Javob: ")
# 	if z == i['javoblari'][0]['matn'] or z == i['javoblari'][1]['matn']:
# 		natija += 1


print(f"To'plangan natija {natija}")




