# By Ruilin @2010-03-23

from django.core.paginator import Paginator

#-------------------------------------------------------------------------------
# Split records into pages.
#-------------------------------------------------------------------------------
def split_into_pages(request, dict, count = 15):
	pages = Paginator(dict, count)

	page = 1
	if request.GET.has_key('page'):
		page = int(request.GET['page'])
	if pages.num_pages < page:
		page = pages.num_pages

	return pages.page(page)

#-------------------------------------------------------------------------------
# Split [1,2,3,4,5,6,7,8,9,0] =>> [[1,2,3,4,5],[6,7,8,9,0]]
# [1,2,3,4,5] =>> [[1,2,3,4,5]]
#-------------------------------------------------------------------------------
def split_into_lists(list, count = 6): # Kalle: changed from 3 to 6
	new_list = []
	slices = len(list) / count
	for i in range(0, slices):
		new_list.append(list[i * count:(i + 1) * count])

	if list[slices * count : len(list)]:
		new_list.append(list[slices * count : len(list)])

	return new_list

#-------------------------------------------------------------------------------
# Give [1,2,3] [2,5,6], return [1,2,3,5,6]
#-------------------------------------------------------------------------------
def list_or(n1, n2):
	result = [x for x in n1]
	for x in n1:
		if x in n2:
			n2.remove(x)
	result.extend(n2)
	
	return result

def list_and(n1,n2):
	result = []
	for x in n1:
		if x in n2:
			result.append(x)
			
	return result;
		
