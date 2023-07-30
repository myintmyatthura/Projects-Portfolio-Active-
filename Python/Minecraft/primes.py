from __future__ import annotations

__author__ = ''
__docformat__ = 'reStructuredText'

class LargestPrimeIterator():
    """
        CLASS DESCRIPTION:
        LargestPrimeIterator class that generates and iterates prime numbers based off the input parameters
        it is given
    """
    def __init__(self, upper_bound: int, factor: int):
        """ 	
            PARAMETERS:
            objects instantiated:
            -   upper_bound[integer]: the integer that the largest prime number found should be less than
            -   factor[integer]: a multiplier that is used to update the upper_bound when a new prime number 
                is computed.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   __init__ magic method to initialise the upper_bound and factor of the class
            -   upper_bound and factor will be passed into the init function,
            -   rest of the instance variables will be defaulted
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: it's an __init__ function
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables
        """
        self.upper_bound = upper_bound
        self.prime_num = 0
        self.factor = factor

    def __next__(self):
        """
            PARAMETERS:
            the instances of LargestPrimeIterator
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            A magic method that returns the next item in the sequence of the iterator.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            num[int]: the largest prime number that is lesser than upper_bound.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(log(N)), where N is num

            COMPLEXITY FOR WORST CASE:
            O(N log(N)), where N is num  
        """
        num = self.upper_bound - 1
        if num < 2:
            return False
        #if num % 2 == 0: # even number
        #    break
        is_prime_bool = False
        while num >= 2 and not is_prime_bool:
            #print(num)
            #if num % 2 == 0: # even number
            #    break
            i = 2
            ag = (num//2) + 1 # 5
            #print(i)
            #print(ag)
            while i <= ag: # 7 <= 5 for early exit but 6 <= 5 for all prime num
            #for i in range(2, (num//2) + 2): # between 2 to n/2
                #print(num%i)
                if num % i == 0: # if num is not prime
                    #prime_bool = False
                    num -= 1 # decrement the num amount
                    i = ag + 2 # 7
                else:
                    i += 1 # 6
                    #break
            # all the loop
            gy = ag + 1 # 6
            if i <= gy: #
                is_prime_bool = True

            #i = 2
            #if is_prime_bool:
            #    num -= 1
            #    prime_bool = True
            #    self.prime_num = num
            #num -= 1 # decrement the num amount

        self.upper_bound = num * self.factor
        return num


    def __iter__(self):
        """
            PARAMETERS:
            the instances of LargestPrimeIterator
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            a magic method that allows the Largest Prime Iterator to be iterable
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            the iterator object (LargestPrimeIterator) as an iterable; the result of every next call
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(__next__) 
        """
        return self
    #raise NotImplementedError()

if __name__ == "__main__":
    a = LargestPrimeIterator(6, 2)
    for i in range(10):
        print(next(a))

