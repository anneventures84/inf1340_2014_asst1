""" Assignment 1, Exercise 2, INF1340, Fall, 2014. UPC Checksum
This module contains one function checksum(upc). Provided that there are 12 digits in the upc, this module will compare
the final digit (i.e., the check digit) against the checksum.
If checkSum equals the computed check digit, it returns an output of True, otherwise it returns False.

ValueErrors will be raised if upc is less than or more than 12.
TypeError will be raised if upc is not string types.

"""
__author__ = 'Anne Simon', 'Grant Wheeler'
__email__ = "anne.simon@mail.utoronto.ca", "grant.wheeler@mail.utoronto.ca"
__copyright__ = "2014 Anne and Grant"


def checksum(upc):

    """
        Checks if the digits in a UPC is consistent with checksum

        :param upc: a 12-digit universal product code

        :return:
            Boolean: True, checksum is correct
            False, otherwise

        :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under)
    """

    upcValidSize = 12
    if type(upc) is str:  # verify if upc value is a string
        upcParamSize = len(upc)  # get the size of upc value and assign into variable upcParamSize
        if upcParamSize < 1:  # if upc size is less than 1, raise Value Error and indicate required size is 12 digits
            raise ValueError("upc is less than the required 12 digits size")
        else:
            if upcParamSize != upcValidSize:  # if upc size is greater than the valid size of 12 digits
                # get excess digits by subtracting upc size against value 12 digits
                upcParamSize = upcParamSize - upcValidSize
                # raise ValueError with message indicating the excess digits
                raise ValueError ("upc is greater than " + str(upcParamSize) +
                                   " digits of the required 12 digits")
    else:
        raise TypeError ("upc is not a string")
    upcArray = list(upc)  # get upc value and covert into array
    # flag to identify odd/even digit position ->True - odd number, False - even number.  Initial value will be
    # True for 1st digit position
    upcFlag = True
    oddCheckSum = 0  # accumulator for odd number
    evenCheckSum = 0  # accumulator for even number
    checkSum = 0  # the check digit which will hold the digit identified on the twelve position of upc value
    for upcCheck in range(len(upcArray)):  # perform loop using the array pointer value based on size of upcArray
        # if array pointer (upcCheck) is equal to 11, it is pointing on the twelve position of upc value
        if upcCheck == 11:
            checkSum = int(upcArray[upcCheck])  # get the check digit and assign into checkSum variable
            break  # stop the loop as 12 position already reached and the check digit was found
        else:  # if not yet on the twelve position, continue accumulating the odd/even numbers
            if upcFlag:  # if the upcFlag is True, it means digit position is in odd number
                upcFlag = False  # assign False to upcFlag as next loop will be for even digit position
                oddCheckSum += int(upcArray[upcCheck])  # accumulate the odd digit position number
            else:  # if upcFlag is not True, then value is False - meaning digit position is an even number
                upcFlag = True  # assign True to upcFlag as next loop will be for odd digit position
                evenCheckSum += int(upcArray[upcCheck])  # accumulate the even digit position number

# multiply the sum of odd digit position values by 3 and add the result on the sum of even digit position values
    derivedCheckSum  = oddCheckSum * 3 + evenCheckSum
    getModCheckSum = derivedCheckSum % 10  # get the remainder (modulo) of the total value when divided by 10
    if getModCheckSum != 0:  # if remainder is not zero perform next statement, otherwise the check digit is zero
        getModCheckSum = 10 - getModCheckSum  # deduct the remainder against value 10
    if checkSum == getModCheckSum:  # if checkSum equals the computed check digit, return True, otherwise False
        return True
    else:
        return False

