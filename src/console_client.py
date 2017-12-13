import unary_tms

print('Increment unary:')
tm_increment = unary_tms.increment('|||', True)
print('Tape before processing: ' + tm_increment.get_tape())
tm_increment.process()
print('Tape after processing: ' + tm_increment.get_tape())


print('\nDecrement unary:')
tm_decrement = unary_tms.decrement('|||||', True)
print('Tape before processing: ' + tm_decrement.get_tape())
tm_decrement.process()
print('Tape after processing: ' + tm_decrement.get_tape())


print('\nAdd unary:')
tm_add = unary_tms.add('|||&||', True)
print('Tape before processing: ' + tm_add.get_tape())
tm_add.process()
print('Tape after processing: ' + tm_add.get_tape())


print('\nSubtract unary:')
tm_subtract = unary_tms.subtract('||||||#|||', True)
print('Tape before processing: ' + tm_subtract.get_tape())
tm_subtract.process()
print('Tape after processing: ' + tm_subtract.get_tape())