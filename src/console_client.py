import tms

tm_increment = tms.increment('|||')
tm_increment.process()
print(tm_increment.get_tape())
