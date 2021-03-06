""""
Test 2, problem 2.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Hussein Alawami.  October 2016.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import sys


def main():
    """ Calls the   TEST   functions in this module. """

    ####################################################################
    # STUDENTS:  UN-comment these tests as you work the problems.
    ####################################################################

#     test_init()
#     test_get_full_name()
#     test_give_money_to()
#     test_get_most_recently_given_amount()
    test_make_baby_with()


########################################################################
# The   Person   class (and its methods) begins here.
########################################################################

class Person(object):
    """
    A Person has:
        -- a first_name, which is a string,
        -- a last_name, which is a string, and
        -- a number, which is the amount of money
             that the Person has.
    """

    def __init__(self, first_name, last_name, money):
        """
        What comes in:
          -- a first_name, which is a string,
          -- a last_name, which is a string, and
          -- a non-negative number (the amount of money
               that the Person starts out with)
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Stores the Persons's first_name, last_name and money
             in the instance variables:
                  self.first_name
                  self.last_name
                  self.money
          -- Also initializes other instance variables as needed
              by other methods.
        Examples:
          person1 = Person('Mohandas', 'Gandhi', 400)
            #   person1.first_name   is now 'Mohandas'
            #   person1.last_name    is now 'Gandhi'
            #   person1.money        is now 400

          person2 = Person('John', 'Kennedy', 80000)
            #   person2.first_name   is now 'John'
            #   person2.last_name    is now 'Kennedy'
            #   person2.money        is now 80000

        Type hints:
          :type first_name: str
          :type last_name:  str
          :type money:      float
        """
        self.first_name = first_name
        self.last_name = last_name
        self.money = money
        self.countMoney = 0

        # --------------------------------------------------------------
        # done: 2. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def get_full_name(self):
        """
        What comes in:
          -- self
        What goes out:
          Returns a string that is this Person's full name.
        Side effects:
          -- Whatever other methods require (if anything).
        Examples:
          gandhi = Person('Mohandas', 'Gandhi', 400)
          name = gandhi.get_full_name()
            # name   is now 'Mohandas Gandhi'

          kennedy = Person('John', 'Kennedy', 80000)
          name = kennedy.get_full_name()
            # name   is now 'John Kennedy'

          name = gandhi.get_full_name()
            # name   is now 'Mohandas Gandhi'
        """
        return self.first_name + ' ' + self.last_name

        # --------------------------------------------------------------
        # done: 3. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def give_money_to(self, other_person, amount_to_give):
        """
        What comes in:
          -- self
          -- Another Person.
          -- A non-negative integer that is no more than the amount of
               money that this Person currently has.
        What goes out:  Nothing (i.e., None)
        Side effects:
          -- Decreases this Person's money by the given amount_to_give.
          -- Increases the other Person's money
               by the given amount_to_give.
          -- Also, whatever other methods require (if anything).
        Examples:
          gandhi = Person('Mohandas', 'Gandhi', 400)
          kennedy = Person('John', 'Kennedy', 80000)
          smith = Person('Dana', 'Smith', 5000)

          gandhi.give_money_to(kennedy, 300)

          print(gandhi.money,
                kennedy.money,
                smith.money)  # Should print:  100  80300  5000

          kennedy.give_money_to(smith, 30000)

          print(gandhi.money,
                kennedy.money,
                smith.money)  # Should print:  100  50300  35000

        Type hints:
          :type other_person:         Person
          :type amount_to_give: int
        """
        self.money -= amount_to_give
        other_person.money += amount_to_give
        self.countMoney = amount_to_give
        # --------------------------------------------------------------
        # done: 4. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def get_most_recently_given_amount(self):
        """
        What comes in:
          -- self
        What goes out:
          Returns the amount of money given via the most recent
            call that this Person has made to  give_money_to.
          Returns 0 if this Person has not yet called  give_money_to.
        Side effects:
          -- Whatever other methods require (if anything).
        Examples:
          gandhi = Person('Mohandas', 'Gandhi', 400)
          kennedy = Person('John', 'Kennedy', 80000)
          smith = Person('Dana', 'Smith', 5000)

          # The following should print:  0  0  0
          print(gandhi.get_most_recently_given_amount(),
                kennedy.get_most_recently_given_amount(),
                smith.get_most_recently_given_amount())

          kennedy.give_money_to(gandhi, 5000)
          gandhi.give_money_to(smith, 2000)
          kennedy.give_money_to(gandhi, 10000)

          # The following should print:  2000  10000  0
          print(gandhi.get_most_recently_given_amount(),
                kennedy.get_most_recently_given_amount(),
                smith.get_most_recently_given_amount())
        """
        # --------------------------------------------------------------
        # done: 5. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

        return self.countMoney

    def make_baby_with(self, spouse, child_name):
        """
        What comes in:
          -- self
          -- Another Person.
          -- A string that can be used as the first name of the
               Person (child) that this method returns
        What goes out:
          Returns a new Person whose:
              -- first name is the given child_name
              -- last name is the same as this Person's last name
              -- money is:
                     half of this Person's current money
                   + half of the given spouse's current money
        Side effects:
          -- Reduces this Person's money
               to half of what it currently is.
          -- Reduces the given spouse's money
               to half of what it currently is.
          -- Also, whatever other methods require (if anything).
        Examples:
          gandhi = Person('Mohandas', 'Gandhi', 400)
          kapidia = Person('Kasturba', 'Kapidia', 6000)

          child = gandhi.make_baby_with(kapidia, 'Harilal')

          #   gandhi.money   is now 200
          #   kapidia.money   is now 3000
          #   child.first_name   is now 'Harilal'
          #   child.last_name    is now 'Gandhi'
          #   child.money        is now 3200

        Type hints:
          :type spouse: Person
          :type child_name: str
        """
        self.last_name = self.last_name
        child = Person(child_name, self.last_name, 0)
        self.give_money_to(child, self.money * 1 / 2 + 1 - 1)
        spouse.give_money_to(child, spouse.money * 1 / 2)
        return child
        # --------------------------------------------------------------
        # done: 6. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

########################################################################
# The TEST functions for the  Person  class begin here.
########################################################################


# ----------------------------------------------------------------------
# These first two methods are used in most of the tests:
# ----------------------------------------------------------------------
def test_instance_variables(person, expected_first_name,
                            expected_last_name, expected_money):
    """
    Tests whether the instance variables for the given person
    are per the given expected values.
      type: person:   Person
    """
    print()
    format_string = '{:9}  {:11} {:11} {:<6}'
    print(format_string.format('', 'first_name', 'last_name', 'money'))
    print(format_string.format('Expected:',
                               expected_first_name,
                               expected_last_name,
                               expected_money))
    print(format_string.format('Actual:',
                               person.first_name,
                               person.last_name,
                               person.money))
    if ((expected_first_name == person.first_name)
        and (expected_last_name == person.last_name)
        and (round(expected_money, 6) == round(person.money, 6))):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()


def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=1.0):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message,
          file=sys.stderr, flush=True)
    time.sleep(flush_time)


# ----------------------------------------------------------------------
# test_init:
# ----------------------------------------------------------------------
def test_init():
    """ Tests the   __init__   method of the Person class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Person class.')
    print('-----------------------------------------------------------')

    # Test 1: Constructing one person:
    person1 = Person('Mohandas', 'Gandhi', 400)

    expected_first_name = 'Mohandas'
    expected_last_name = 'Gandhi'
    expected_money = 400

    test_instance_variables(person1, expected_first_name,
                            expected_last_name, expected_money)

    # Test 2: Constructing another person:
    person2 = Person('John', 'Kennedy', 80000)

    expected_first_name = 'John'
    expected_last_name = 'Kennedy'
    expected_money = 80000

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)


# ----------------------------------------------------------------------
# test_get_full_name:
# ----------------------------------------------------------------------
def test_get_full_name():
    """ Tests the   get_full_name   method of the Person class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_full_name   method of the Person class.')
    print('-----------------------------------------------------------')

    # Construct two Person objects for these tests:
    person1 = Person('Mohandas', 'Gandhi', 400)
    person2 = Person('John', 'Kennedy', 80000)

    # Test 1: Full name for person1:
    print()
    expected = 'Mohandas Gandhi'
    actual = person1.get_full_name()
    print('Expected from get_full_name():', expected)
    print('Actual   from get_full_name():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'Mohandas'
    expected_last_name = 'Gandhi'
    expected_money = 400

    test_instance_variables(person1, expected_first_name,
                            expected_last_name, expected_money)

    # Test 2: Full name for person2:
    print()
    expected = 'John Kennedy'
    actual = person2.get_full_name()
    print('Expected from get_full_name():', expected)
    print('Actual   from get_full_name():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'John'
    expected_last_name = 'Kennedy'
    expected_money = 80000

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)


# ----------------------------------------------------------------------
# test_give_money_to:
# ----------------------------------------------------------------------
def test_give_money_to():
    """ Tests the   give_money_to    method of the Person class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   give_money_to   method of the Person class.')
    print('-----------------------------------------------------------')

    # Construct three Person objects for these tests:
    person1 = Person('Mohandas', 'Gandhi', 400)
    person2 = Person('John', 'Kennedy', 80000)
    person3 = Person('Dana', 'Smith', 5000)

    # Test 1: person1 gives 300 to person2
    print()
    print('Test 1: person1 gives 300 to person2')
    returned_value = person1.give_money_to(person2, 300)

    expected_first_name = 'Mohandas'
    expected_last_name = 'Gandhi'
    expected_money = 100

    test_instance_variables(person1, expected_first_name,
                            expected_last_name, expected_money)

    expected_first_name = 'John'
    expected_last_name = 'Kennedy'
    expected_money = 80300

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)

    if returned_value is not None:
        message = '  *** FAILED the above test. ***\n'
        message += 'The method should NOT have returned a value.\n'
        message += 'but it returned: {}'.format(returned_value)
        print_failure_message(message)

    # Test 2: person2 gives 30000 to person3
    print()
    print('Test 2: person2 gives 30000 to person3')
    returned_value = person2.give_money_to(person3, 30000)

    expected_first_name = 'John'
    expected_last_name = 'Kennedy'
    expected_money = 50300

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)

    expected_first_name = 'Dana'
    expected_last_name = 'Smith'
    expected_money = 35000

    test_instance_variables(person3, expected_first_name,
                            expected_last_name, expected_money)

    if returned_value is not None:
        message = '  *** FAILED the above test. ***\n'
        message += 'The method should NOT have returned a value.\n'
        message += 'but it returned: {}'.format(returned_value)
        print_failure_message(message)


# ----------------------------------------------------------------------
# test_get_most_recently_given_amount:
# ----------------------------------------------------------------------
def test_get_most_recently_given_amount():
    """
    Tests the   get_most_recently_given_amount    method
    of the Person class.
    """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_most_recently_given_amount   method')
    print('of the Person class.')
    print('-----------------------------------------------------------')

    # Construct three Person objects for these tests:
    person1 = Person('Mohandas', 'Gandhi', 400)
    person2 = Person('John', 'Kennedy', 80000)
    person3 = Person('Dana', 'Smith', 5000)

    ####################################################################
    # Test 1: No one has given money to anyone.
    ####################################################################
    print()
    print('Test 1: no one has given money to anyone.')

    print()
    print('Checking person1:')
    expected = 0
    actual = person1.get_most_recently_given_amount()
    print('Expected from get_most_recently_given_amount():', expected)
    print('Actual   from get_most_recently_given_amount():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'Mohandas'
    expected_last_name = 'Gandhi'
    expected_money = 400

    test_instance_variables(person1, expected_first_name,
                            expected_last_name, expected_money)

    print()
    print('Checking person2:')
    expected = 0
    actual = person2.get_most_recently_given_amount()
    print('Expected from get_most_recently_given_amount():', expected)
    print('Actual   from get_most_recently_given_amount():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'John'
    expected_last_name = 'Kennedy'
    expected_money = 80000

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)

    print()
    print('Checking person3:')
    expected = 0
    actual = person3.get_most_recently_given_amount()
    print('Expected from get_most_recently_given_amount():', expected)
    print('Actual   from get_most_recently_given_amount():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'Dana'
    expected_last_name = 'Smith'
    expected_money = 5000

    test_instance_variables(person3, expected_first_name,
                            expected_last_name, expected_money)

    ####################################################################
    # Test 2: Several calls to give_money_to:
    ####################################################################
    print()
    print('Test 2: person2 gives person1 5000')
    print('   then person1 gives person3 2000')
    print('   then person2 gives person1 10000.')
    person2.give_money_to(person1, 5000)
    person1.give_money_to(person3, 2000)
    person2.give_money_to(person1, 10000)

    person1_expected_money = 13400
    person2_expected_money = 65000
    person3_expected_money = 7000

    print()
    print('Checking person1:')
    expected = 2000
    actual = person1.get_most_recently_given_amount()
    print('Expected from get_most_recently_given_amount():', expected)
    print('Actual   from get_most_recently_given_amount():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'Mohandas'
    expected_last_name = 'Gandhi'
    expected_money = person1_expected_money

    test_instance_variables(person1, expected_first_name,
                            expected_last_name, expected_money)

    print()
    print('Checking person2:')
    expected = 10000
    actual = person2.get_most_recently_given_amount()
    print('Expected from get_most_recently_given_amount():', expected)
    print('Actual   from get_most_recently_given_amount():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'John'
    expected_last_name = 'Kennedy'
    expected_money = person2_expected_money

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)

    print()
    print('Checking person3:')
    expected = 0
    actual = person3.get_most_recently_given_amount()
    print('Expected from get_most_recently_given_amount():', expected)
    print('Actual   from get_most_recently_given_amount():', actual)

    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Instance variables should NOT have changed:
    expected_first_name = 'Dana'
    expected_last_name = 'Smith'
    expected_money = person3_expected_money

    test_instance_variables(person3, expected_first_name,
                            expected_last_name, expected_money)


# ----------------------------------------------------------------------
# test_make_baby_with:
# ----------------------------------------------------------------------
def test_make_baby_with():
    """ Tests the   make_baby_with    method of the Person class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   make_baby_with   method of the Person class.')
    print('-----------------------------------------------------------')

    # Construct two Person objects for these tests:
    person1 = Person('Mohandas', 'Gandhi', 400)
    person2 = Person('Kasturba', 'Kapidia', 6000)

    # Test 1: person1 and person2 have a baby named 'Harilal'
    print()
    print('Test 1: Mohandas Gandhi and Kasturba Kapidia have a baby named "Harilal"')
    child = person1.make_baby_with(person2, 'Harilal')

    print()
    print('Checking the child:')

    if type(child) is not Person:
        message = '  *** FAILED the above test. ***\n'
        message += 'The method should have returned a Person.\n'
        message += 'but it returned: {}\n'.format(child)
        message += 'which is a   {}   object.'.format(type(child))

        print_failure_message(message)
        return

    expected_first_name = 'Harilal'
    expected_last_name = 'Gandhi'
    expected_money = 3200

    test_instance_variables(child, expected_first_name,
                            expected_last_name, expected_money)

    expected_first_name = 'Mohandas'
    expected_last_name = 'Gandhi'
    expected_money = 200

    test_instance_variables(person1, expected_first_name,
                            expected_last_name, expected_money)

    expected_first_name = 'Kasturba'
    expected_last_name = 'Kapidia'
    expected_money = 3000

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)

    # Second test
    # Construct two Person objects for these tests:
    person1 = Person('Romeo', 'Montague', 0)
    person2 = Person('Juliet', 'Capulet', 100000)

    # Test 1: person1 and person2 have a baby named 'Mercutio'
    print()
    print('Test 1: Romeo Montague and Juliet Capulet have a baby named "Mercutio"')
    child1 = person1.make_baby_with(person2, 'Mercutio')
    child2 = person2.make_baby_with(person1, 'Mercutio2')

    print()
    print('Checking the child:')

    if type(child1) is not Person:
        message = '  *** FAILED the above test. ***\n'
        message += 'The method should have returned a Person.\n'
        message += 'but it returned: {}\n'.format(child)
        message += 'which is a   {}   object.'.format(type(child))

        print_failure_message(message)
        return
    if type(child2) is not Person:
        message = '  *** FAILED the above test. ***\n'
        message += 'The method should have returned a Person.\n'
        message += 'but it returned: {}\n'.format(child)
        message += 'which is a   {}   object.'.format(type(child))

        print_failure_message(message)
        return

    expected_first_name = 'Mercutio'
    expected_last_name = 'Montague'
    expected_money = 50000

    test_instance_variables(child1, expected_first_name,
                            expected_last_name, expected_money)
    expected_first_name = 'Mercutio2'
    expected_last_name = 'Capulet'
    expected_money = 25000

    test_instance_variables(child2, expected_first_name,
                            expected_last_name, expected_money)

    expected_first_name = 'Romeo'
    expected_last_name = 'Montague'
    expected_money = 0

    test_instance_variables(person1, expected_first_name,
                            expected_last_name, expected_money)

    expected_first_name = 'Juliet'
    expected_last_name = 'Capulet'
    expected_money = 25000

    test_instance_variables(person2, expected_first_name,
                            expected_last_name, expected_money)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
