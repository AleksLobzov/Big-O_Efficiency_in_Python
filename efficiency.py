import timeit
from timeit import Timer

print("Let's examine list methods efficiency!")
r = input("Please, enter the range: ")
r = r.split(',')
r[0] = int(r[0])
r[1] = int(r[1])
r[2] = int(r[2])
experiment_number = input('And now type the number of experiments: ')

#index assignment - is it O(1)?
print('list[i] = item - is it O(1)?')
index_timer = Timer('l[0] = l[len(l)-1] = %d' % 1, 'from __main__ import l')
for i in range(r[0], r[1], r[2]):
  l = list(range(i))
  index_time = index_timer.timeit(number = int(experiment_number))
  print('number of items: %-10d' % i, 'execution time: %7.5f' % index_time)

#append() - is it O(1)?
print('list.append(item) - is it O(1)?')
append_timer = Timer('l.append(%d)' % 1, 'from __main__ import l')
for i in range(r[0], r[1], r[2]):
  l = list(range(i))
  append_time = append_timer.timeit(number = int(experiment_number))
  print('number of items: %-10d' % i, 'execution time: %7.5f' % append_time)

#pop() - is it O(1)?
print('list.pop() - is it O(1)?')
pop_timer = Timer('l.pop()', 'from __main__ import l')
for i in range(r[0], r[1], r[2]):
  l = list(range(i))
  pop_time = pop_timer.timeit(number = int(experiment_number))
  print('number of items: %-10d' % i, 'execution time: %7.5f' % pop_time)

#pop(0) - is it O(n)?
print('list.pop(i) - is it O(n)?')
pop_0_timer = Timer('l.pop(0)', 'from __main__ import l')
for i in range(r[0], r[1], r[2]):
  l = list(range(i))
  pop_0_time = pop_0_timer.timeit(number = int(experiment_number))
  print('number of items: %-10d' % i, 'execution time: %7.5f' % pop_0_time)

#insert(0, item) - is it O(n)?
print('list.insert(i, item) - is it O(n)?')
insert_0_timer = Timer('l.insert(0, %d)' % 1, 'from __main__ import l')
for i in range(r[0], r[1], r[2]):
  l = list(range(i))
  insert_0_time = insert_0_timer.timeit(number = int(experiment_number))
  print('number of items: %-10d' % i, 'execution time: %7.5f' % insert_0_time)

