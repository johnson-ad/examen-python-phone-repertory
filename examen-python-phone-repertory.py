tabContact = [{"nom":"Fall","numero":771231122},
{"nom":"Master","numero":772541743},
{"nom":"Lol","numero":709871523},
{"nom":"King","numero":3300023123},
{"nom":"Moudou","numero":784444443},
{"nom":"Vague","numero":781311112},
{"nom":"Paul","numero":7000001123}]

 


def infoPhone(**elem):
    rep = "1-Afficher le repertoire"
    rech = "2-Rechercher contact"
    add = "3-Ajouter contact"
    upContact = "4-Modifier contact"
    delContact = "5-Supprimer contact"
    quiter = "6-Quiter"
    print("\n",rep,"\n",rech,"\n",add,"\n",upContact,"\n",delContact,"\n",quiter)

def afficher(rep=""):
    print("*" * 100)
    print("Liste des contacts")
    for i, nom  in enumerate(tabContact):
        print(i, nom)
    print("*" * 100)


def ajouterContact(addName="" , addPhoneNumber=""):
    print("Ajouter un nouveau Contact")
    addName = input("Entrer Le nom : ")
    addPhoneNumber = int(input("Entrer le Numero : "))
    ajouter = "o"
    while ajouter == "o":
        dicAjt = {"nom": addName,"numero": addPhoneNumber}
        tabContact.insert(0, dicAjt)
        print("*" * 100)
        ajouter = input("Voulez-vous vraiment ajouter ce Numero ? o/n ")
        for i, nom  in enumerate(tabContact):
            print(i, nom )
        print("*" * 100, "\n")
          
        ajouter = input("Voulez-vous ajouter un autre contact ? o/n \n")
        addName = input("Entrer Le nom : ")
        addPhoneNumber = int(input("Entrer le Numero : "))
        i = int()
        if (addPhoneNumber < 7 and addName != i ):         
            print("Vieullez entre un bon Numero \nEx: 77 xxx xx xx")
        else:
            dicAjt = {"nom": addName,"numero": addPhoneNumber}
            tabContact.insert(0, dicAjt)
            for i, nom  in enumerate(tabContact):
                print(i, nom)
            print("*" * 100, "\n")
        if ajouter != "a":
            break


def recherche(cont=""):
    afficher()
    inputID = int(input("Entrer l'ID de votre contact a rechercher : "))
    for i in tabContact:
        if i == tabContact[inputID]:
            print(tabContact[inputID]["nom"],": ", tabContact[inputID]["numero"])
            break
    else:
       print("Pas de contact a ce ID : " + str(inputID))


def delCont(delc=""):
    afficher()
    inputID = int(input("Entrer l'ID de votre contact a supprimer : "))
    for i in tabContact:
        if i == tabContact[inputID]:
            res = "o"
            while res == "o":
                res = input("Voulez-vous continiuez ?  o/n ")
                if res == "o":
                    del tabContact[inputID]
                    print(tabContact[inputID]["nom"],":", tabContact[inputID]["numero"], " a ete bien supprimer")
                    for i, nom  in enumerate(tabContact):
                        print(i, nom)
                    break
                elif res == "n":
                    print("annulation de la suppresion")
                    break



def modif(mo=""):
    afficher()
    req = "o"
    while req == "o":
        res = input("Voulez-vous modifier un contact ?  o/n ")
        if res == "o":
            inputID = int(input("Entrer L'ID de ce contact : "))
            inputName = input("Entrer le nouveau nom du contact : ")
            inputNumber = int(input("Entrer son nouveau numerau : "))
            tabContact[inputID]["nom"]= inputName
            tabContact[inputID]["numero"]= inputNumber
            print("Nouveau contact ajouter :",tabContact[inputID]["nom"],":", tabContact[inputID]["numero"])
            tabContact
            for i, nom  in enumerate(tabContact):
                print(i, nom)
            print("*" * 100, "\n")
            break
        elif res == "n":
            print("annulation de la modification")
            print("*" * 100, "\n")
            break


def quiter(end=""):
    print("*" * 100)
    end = "o"
    while end == "o":
        end = input("Voulez-vous vraiment quiter ? o/n \n")
        if(end == "o"):
            print("A bientot")
            break
        elif end =="n":
            repertoire()
    print("*" * 100)


rinit = 0
rep=1
rech=2 
add=3 
upContact=4 
delContact=5 
quiterRep=6


respon = ""
def repertoire(respon=""):
    if respon == "":
        infoPhone()
        while respon == "":
            respon = int(input("==>"))
            if respon == rep:
                afficher()
                break
            elif respon == rech:
                recherche()
                break
            elif respon == add:
                ajouterContact()
                break
            elif respon == upContact:
                modif()
                break
            elif respon == delContact:
                delCont()
                break
            elif respon == quiterRep:
                quiter()
                break
            else:
                print("Repondez aux questions !")


repertoire()