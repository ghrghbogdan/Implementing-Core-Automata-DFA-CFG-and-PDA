import File_loader
import random
load_file_content=File_loader.load_file_content
create_section_list=File_loader.create_section_list
get_section_content=File_loader.get_section_content
content= load_file_content("cfg_template.txt")
list=create_section_list(content)

Var=get_section_content(list[0],content)
Terminals=get_section_content(list[1],content)
Start=get_section_content(list[2],content)
Rules=get_section_content(list[3],content)

#incarcam resursele necesare din fisier
def cfg_check(content,list):
    if len(list)<4:
        print("Section missing")
        return 0
    if len(list)>4:
        
        print("Section not required")
        return 0        #verificam daca fisierul are 4 sectiuni + mesaje personalizate
    if len(Start)>1:
        print("Multiple start symbols")
        return 0        #sectiunea start trebuie sa aiba un singur simbol de start
    if Start[0] not in Var:
            print("Start symbol not in Var")        #verificam daca simbolul de start este variabila
            return 0
    for element in Rules:
        if element.split("->")[0] not in Var:       #verificam daca primul element din regula este variabila
            print("LHS not in Var")
            return 0
        rule=element.split("->")[1]
       
        for i in rule.split(","):       #verificam daca restul elementelor din regula sunt variabile sau terminali
           
            if i not in Var and i not in Terminals:
                print(f"{i} not in Var or Terminals")
                return 0
    return 1

def emulate_cfg():
    
    import random
    start=Start[0]      #folosim libraria random pentru generare, setam startul, si o punem in output
    output=start
   

    found=True
    while found:
        found=False #presupunem ca nu gasim o regula pentru inputul nostru
        

        contor=0
        for element in Rules:
            if element.split("->")[0]==start:  #verificam daca regula este potrivita pentru elementul curent
                contor+=1   #vedem cate reguli se potrivesc
        random_rule=random.randint(1,contor)    #random unei reguli potrivite

        for element in Rules:
            if element.split("->")[0]==start:               
                random_rule-=1  #ne asiguram ca alegem regula potrivita
                if random_rule==0:      #atunci cand o gasim
                    rule=element.split("->")[1]     #stocam in rule regula
                    break
        output=output.replace(start,rule,1)         #apoi inlocuim variabila cu regula
        
        for i in output.split(","): 
            
            if i in Var:        
                start=i 
                found=True      #validam faptul ca am gasit o regula potrivita      
                break
        if found==False:        #daca nu am gasit dam break
            break       
        
    


    output=output.replace(",","")           #scoatem virgulele din output
    output=output.replace("$","")           #scoatem epsilon din output
    
    return output


if cfg_check(content,list):
    print("Cfg is valid")
    print(emulate_cfg())
else:
    print("Cfg is invalid")
