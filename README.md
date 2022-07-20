# sensitive-word-detector 敏感词检测器
A simple sensitive word detector based on trie, implemented in python.\
一个简易的python敏感词检测器，基于trie树(DFA算法)。

---

## How to run 如何使用
1. Copy the text which needs to be censored into text.txt.\
把需要检测的文本复制进text.txt。

2. Copy the key words (sensitive words) into keywords.txt, one word per line. for the  format, see sample_banned_words.txt under sample_files.\
把关键词(敏感词)复制进keywords.txt，一行一词，格式请见sample files里的sample_banned_words.txt。

3. Copy the characters to be ignored into ignored_chars.txt, one character per line. for the format, see sample_ignored_chars.txt under sample_files.\
把需要忽略的字符复制进ignored_chars.txt，一行一个字符，格式请见sample_files里的sample_ignored_chars.txt。

4. Click censor.exe to run the program, and view the results in the pop-up command line interface.\
点击censor.exe运行程序，在弹出的命令行里查看检测结果。

## Tips 小提示
1. Don't change the names and the paths of the txt files, otherwise the program can't run normally.\
不要改变txt文件的名字和路径，不然程序会无法正常运行。

2. If you don't need to ignore characters, just leave ignored_chars.txt blank without deleting the file.\
如果不需要忽略字符，将ignored_chars.txt留空即可，不用删除文件。
