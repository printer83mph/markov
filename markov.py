
import random

def single(word,word_list):
    output = []
    for i in range(0,len(word_list)-1):
        if word_list[i] == word:
            if(word_list[i+1] != "-:-"):
                output.append(word_list[i+1])
    if output != []:
        return output
    else: return random.choice(word_list)

def double(word1,word2,word_list):
    if(len(word_list) > 1):
        output = []
        for i in range(0,len(word_list)-1):
            if(word_list[i] == word1 and word_list[i+1] == word2):
                if(word_list[i+2] != "-:-"):
                    output.append(word_list[i+2])
        if output != []:
            return output
        else: return single(word2,word_list)
    else: return single(word2,word_list)

def make_chain(word_list,word_count):
    output = [random.choice(word_list)]
    for i in range(0,word_count):
        output.append(random.choice(single(output[-1],word_list)))
    return output

def make_chain(word_list,sentence_count,choice):
    output = []
    start_words = []
    for g in range(0,len(word_list)-1):
        if(word_list[g] == "-:-" and word_list[g+1][0].isupper()):
            start_words.append(word_list[g+1])
    for i in range(0,sentence_count):
        current_sentence = [random.choice(start_words)]
        if(single(current_sentence[-1],word_list) != []):
            current_sentence.append(random.choice(single(current_sentence[-1],word_list)))
        else: current_sentence.append(random.choice(word_list))
        while(current_sentence[-1][-1] not in (".","!","?")):
            if(choice):
                if(double(current_sentence[-2],current_sentence[-1],word_list) != []):
                    current_sentence.append(random.choice(double(current_sentence[-2],current_sentence[-1],word_list)))
                else: current_sentence.append(random.choice(word_list))
            else:
                if(single(current_sentence[-1],word_list) != []):
                    current_sentence.append(random.choice(single(current_sentence[-1],word_list)))
                else: current_sentence.append(random.choice(word_list))
        output += current_sentence + ["\n"]
    return output

def convert(words):
    output = []
    for i in range(0,len(words)-1):
        if(words[i][-1] == "." or words[i][-1] == "!" or words[i][-1] == "?"):
            words.insert(i+1,"-:-")

def main():
    file = open("base_text.txt","r")
    test_list = file.read().split()
    convert(test_list)
    choice = True if raw_input("Double? y/N > ") in ("y","Y") else False
    output = open("output.txt","w")
    output.write(" ".join(make_chain(test_list,50,choice)))
    print("Done!")

if __name__ == '__main__':
    main()
