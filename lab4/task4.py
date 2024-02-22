import datetime
x = datetime.datetime(int(input()),int(input()),int(input()),int(input()),int(input()),int(input()))
y = datetime.datetime(int(input()),int(input()),int(input()),int(input()),int(input()),int(input()))
z = (x - y).total_seconds()
print(z)
