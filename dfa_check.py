import File_loader
load_file_content=File_loader.load_file_content
create_section_list=File_loader.create_section_list   
get_section_content=File_loader.get_section_content
content= load_file_content("file_name.txt")
list=create_section_list(content)
sigma=get_section_content(list[0],content)
states=get_section_content(list[1],content)
start_state=get_section_content(list[2],content)
final_states=get_section_content(list[3],content)
delta=get_section_content(list[4],content)
# in partea de sus sustragem sectiunile si toate elementele din fiecare sectiune care ne intereseaza
def dfa_check(content,list):
    if len(list)<5:
        print("Section missing")
        return 0
    if len(list)>5:
        print("Section not required")
        return 0    #verificam daca textul are toate sectiunile de care avem nevoie afisand un mesaj personalizat in caz contrar
    for section in list[:4]: #urmeaza sa verificam daca primele 3 sectiuni sunt corecte
        section_content=get_section_content(section,content)
        # print(section_content)
        for line in section_content:
            if len(line.split())!=1:    #daca fiecare rand contine mai mult de un element notam ca invalid
                print(f"Invalid line: {line}")  #si afisam un mesaj personalizat
                return 0
    section_content=get_section_content(list[4],content)
    # print(section_content)
    for line in section_content:    #pentru ultima linie
        if len(line.split(','))!=3:             #verificam daca are exact 3 elemente despartite prin virgula stare,input,stare
            print(f"Invalid line: {line}")
            return 0
        elements=line.split(',')        #pastram cele 3 elemente
        if elements[0] not in get_section_content(list[1],content) or elements[1] not in get_section_content(list[0],content) or elements[2] not in get_section_content(list[1],content):
            print("Invalid input")  #daca primul si al 3-lea element nu sunt in states , iar al 2-lea nu e in sigma
            return 0    #afisam invalid input
        return 1
    section_content=get_section_content(list[2],content)
    for elem in section_content:
        if elem not in get_section_content(list[1],content):    #daca nu gasim starea de start afisam invalid input
            print("Invalid input")
            return 0
    section_content=get_section_content(list[3],content)
    for elem in section_content:
        if elem not in get_section_content(list[1],content):    #daca nu gasim starea de final afisam invalid input
            print("Invalid input")
            return 0
def emulate():
    head=start_state[0]
    string=input("Enter the string: ")      #introducem stringul
    for i in range(len(string)):
        if string[i] not in sigma:          #daca elementele din string nu sunt in sigma dam invalid input
            print("Invalid input")
            return 0
        for line in delta:
            if line.split(',')[0]==head and line.split(',')[1]==string[i]:    #trecem de la o stare la alta
                head=line.split(',')[2]
                break
        if head in final_states and i==len(string)-1:       #daca ajungem in starea de final ne oprim
            print("String accepted")
            return 0
    print("String rejected")
    return 0





if(dfa_check(content,list)==0):
    raise SystemExit("DFA is incorrect")

emulate()




