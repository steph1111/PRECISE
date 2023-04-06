#!/usr/bin/env python3
"""
Module sig_float contains the sig_float class--instances 
of numbers that behave according to sig fig rules.
"""
__author__ = "Stephanie L'Heureux"

import warnings


class sig_float:
  """
  Defines a numerical float-like type that obides to significant figure rules:
  • All non-zero digits are significant.
  • All captive zeros are significant.
  • Trailing zeros are only significant if they
    follow a decimal point or have a bar written
    above them.
  • Leading zeros are never significant.
  """

  def __init__(self, str_number:str="0")->None:
    """
    Initializes a sig_float object
    'str_number' has a default value of 0 
    """
    # If the user did not provide a string arguement, arguement 
    # is converted to a string and warning is raised
    if not isinstance(str_number, str):
      warnings.warn("Warning: Arguement should be of type str", PendingDeprecationWarning)
      str_number = str(str_number)
    
    # Initializations
    self._str = str_number
    self._sig_figs = self.sig_figs()
    self._precision = self.precision()
    self._float = float(self._str)

  def sig_figs(self)->int:
    """
    Returns the number of sig figs of a sig_float object
    """
    # Default start and end
    start = 0
    end = len(self._str)
    negative = False

    # Account for negative
    if self._str[0] == "-":
      negative = True
      self._str = self._str[1:]    
   
    # Find stopping point of leading zeros
    for digit in self._str:
      if digit != "0":
        break
      start += 1

    # Find stopping point of trailing zeros
    if self._str.find(".") != -1:
      self._str = self._str[start:] # Update string representation
      # Add the negative back in
      if negative:
        self._str = "-" + self._str
        start += 1
      return end - start - 1 # -1 to account for the "." char
    else:
      # Add the negative back in
      if negative:
        self._str = "-" + self._str
        start += 1
      # Iterate reversed string to find stopping point of trailing zeros
      string_num_reversed = reversed(self._str)
      for digit in string_num_reversed:
        if digit != "0":
          break
        end -= 1
    self._str = self._str[start:end] # Update string representation
  
    return end - start
  
  def precision(self)->int:
    """
    Returns the number of decimal places to which the number is percise to
    """
    index_decimal = self._str.find(".")
    if index_decimal != -1:
      return len(self._str) - self._str.find(".") -1
    return 0
  
  #TODO: Help!!
  def round_sig(self, sig_figs:int):
    # Determine the number of valid digits in the number
    # negative = False
    digits = len(self._str)
    if self._str.find(".") != -1:
      digits -= 1
    if self._str[0] == "-":
      digits -= 1
  
  # TODO: Implicate
  def scientific(self):
    pass
  
  def __mul__(self, other): # ->sig_float
    """
    Multiplies two numbers of type sig_float with * using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Multiplication using sig fig rules  
    product = self._float * other._float
    product_sig_figs = min(self._sig_figs, other.sig_figs())
    
    # FIXME Rounding causing issue?????
    return sig_float("404")
  
  def __truediv__(self, other): # ->sig_float
    """
    Divides two numbers of type sig_float with / using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Multiplication using sig fig rules  
    quotient = self._float / other._float
    quotient_sig_figs = min(self._sig_figs, other.sig_figs())
    
    # FIXME Rounding causing issue????? See _round_sig()
    return sig_float("404")

  def __add__(self, other): # ->sig_float
    """
    Adds two numbers of type sig_float with + using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)
    
    # Addition using sig fig rules
    sum = self._float + other._float
    sum_precision = min(self._precision, other._precision)
    temp_str = str(round(sum, sum_precision))

    # Remove trailing decimal python adds
    if sum_precision == 0:
      return sig_float(temp_str[:-2])

    return sig_float(temp_str)

  def __sub__(self, other): # ->sig_float
    """
    Subtracts two numbers of type sig_float with + using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Subtraction using sig fig rules
    diff = self._float - other._float
    diff_precision = min(self._precision, other._precision)
    temp_str = str(round(diff, diff_precision))
  
    # Remove trailing decimal python adds
    if diff_precision == 0:
      return sig_float(temp_str[:-2])
  
    return sig_float(temp_str)
  
  @property
  def numeric(self)->float:
    """
    Returns a float representation of the number, may have improper sig figs. Use with caution!!
    Call by object.numeric
    """
    return self._float

  @property
  def string(self)->str:
    """
    Returns a string represntation of the number
    Call by object.string
    """
    return self._str

  def __str__(self)->str:
    """
    Returns a string represntation of the number with correct sig figs
    """
    return self._str
  
  def __bool__(self)->bool:
    """
    Applies standard numeric to bool coversions. 0 is false, non-zero is true
    """
    return bool(self._float)
  
  def __float__(self)->float:
    """
    Returns a float represntation of the number, may have improper sig figs. Use with caution!!
    """
    return self._float
  
  def __repr__(self)->str:
    return f"{type(self).__name__}('{self}')"
  
  def __eq__(self, other)->bool:
    """
    Evaluates if two numbers of type sig_float are equal
    """
    # TODO: Ask how equality should work
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._str == other._str

  def __ne__(self, other)->bool:
    """
    Evaluates if two numbers of type sig_float are not equal
    """
    # TODO: Ask how equality should work
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._str != other._str

  
  def __lt__(self, other)->bool:
    """
    Evaluates if a number is less than another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float < other._float
  
  def __le__(self, other)->bool:
    """
    Evaluates if a number is less or equal to than another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float <= other._float

  def __gt__(self, other)->bool:
    """
    Evaluates if a number is greater than another number.
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float > other._float
  
  def __ge__(self, other)->bool:
    """
    Evaluates if a number is greater than or equal to another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float >= other._float


if __name__ == "__main__":
  this = sig_float("0001633.00")
  # print(this)
  # print(this) 
  # print(f"This: {this.sig_figs()}")
  that = sig_float("01623003.912") 
  # print(f"This: {that.sig_figs()}")
  # print(this * that)
  # result = sig_float(str(this * that))
  # print(result)