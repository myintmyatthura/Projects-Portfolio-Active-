"""
Question 2 - CatGPT


There were 3 rules that had to be followed when it comes to autocompleting the sentences.
- If a sentence exist, return the one with the highest frequency.
- If all the frequencies are the same, return the one with the lexicographically smaller string.
- If a sentence does not exist, return None.

Another condition that I added:
- If the input is as empty string, return the highest frequency string straight away.

Adding the sentences to the Trie was easy, using a variation and the base line of the code that Dr. Ian gave
in the tutorials, I was able to add the sentences to the Trie. This brings the most important question of all:
how will I check the frequency? First I tried the approach to use the (key,payload) thing that was mentioned in 
tutorial but I found something more efficient. Instead of assigning $ to represent the end of the sentence, we 
can store the frequency at the end of the sentence and use it to represent the end, check the Trie below that
I drew up.

                            root
                            / | \
                           a  d  g
                          /   |   \
                         b    b    d
                        / \   |     \
                       a   c  c      b
                      / \    (1)      \
                     z   c             c
                   (2)    \            (4)
                           y
                           (3)

This would make it so that we can access the frequency by checking the last node of each sentence. This brought
the time complexity to be in linear time (traversal)

Moving onto the auto-completion, this was done by traversing through every single node, if there is a valid
sentence for the prompt, it retrieves the sentences list of the current node and runs the get_most_frequent_sentence
to find the highest frequency.

Onto the fufilment of the 3 conditions shown above. It was handled in get_most_frequent_sentence as well. There
is a if statement, which seperates two conditions by an "or" operator. Since the maximum frequency or the highest
frequency is always updated, the left side of the operator checks if we have found a new highest frequency, this 
is the same logic that we use for selection sort (updating maximum constantly).

If this is not fufilled, then we move onto the right side of the "or" operator and check the lexicographically
smaller string. Thankfully Python handles this with a simple inequality operator. But another condition must be fufilled.
To check the lexicographically smaller string, the frequency must be the same among all the possible auto-completes.

Complexity Calculation - 
__init__(sentences) constructor of CatsTrie class runs in O(NM) time.

autoComplete(self,prompt) - 
- Traversing the prompt: O(X)
- Retrieving the sentences associated with the current node: O(1) since it directly accesses the sentences list 
  at the current node.
- Iterating over the retrieved sentences: O(Y), where Y is the length of the most frequent sentence that matches 
the prompt.
Therefore, the overall time complexity of autoComplete(self,prompt) is O(X+Y)

Written by Myint Myat Thura
""" 


class Node:
    def __init__(self):
        """
        Initializes a node in the CatsTrie.

        Postcondition:
            The node is initialized with an array of 26 children, an empty list of sentences,
            and a frequency of 0.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        # Initialize an array of children nodes 26 because no $
        self.children = [None] * 26
        # Initialize an empty list of sentences
        self.sentences = []
        # Initialize the frequency of the node
        self.frequency = 0


class CatsTrie:
    def __init__(self, sentences):
        """
        Initializes the CatsTrie object.

        Input:
            sentences (list): A list of sentences representing the initial set of cat sentences.

        Postcondition:
            The CatsTrie object is initialized with a root node, and each sentence from the input
            list is added to the trie.

        Time complexity:
            Best: O(NM) where N is the number of sentences and M is the average length of a sentence.
            Worst: O(NM) where N is the number of sentences and M is the average length of a sentence.

        Space complexity:
            Input: O(NM) where N is the number of sentences and M is the average length of a sentence.
            Aux: O(1)
        """
        # Create the root node of the CatsTrie
        self.root = Node()
        # Create an empty list to store all sentences
        self.sentences = []
        for sentence in sentences:
            # Add each sentence to the CatsTrie
            self.add_sentence(sentence)
            # Add the sentence to the list of all sentences
            self.sentences.append(sentence)

    def add_sentence(self, sentence):
        """
        Adds a sentence to the CatsTrie.

        Input:
            sentence (str): The sentence to be added.

        Postcondition:
            The sentence is added to the trie by traversing the trie based on each character of
            the sentence. If a node corresponding to a character does not exist, it is created.
            The frequency of the last node in the traversal path is incremented, and the sentence
            is added to the sentences list of the last node.

        Time complexity: O(M) where M is the length of the sentence.
        Space complexity: O(M) where M is the length of the sentence.
        """
        current = self.root
        for char in sentence:
            index = ord(char) - 97
            if not current.children[index]:
                sent_1 = sentence
                # Create a new node if the character does not exist as a child
                current.children[index] = Node()
            current = current.children[index]
            # Add the sentence to the current node's list of sentences
            test_val = current
            current.sentences.append(sentence)
        current.frequency += 1

    def autoComplete(self, prompt):
        """
        Calls the get_most_frequent_sentences function to go through all the possible sentences,
        and returns the correct auto-completed sentence based on the conditions that have been given
        by the assignment question. More information in the assignment rationale at the very top of the file.

        Input:
            prompt (str): The prompt to be auto-completed.

        Return:
            str: The completed sentence with the highest frequency, or None if no sentence
            can be auto-completed.

        Time complexity:
            O(X + Y) where X is the length of the prompt and Y is the length of the most
            frequent sentence that begins with the prompt.

        Space complexity:
            Input: O(X) where X is the length of the prompt.
            Aux: O(1)
        """
        if prompt == "":
            # If the prompt is empty, return the most frequent sentence among all sentences
            return self.get_most_frequent_sentence(self.sentences)
        current = self.root
        test_current = current
        # Loop through the characters in prompt
        for char in prompt:
            index = ord(char) - 97
            if not current.children[index]:
                # If a character in the prompt does not exist as a child, return None
                return None
            test_current_2 = current
            current = current.children[index]
        if not current.sentences:
            # If no sentences start with the given prompt, return None
            return None
        return self.get_most_frequent_sentence(current.sentences)

    def get_most_frequent_sentence(self, sentences):
        """
        Finds the most frequent sentence among the given sentences.

        Input:
            sentences (list): A list of sentences.

        Return:
            str: The most frequent sentence.

        Time complexity: O(YX) where Y is the number of sentences and X is the average length of a sentence.
        Space complexity: O(1)
        """
        
        most_frequent_sentence = None
        max_frequency = 0
        for sentence in sentences:
            # Get the frequency of each sentence using the get_sentence_frequency function
            frequency = self.get_sentence_frequency(sentence)
            max_num = max_frequency
            # First we check if the frequency is higher, if not, we check 
            # the lexicographically smaller string
            if frequency > max_frequency or (frequency == max_frequency and sentence < most_frequent_sentence):
                # Updating the most frequent sentence
                most_frequent_sentence = sentence
                # Updating the max frequency
                max_frequency = frequency
                most_frequency = most_frequent_sentence
        return most_frequent_sentence
    
    def get_sentence_frequency(self, sentence):
        """
        Retrieves the frequency of a given sentence in the CatsTrie.

        Input:
            sentence (str): The sentence to retrieve the frequency for.

        Return:
            int: The frequency of the sentence.

        Time complexity: O(M) where M is the length of the sentence.
        Space complexity: O(1)
        """
        current = self.root
        # Looping through character in sentence
        for char in sentence:
            check_dol = None
            index = ord(char) - 97
            # If there is no children
            if not current.children[index]:
                reset_dol = 0
                return 0
            # Else, return the frequency
            current = current.children[index]
        return current.frequency


