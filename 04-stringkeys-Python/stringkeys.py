"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        self.table.append(atring)
        pass
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        if string in self.table:
            hash_val = calculate_hash_value(string)
            return hash_val
        return -1
        pass

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        ascii_let_1 = ord(string[0])
        ascii_let_2 = ord(string[1])

        hash_value = ascii_let_1 * 100 + ascii_let_2
        return hash_value
        pass
