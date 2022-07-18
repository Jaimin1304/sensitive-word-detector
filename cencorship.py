from time import time

class TrieTree:


    class TrieNode:

        def __init__(self, letter, is_end=False, parent=None) -> None:
            self.letter = letter
            self.child_dic = {}
            self.is_end = is_end
            self.parent = parent
        
        def print_tree(self) -> None:
            print("--------")
            print(f"{self.letter}|is_end: {self.is_end}|parent: {self.parent.letter if self.parent is not None else 'None'}")
            for key, value in self.child_dic.items():
                print(f"--{key}-> ({value.letter})")
            for key, value in self.child_dic.items():
                value.print_tree()


    def __init__(self) -> None:
        self.root = self.TrieNode("root")

    def construct_tree(self, filename) -> None:
        start_time = time()
        with open(filename, "r", encoding="utf-8") as f:
            word_lst = f.readlines()
            for i in range(len(word_lst)):
                word_lst[i] = word_lst[i][:-1]
        for i in word_lst:
            node_ptr = self.root
            for index, j in enumerate(i):
                # skip the existing end
                if node_ptr.is_end:
                    continue
                # insert new letter to the tree and keep going
                if j not in node_ptr.child_dic:
                    node_ptr.child_dic[j] = self.TrieNode(j, False, node_ptr)
                node_ptr = node_ptr.child_dic[j]
                # insert end flag
                if index == len(i) - 1:
                    node_ptr.is_end = True
        end_time = time()
        print(f"construction time: {end_time - start_time}")

    def censor(self, text, ignore_lst=[]) -> dict:
        start_time = time()
        text = text.lower()
        result = {"passed": True, "banned_word_num": 0, "banned_words": [], "execution time": 0}

        head_ptr = 0
        for index, i in enumerate(text):
            if index < head_ptr:
                continue
            head_ptr = index
            letter_ptr = index
            node_ptr = self.root
            curr_word = ""
            while True:
                if letter_ptr >= len(text):
                    break
                if node_ptr.is_end:
                    result["passed"] = False
                    result["banned_word_num"] += 1
                    result["banned_words"].append([curr_word, index+1])
                    #print("letter ptr: " + str(letter_ptr) + " " + text[letter_ptr])
                    head_ptr = letter_ptr
                    break
                if text[letter_ptr] in node_ptr.child_dic:
                    curr_word += text[letter_ptr]
                    node_ptr = node_ptr.child_dic[text[letter_ptr]]
                    letter_ptr += 1
                else:
                    break
        end_time = time()
        result["execution time"] = end_time - start_time
        return result


if __name__ == "__main__":
    print("---start---")
    tree = TrieTree()
    tree.construct_tree("sample_banned_words.txt")
    #tree.root.print_tree()
    print("---")
    print(tree.censor("我妈逼我回家吃饭"))
