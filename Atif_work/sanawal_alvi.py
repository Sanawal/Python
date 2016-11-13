def main():
	num_array = list()
	num = float(raw_input("Enter how many elements you want in array:"))
	print 'Enter values in array: '
	for i in range(int(num)):
	    n = float(raw_input("num :"))
	    num_array.append(float (n))
	print 'Your Entered array: ',num_array
	mean(num_array)
	print 'mean', mean(num_array)
	print 'median', median(num_array)
	print 'mode', mymode(num_array)

def mean(list):
	sum = 0
	for elm in list:
		sum += elm
	return sum/len(list);

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

def mymode(list):
	d = {}
	for elm in list:
		try:
			d[elm] += 1
		except(KeyError):
			d[elm] = 1
	
	keys = d.keys()
	max = d[keys[0]]
	
	for key in keys[1:]:
		if d[key] > max:
			max = d[key]

	max_k = []		
	for key in keys:
		if d[key] == max:
			max_k.append(key),
	return max_k

if __name__ == "__main__":
  main()