Solution
========

Step 1
------

Student needs to create a variable to store their password. ::

  MY_PASSWORD = "SuperSafePa88"

Step 2
------

Student needs to create a dictionary to store the conditions for a safe
password. ::

  PASSWORD_CONDITIONS = {
      "has_lower_letter": False,
      "has_upper_letter": False,
      "has_number": False,
  }

Step 3
------

Students need to know that you can get the values on the dictionary. ::

  PASSWORD_CONDITIONS.values()

Step 4
------

Students need to know that they can discovery if the password is strong using ::

  not False in PASSWORD_CONDITIONS.values()

Instructors need to explain this step very slow!!!

1. ``in`` check if the "left hand side" can be find on the "right hand side".
2. Since ``False`` in `` PASSWORD_CONDITIONS.values()`` means that the password
   is not strong, we need to get the negation of it with ``not``.
  
Step 5
------

Student needs to understand the for-loop concept. ::

  for char in MY_PASSWORD:
      print(char)

Step 6
------

Student needs to know that ``char`` can be asked for the conditions using ::

  char.islower()

for ``har_lower_letter``, ::

  char.isupper()

for ``has_upper_letter``, and ::
  
  char.isdigit()

for ``has_number``.
  
Use ``help(str)`` for the full list.

Step 7
------

This step merge the step 5 and 6.
Students need to print information about the password usin the for-loop and the
string questions. ::

  for char in MY_PASSWORD:
      if char.islower():
          print("{} is lower case".format(char))
      if char.isupper():
          print("{} is upper case".format(char))
      if char.isdigit():
          print("{} is digit".format(char))

Step 8
------

Student now replace the ``print`` with the change on the dictionary. ::

  for char in MY_PASSWORD:
      if char.islower():
          PASSWORD_CONDITIONS["has_lower_letter"] = True
      if char.isupper():
          PASSWORD_CONDITIONS["has_upper_letter"] = True
      if char.isdigit():
          PASSWORD_CONDITIONS["has_number"] = True

      print(PASSWORD_CONDITIONS)

Step 9
------

We use the code from the previous step as the body of our function. ::

  def my_password_is_strong(password):
      for char in password:
          if char.islower():
              PASSWORD_CONDITIONS["has_lower_letter"] = True
          if char.isupper():
              PASSWORD_CONDITIONS["has_upper_letter"] = True
          if char.isdigit():
              PASSWORD_CONDITIONS["has_number"] = True

      return not False in PASSWORD_CONDITIONS.values()

  my_password_is_strong(MY_PASSWORD):

Step 10
-------

Topics for discussions:

1. What happens if you call the function twice when the first time has a strong
   password and the second time has a weak password?

   **Answer**: the second time will return ``True``. You can solve this issue
   by moving the ``PASSWORD_CONDITIONS`` to inside the function.
