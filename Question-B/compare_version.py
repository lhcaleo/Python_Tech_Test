def compare(version_1,version_2):
	if(type(version_1) is not str or type(version_2) is not str):
		raise TypeError("Type Error: input value is not a string")

	try:
		version_1 = list(map(int, version_1.split('.')))
		version_2 = list(map(int, version_2.split('.')))
	except (ValueError):
		raise ValueError("Value Error: input contains non-digit items")

	result = 0
	# if version 1 is longer than version 2
	if(len(version_1) > len(version_2)):
		for i in range(len(version_2)):
			if version_1[i] != version_2[i]:
				if (version_1[i] - version_2[i] > 0):
					result = 1
					break
				if (version_1[i] - version_2[i] < 0):
					result = -1
					break
		if(result != 0):
			return result
		for j in range(len(version_2), len(version_1)):
			if(version_1[j]) > 0:
				result = 1
	# if version 2 is longer than version 1			
	else:
		for i in range(len(version_1)):
			if version_1[i] != version_2[i]:
				if (version_1[i] - version_2[i] > 0):
					result = 1
					break
				if (version_1[i] - version_2[i] < 0):
					result = -1
					break
		if(result != 0):
			return result
		for j in range(len(version_1), len(version_2)):
			if(version_2[j]) > 0:
				result = -1
	return result


