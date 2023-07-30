""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
"""
from __future__ import annotations
__author__ = 'Brendon Taylor. Modified by Graeme Gange, Alexey Ignatiev, and Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'


from referential_array import ArrayR
from typing import TypeVar, Generic
from primes import LargestPrimeIterator
T = TypeVar('T')


class LinearProbeTable(Generic[T]):
    """
        CLASS DESCRIPTION:
        The LinearProbeTable is a Hash Table DataType that implements Linear Probing so that open adressing 
        may be used to resolve collisions.

        attributes:
            count: number of elements in the hash table
            table: used to represent our internal array
            tablesize: current size of the hash table
    """

    def __init__(self, expected_size: int, tablesize_override: int = -1) -> None:
        """
            PRECONDITIONS:
            -   expected size must be an integer
            -   tablesize_override must be an integer; if no table_size override parameter is given 
                it is initialised as -1
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            objects instantiated:
            -   expected_size[integer]: the maximum number of elements that will be added to the hash table
            -   tablesize_override[integer]: used to set the tablesize to the exact value of tablesize_override.
                if not instantiated a reasonable choice for tablesize is made in place.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            FUNCTION DESCRIPTION:
            -   __init__ magic method to initialise the LinearProbeTable
            -   expected_size and tablesize_override will be passed into the init function,
            -   the rest of the attributes of the LinearProbeTable will be defaulted, and updated as items
                are added into the table.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: it's an __init__ function
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables and checks for preconditions 
        """
        if tablesize_override != -1:
            self.tablesize = tablesize_override
        else:
            self.tablesize = expected_size * 2
        self.count = 0  # no. of items in the hash table
        self.table = ArrayR(self.tablesize)
        self.conflict_count = 0 # total no. of conflicts
        self.probe_total = 0    # total distance probed 
        self.probe_max = 0  # length of the longest probe chain
        self.rehash_count = 0   # no. of times rehashed
        

    def hash(self, key: str) -> int:
        """
            Hash a key for insertion into the hashtable.
        """
        """
        PARAMETERS:
        the instances of LinearProbeTable class
        key[string]: the key to be hashed into the hashtable
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        METHOD DESCRIPTION:
        -   performs a hash on the key inserted as a parameter that will be used as the index position  
            where an item will be inserted.
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        RETURN:
        value[integer]: an integer that signifies the index the item should be added in for the hash table
        ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
        COMPLEXITY FOR BEST CASE:
        O(log(N)), where is the time complexity of LargestPrimeIterator (see primes.py), LargestPrimeIterator
        is iterated through 3 times (once for b, twice for a) only, and the length of key is 1 (e.g. "a") and 
        therefore the for loop only iterates once.

        COMPLEXITY FOR WORST CASE:
        O(log(N) + M log(N) + K), where log(N) is the complexity of LargestPrimeIterator (see primes.py), M log(N) 
        is the complexity of the while loop used to find a prime number that is closest to the tablesize, and K
        is the length of the key.
        """
        value = 0
        closest_val = self.tablesize + 1
        prime = LargestPrimeIterator(closest_val, 2)
        b = next(prime)
        while b < self.tablesize:
            closest_val += 1
            prime = LargestPrimeIterator(closest_val, 2)
            b = next(prime)
        a = next(prime)
        a = next(prime)
        for char in key:
            value = (ord(char) + a*value) % self.tablesize
            a = a * b % (self.tablesize-1)

        return value

    def statistics(self) -> tuple:
        """
            PARAMETERS:
            the instances of the LinearProbeTable class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            returns a tuple that contains statistical details relating to the number of conflicts encountered,
            the total distance probed throughout the code's execution, the longest probe chain that was measured, 
            as well as the total number of times the LinearProbeTable has to be rehashed.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [tuple]: a tuple containing the total number of conflicts, the total length probed, the longest probe
            chain and the number of times the LinearProbeTable is rehashed.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only returns values assigned to variables.
        """
        return (self.conflict_count, self.probe_total, self.probe_max, self.rehash_count)

    def __len__(self) -> int:
        """
            Returns number of elements in the hash table
            :complexity: O(1)
        """
        """
            PARAMETERS:
            the instances of the LinearProbeTable class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            a magic method that returns the number of items currently in the LinearProbeTable
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            count[integer]: the number of items in the LinearProbeTable
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only returns values assigned to variables.
        """
        return self.count

    def _linear_probe(self, key: str, is_insert: bool) -> int:
        """
            PARAMETERS:
            the instances of LinearProbeTable class
            key[string]: the key to be hashed into the hashtable
            is_insert[boolean]: boolean statement as to whether the linear_probe will be used for the insertion
            method, or otherwise.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Finds the correct position for the key in the hash table using linear probing, and raises a key error
            if the position can't be found. The method checks if the position the key should be added into is empty,
            and if not either overwrites the current item in it, or checks if the next position is empty.
            instance variables conflicts and probes are added into the method to help keep track of necessary
            statistics, and the stat_update method is used to change these statistics.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            position[integer]: the index in the LinearProbeTable that the linear probe has found. will be used
            to either insert or retrieve and item.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(K + U), where the first position is empty and K is the length of the key, and U is the complexity
            of the stat_update method (see stat_update).

            COMPLEXITY FOR WORST CASE:
            O(K + N + U), where K is the size of the key and N is the tablesize, and we search the entire table,
            i.e. we iterate through every index of the table, and U is the complexity of the stat_update method 
            (see stat_update).
        """
        position = self.hash(key)  # get the position using hash
        conflicts = 0
        probes = 0

        if is_insert and self.is_full():
            raise KeyError(key)

        for _ in range(len(self.table)):  # start traversing
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    self.stat_update(conflicts, probes)
                    return position
                else:
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                self.stat_update(conflicts, probes)
                return position
            else:  # there is something but not the key, try next
                position = (position + 1) % len(self.table)
                conflicts = 1
                probes += 1
            
        # self.conflict_count += conflicts
        # if probes > self.probe_max: # changes probe_max if a longer probe chain was found
        #     self.probe_max = probes
        # self.probe_total += probes  # tracks the additional probes
        raise KeyError(key)

    def stat_update(self, conflicts: int, probes: int) -> None:
        """
            PARAMETERS:
            the instances of the LinearProbeTable class
            conflicts[integer]: whether there was a conflict during the linear probe, 0 if no, 1 if yes
            probes[integer]: the length of the probe chain that occured during the linear probe.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            updates the class's total conflict count, total length probed, and longest probe chain 
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: the method only updates the values in the class, and returns no items.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(comp), where comp is the complexity of the comparison between probes and probe_max.
        """
        self.conflict_count += conflicts
        if probes > self.probe_max:
            self.probe_max = probes
        self.probe_total += probes

    def keys(self) -> list[str]:
        """
            Returns all keys in the hash table.
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][0])
        return res

    def values(self) -> list[T]:
        """
            Returns all values in the hash table.
        """
        res = []
        for x in range(len(self.table)):
            if self.table[x] is not None:
                res.append(self.table[x][1])
        return res

    def __contains__(self, key: str) -> bool:
        """
            Checks to see if the given key is in the Hash Table
            :see: #self.__getitem__(self, key: str)
        """

        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
            Get the item at a certain key
            :see: #self._linear_probe(key: str, is_insert: bool)
            :raises KeyError: when the item doesn't exist
        """

        position = self._linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
            Set an (key, data) pair in our hash table
            :see: #self._linear_probe(key: str, is_insert: bool)
            :see: #self.__contains__(key: str)
        """
        """
            PARAMETERS:
            the instances of LinearProbeTable class
            key[string]: the key of the item (data) that we're using to store in the LinearProbeTable
            data[T]: the item that will be stored in the LinearProbeTable at an index obtained using key.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            a magic method that allows us to set an item (key, data) at a certain index
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: the method only updates the values in the class, and returns no items.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(N + comp), where N is the best case time complexity of _linear_probe (see _linear_probe), and comp
            is the complexity of the comparisons.

            COMPLEXITY FOR WORST CASE:
            O(N + M + comp), where N is the worst case time complexity of _linear_probe (see _linear_probe), M is
            the worst case time complexity of _rehash (see _rehash), and comp complexity of the comparisons.
        """
        if self.count > self.tablesize // 2:
            self._rehash()

        position = self._linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1

        self.table[position] = (key, data)

    def is_empty(self):
        """
            Returns whether the hash table is empty
            :complexity: O(1)
        """

        return self.count == 0

    def is_full(self):
        """
            Returns whether the hash table is full
            :complexity: O(1)
        """

        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
            Utility method to call our setitem method
            :see: #__setitem__(self, key: str, data: T)
        """

        self[key] = data

    def _rehash(self) -> None:
        """
            Need to resize table and reinsert all values
        """
        """
            PARAMETERS:
            the instances of the LinearProbeTable class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            resizes the LinearProbeTable as well as reinserts the existing values back in
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [NONE]: the method only updates the values in the class, and returns no items.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(length), where length is the number of items that are in the LinearProbeTable. Best and Worst case
            are the same as the method is only called when an item is about to be inserted and the number of items
            exceeds half of its capacity, and therefore will not be called when there are no items in the table,
            (which would give the best case complexity as O(1)).
        """
        # if no. of items stored there exceeds half of its capacity
        old_table = self.table
        self.tablesize *= 2
        self.table = ArrayR(self.tablesize)
        self.count = 0
        for item in old_table:
            if item is not None:
                self[item[0]] = item[1]
        self.rehash_count += 1

    def __str__(self) -> str:
        """
            Returns all they key/value pairs in our hash table (no particular
            order).
            :complexity: O(N) where N is the table size
        """
        """
            PARAMETERS:
            the instances of the LinearProbeTable class
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            a magic method that produces a string representation of the LinearProbeTable
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            result[string]: returns a string containing all the key value pairs stored in the LinearProbeTable.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(1), where the LinearProbeTable is empty

            COMPLEXITY FOR WORST CASE:
            O(N), where N is the number of items stored in the LinearProbeTable.
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result

if __name__ == "__main__":
    table = LinearProbeTable(10, 19)
    table["12"] = 1
    print(table)
    
