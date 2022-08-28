def interview(lst, tot):
	test_list=[5, 5, 10, 10, 15, 15, 20, 20]
	return "qualified" if all(a<=b for a,b in zip(lst,test_list))and len(lst)==8  and tot<=120 else"disqualified"
