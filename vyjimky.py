#!/usr/bin/env python3


for i in range(1,101):
   if i % 3 == 0 and i % 5 == 0:
      i="FooBar"
   elif i % 3 == 0:
      i="Foo"
   elif i % 5 == 0:
      i="Bar"
   print(i)


