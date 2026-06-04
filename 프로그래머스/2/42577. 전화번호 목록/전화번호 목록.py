class Node(object):
    def __init__(self, key, data=None):
        self.key=key
        self.data=data
        self.children={}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            
            curr_node = curr_node.children[char]
        
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        if curr_node.data:
            return True
        else:
            return False
    
    def starts_with(self, string):
        curr_node = self.head
        words=[]
        for char in string:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        
        curr_node = [curr_node]
        next_node = []
        while True:
            for node in curr_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                curr_node = next_node
                next_node = []
            else:
                break
        return words

def solution(phone_book):
    answer = True
    
    trie = Trie()
    
    for p in phone_book:
        trie.insert(p)
    
    for p in phone_book:
        words = trie.starts_with(p)
        if len(words)>1:
            return False
        
    return answer