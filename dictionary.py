
articles = {'FEB':[17,20,24]}

while(True):

	new_Key= input()
	
	if new_Key == '':
		break

	if new_key in articles:
		print('key exists!!\n')
		print('mein value daal dunga! bata dijiye bs\n')
		value = input()
		articles[new_Key].append(value)
	else:
		print('value?\n')
		value= input()
		articles[new_key]= [value]

		