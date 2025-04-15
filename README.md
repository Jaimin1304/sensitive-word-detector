# Sensitive Word Detector

A simple yet powerful sensitive word detector based on a Trie tree (DFA algorithm), implemented in Python.

## ✨ Features

- **Efficient Detection**: Quickly identifies sensitive words in text using an optimized Trie tree structure
- **Customizable**: Supports user-defined sensitive words and characters to ignore
- **Flexible**: Ignores specified characters (e.g., punctuation) during detection
- **Easy to Use**: Minimal setup required with simple text file configuration

## 🚀 How to Use

### Step 1: Prepare Input Files

1. **Text to Detect**:  
   Copy the text you want to check into text.txt.

2. **Sensitive Words**:  
   Add sensitive words to keywords.txt, one word per line.  
   _(See examples in sample_banned_words.txt)_

3. **Ignored Characters**:  
   Add characters to ignore during detection to ignored_chars.txt, one character per line.  
   _(See examples in sample_ignored_chars.txt)_

   > **Note**: If you don't need to ignore any characters, leave ignored_chars.txt blank.

### Step 2: Run the Program

Execute the program by running:
```bash
python censor.py
```

Or double-click censor.exe if you have the executable version.

### Step 3: View Results

The results will display in the command line, including:
- Whether the text passed the check (`passed`)
- Number of sensitive words detected (`banned_word_num`)
- List of detected sensitive words and their positions (`banned_words`)
- Execution time (`execution time(s)`)

## 📋 Example

### Input
- **text.txt**: `我是傻***逼`
- **keywords.txt**: `傻逼`
- **ignored_chars.txt**: `*`

### Output
```
----- program start -----
--- building tree ---
Trie construction time(s): 0.001
--- results ---
passed: False
banned_word_num: 1
banned_words: [['傻逼', 3]]
execution time(s): 0.002
----- program end -----
```

## 💡 Tips

- Keep input file names unchanged for proper functioning
- For large sensitive word lists, the program may take longer to execute
- Character encoding is UTF-8 for proper handling of various languages

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# 敏感词检测器

一个基于 Trie 树（DFA 算法）的简单而强大的敏感词检测器，使用 Python 实现。

## ✨ 功能特点

- **高效检测**: 使用优化的 Trie 树结构快速识别文本中的敏感词
- **可定制**: 支持用户自定义敏感词和需要忽略的字符
- **灵活性**: 在检测过程中忽略指定字符（如标点符号）
- **简单易用**: 仅需简单的文本文件配置，设置简便

## 🚀 如何使用

### 步骤 1: 准备输入文件

1. **待检测文本**:  
   将需要检测的文本复制到 text.txt 文件中。

2. **敏感词列表**:  
   将敏感词添加到 keywords.txt 文件中，每行一个词。  
   _(可参考 sample_banned_words.txt 示例)_

3. **忽略字符**:  
   将需要忽略的字符添加到 ignored_chars.txt 文件中，每行一个字符。  
   _(可参考 sample_ignored_chars.txt 示例)_

   > **提示**: 如果不需要忽略字符，可以将 ignored_chars.txt 留空。

### 步骤 2: 运行程序

执行程序:
```bash
python censor.py
```

或者如果有可执行版本，双击 censor.exe。

### 步骤 3: 查看结果

结果将在命令行中显示，包括：
- 文本是否通过检测（`passed`）
- 检测到的敏感词数量（`banned_word_num`）
- 敏感词及其位置列表（`banned_words`）
- 检测执行时间（`execution time(s)`）

## 📋 示例

### 输入
- **text.txt**: `我是傻***逼`
- **keywords.txt**: `傻逼`
- **ignored_chars.txt**: `*`

### 输出
```
----- program start -----
--- building tree ---
Trie construction time(s): 0.001
--- results ---
passed: False
banned_word_num: 1
banned_words: [['傻逼', 3]]
execution time(s): 0.002
----- program end -----
```

## 💡 小提示

- 保持输入文件名称不变，以确保程序正常运行
- 对于较大的敏感词列表，程序可能需要更长时间执行
- 文件编码采用 UTF-8，以正确处理各种语言

## 📄 许可证

本项目基于 MIT 许可证开源 - 详情请参阅 LICENSE 文件。