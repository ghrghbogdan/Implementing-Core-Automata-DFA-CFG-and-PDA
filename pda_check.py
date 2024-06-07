import File_loader
load_file_content=File_loader.load_file_content
create_section_list=File_loader.create_section_list
get_section_content=File_loader.get_section_content
content= load_file_content("pda_template.txt")
list=create_section_list(content)

Sigma=get_section_content(list[0],content)
Gamma=get_section_content(list[1],content)
Gamma.append('')
States=get_section_content(list[2],content)
Delta=get_section_content(list[3],content)
Start=get_section_content(list[4],content)
Final=get_section_content(list[5],content)
#incarcam elementele necesare

def pda_check(content,list):
    if len(list)<6:
        print("Section missing")
        return 0
    if len(list)>6:
        print("Section not required")       #verificam daca avem 6 sectiuni
        return 0
    if len(Start)>1:
        print("Multiple start states")      #verificam daca avem un singur start
        return 0
    if len(Start)==0:
        print("No start state")             #verificam daca avem start
        return 0
    if len(Final)==0:
        print("No final states")        #verificam daca avem stare de final
        return 0
    for element in Delta:
        if element.split(",")[0] not in States:
            print("State from Delta not in States")         #verificam daca primul element din delta e in states
            return 0
        if element.split(",")[1] not in Sigma and element.split(",")[1]!="$":       #verificam daca al doilea element din delta e in gamma
            print("Symbol from Delta not in Gamma")
            return 0
        if element.split(",")[2] not in Gamma and element.split(",")[2] != "$":         #verificam daca al treilea element din delta e in states sau gamma
            print("Symbol/state from Delta not in Gamma or States")
            return 0
        if element.split(",")[3] not in States and element.split(",")[3] != "$":            #verificam daca al patrulea element din delta e in states
            print("State from Delta not in States")
            return 0
        for litera in element.split(",")[4]:
            if litera not in Gamma and litera != "$" :                  
                print("Symbol/state from Delta not in Gamma or States")                 #verificam daca al cincilea element din delta e in states sau gamma
                return 0

    return 1
def emulate_pda():
    print("Enter the input string")             #dam stringul e input
    string_input=input()
    string_input="$"+string_input+"$"           #apenduim la inceput si la final epsilon pentru buna functionare a pda-ului
    index=0                                     #setam indexul curent 0
    stack="!"                                   #setam baza stivei !
    current_state=Start[0]                      #setam starea curenta start
    while index<len(string_input):              #cat timp nu ajungem la finalul inputului
        found=False
        

# in acest for rezolvam toate problemele in ceeea ce priveste interpretarea delta
# interpretam toate actiunile pentru locul in care se afla epsilon sau baza stivei
# codul devine putin repetitiv dar in mare stim urmatoarele aspecte:
# daca gasim epsilon in stiva inseamna ca nu ne intereseaza ce este acolo
# daca "punem" epsilon in stiva inseamna ca stergem elementul din varful stivei
# daca punem ! la baza stivei inseamna ca trecem de la prima stare la a doua
#daca gasim  ! la baza stivei inseamna ca trecem la ultima stare din pda

        for element in Delta:                  
            tokens=element.split(",")           
            if tokens[0]==current_state:        
                if tokens[1]==string_input[index] or tokens[1]=="$":
                    if tokens[2]=="$":
                        if tokens[4]=="$":
                            stack=stack[1:]
                            current_state=tokens[3]
                            found=True
                            index+=1
                            break
                        if tokens[4]=="!":
                            current_state=tokens[3]
                            found=True
                            
                            index+=1
                            break
                        stack=tokens[4]+stack
                        current_state=tokens[3]
                        found=True
                        index+=1
                        break
                    if tokens[2]=="!":
                        if tokens[4]=="$":
                            stack=stack[1:]
                            current_state=tokens[3]
                            found=True
                            index+=1
                            break
                        if tokens[4]=="!":
                            found=True
                            index+=1
                            break
                        stack=tokens[4]+stack
                        found=True
                        index+=1
                        break
                    if tokens[2]==stack[0]:
                        if tokens[4]=="$":
                            stack=stack[1:]
                            current_state=tokens[3]
                            found=True
                            index+=1
                            break
                        if tokens[4]=="!":
                            current_state=tokens[3]
                            found=True
                            index+=1
                            break
                        stack=tokens[4]+stack
                        current_state=tokens[3]
                        found=True
                        index+=1
                        break
        
    
        if found==False:            #daca nu gasim o regula care sa se potriveasca cu contextul inseamna ca inputul e gresit
            print("Input string rejected")
            return
    if current_state==Final[0]:         #daca am ajuns in starea e final inseamna ca inputul a fost acceptat
        print("String accepted")
    return





if pda_check(content,list)==1:
    print("PDA is correct")
    emulate_pda()
else:
    print("PDA is incorrect")
    print("Please correct the PDA")

