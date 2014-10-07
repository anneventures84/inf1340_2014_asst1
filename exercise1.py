""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion
This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). ValueErrors will be raised
for invalid value given on parameter. TypeError will be raised for invalid type passed on parameter

"""
__author__ = 'Anne Simon', 'Grant Wheeler'
__email__ = "anne.simon@mail.utoronto.ca", "grant.wheeler@mail.utoronto.ca"
__copyright__ = "2014 Anne and Grant"


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.
   
    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100
            If string, accepted values are A+, A, A-, B+, B, B-, FZ
           
    :return:
        float: The equivalent GPA
            Value is 0.0-4.0
           
    :raises:
        TypeError: if parameter is not a string or integer
        ValueError: if parameter is out of range
    """
   
    letter_grade = ""  # declare variable for str value
    gpa = 0.0  # variable representing the gpa equivalent of the given grade
    if type(grade) is str:  # if grade given is string
        if grade == " ":  # ensure that grade is not equal to null,otherwise raise Value Error
            raise ValueError("Invalid value given on parameter")
        if grade in ("A+,A,A-,B+,B,B-,FZ"):  # ensure that grade given is a valid letter grade
            letter_grade = grade # assign grade parameter value into variable letter_grade string
        else:  # raise ValueError if value given on parameter is not valid
            raise ValueError("Invalid value given on parameter")
    elif type(grade) is int:  # if grade parameter has an integer value
        letter_grade = mark_to_letter(grade)  # get the letter equivalent of int grade by calling mark_to_grade function
    else:  # if grade is not string or integer, raise TypeError
        raise TypeError("Invalid type passed as parameter")
   
   # Get the letter grade equivalent gpa value
    if letter_grade == "A+" or letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    else:
        gpa = 0.0
        
    # provide the equivalent gpa of given grade
    return gpa

# function to convert grade integer into its grade letter equivalent


def mark_to_letter(grade):
    """
    Convert integer grade to letter.

    :param:
        grade (integer): Grade to be converted
            values are 0-100

    :return:
        string: The equivalent of integer grade
            Value is A+/A/A-/B+/B/B-/FZ

    :raises:
        TypeError: if parameter is not a string or integer
        ValueError: if parameter is out of range
    """

    letter_grade = "" # declare variable for letter_grade equivalent
    if grade >= 0 and grade <= 100:  # get valid grade integer
            if grade > 89:
                letter_grade = "A+"
            elif grade > 84:
                letter_grade = "A"
            elif grade > 79:
                letter_grade = "A-"
            elif grade > 76:
                letter_grade = "B+"
            elif grade > 72:
                letter_grade = "B"
            elif grade > 69:
                letter_grade = "B-"
            else:
                letter_grade = "FZ"
    else:  # raise Value Error if grade integer is not value
            raise ValueError ("Invalid value given on parameter")

    # provide equivalent grade letter
    return letter_grade