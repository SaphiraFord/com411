#Importing ABC, abstract base class to make a class abstract
from abc import ABC, abstractmethod


class Tech(ABC):

  #Creating an abstract method with the keywords "@abstractmethod" and "pass"
  @abstractmethod
  def activate():
    pass

  @abstractmethod
  def deactivate():
    pass