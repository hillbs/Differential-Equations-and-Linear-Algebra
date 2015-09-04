import contacts
from datetime import datetime
import operator

days_list = []
people = contacts.get_all_people()
now = datetime.now()
for p in people:
  b = p.birthday
  if b:
	next_birthday = datetime(now.year, b.month, b.day)
	if next_birthday < now:
	  next_birthday = datetime(now.year + 1, b.month, b.day)
	days = (next_birthday - now).days
	days_list.append({'name': p.full_name, 'days': days})

if not days_list:
  print 'You don\'t have any birthdays in your address book.'
else:
  days_list.sort(key=operator.itemgetter('days'))
  print 'Upcoming Birthdays'
  print '=' * 40
  for item in days_list:
	print '* %s in %i days' % (item['name'], item['days'])
for num in range(280,290): print contacts.get_person(num).name
#The above line works as it calls the contacts list using the id, iterated as num, which 
#allows the fullname to be call based on the id. Saves a lot of pfaffing with lists. 
