def load_file_content(file_name):  #in aceasta functie preluam datele din fisier fara comentarii
    try:
        with open(file_name, 'r') as file:
            lines=file.readlines()
            lines=[line for line in lines if line.strip().startswith("#")==False ]
            return "".join(lines)

    except FileNotFoundError as e:
        return f"File '{file_name}' not found"

def create_section_list(content):   #cream lista cu sectiuni care va contine sectiunile fisierului
    array=[]
    lines=content.split("\n")       #facem un array cu fiecare rand din template
    for line in lines:
        if line.startswith("[") and line.split("#")[0].strip().endswith("]"):   #acolo unde gasim [*] continuat de # preluam doar textul dintre []
            array.append(line.split("]")[0].strip().strip("[]"))   
              
    return array
def get_section_content(name,content):  #pentru fiecare sectiune pastram randurile de instructiuni fara instructiuni
    
    if name in content:         #daca gasim numele sectiunii cautate in fisier
        lines=content.split("\n")   #impartim textul pe randuri
        
        start=end=len(lines)

        for i in range(len(lines)):
            if "["+name+"]" in lines[i]:    #daca gasim sectiuinea in fisier
                start=i #am gasit startul
            if lines[i].strip().startswith("[") and lines[i].split("#")[0].strip().endswith("]") and i>start:   #daca gasim o alta sectiune ne oprim si pastram finalul
                end=i
                break
        return lines[start+1:end]   #returnam din lista de randuri doar randurile de din sectiune
        
    else:
        return f"Section '{name}' not found"    #daca nu gasim afisam un mesaj





