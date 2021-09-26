from binarysearch import binary_search

def read_words(file_path):
    with open(file_path, encoding='utf-8') as file:
              return file.read().splitlines()

def main():
    finnish_words = read_words('kotus-sanalista-v1/kotus-sanalista-suomi.txt')
    english_words = read_words('/usr/share/dict/words')

    finnish_words.sort()
    english_words.sort()

    intersection = set(finnish_words) & set(english_words)
    
    for word in intersection:
        print(word)

if __name__ == '__main__':
              main()
        
