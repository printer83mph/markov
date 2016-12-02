
import random

def get_starters(start_word,word_list):
    output = []
    for i in range(0,len(word_list)):
        if word_list[i] == start_word:
            output.append(word_list[i+1])
    return output

def get_list(start_word,word_list,enders):
    output = []
    for i in range(0,len(word_list)):
        if word_list[i] == start_word:
            p = i + 1
            while word_list[p-1] not in enders and p < len(word_list):
                output.append(word_list[p])
                p += 1
    return output

def single(word,word_list):
    output = []
    for i in range(0,len(word_list)):
        if word_list[i] == word:
            output.append(word_list[i+1])
    return output

def main():
    debate = open("debate.txt","r").read().split()
    people = {"trump":"Trump:", "clinton":"Clinton:", "wallace":"Wallace:"}
    starters = {}
    for person in people:
        starters[person] = get_starters(people[person],debate)

    lists = {}
    for person in people:
        enders = []
        for p in people:
            if p != person: enders.append(people[p])
        lists[person] = get_list(people[person],debate,enders)

    new_debate = []
    person = "wallace"
    new_debate.append(people[person])
    while new_debate[-1] != "-:-":
        new_debate.append(random.choice(single(new_debate[-1],lists[person])))
        for p in people:
            if new_debate[-1] == people[p]:
                person = p
                new_debate.append(random.choice(starters[person]))
    for w in range(0,len(new_debate)):
        for p in people:
            if new_debate[w] == people[p]:
                print("did it")
                new_debate[w] = "\n \n" + new_debate[w]
    output = open("debate_output.txt","w")
    output.write(" ".join(new_debate))

if __name__ == '__main__':
    main()
