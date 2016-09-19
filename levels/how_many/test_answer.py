'''This is the test for this answer.'''


import answer as our_answer
import student_answer 


def test_digits(password):

    expect = our_anwser.how_many_digits(password)
    actual = student_anwser.how_many_digits(password)
    return actual, expect


def test_lower(password):

    expect = our_anwser.how_many_lower(password)
    actual = student_anwser.how_many_lower(password)
    return actual, expect


def test_upper(password):

    expect = our_anwser.how_many_upper(password)
    actual = student_anwser.how_many_upper(password)
    return actual, expect
