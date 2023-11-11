def count_words(file):
    word_count = {}
    
    try:
        with open(file) as f:
            words = f.read().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        # Previous is better version of this commented code
        # for word in words:
        #     if word in word_count:
        #         word_count[word] += 1
        #     else:
        #         word_count[word] = 1
    except FileNotFoundError:
        print(f"Error: File {file} was not found")
        return
    except IOError:
        print(f"Error: an IO error occured with reading {file}")
        return


    print(word_count)
    
count_words(r'C:\Users\awojo\OneDrive\Documents\dev\Python-basics\testfile.txt')