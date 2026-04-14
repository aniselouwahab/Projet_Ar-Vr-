import sys

def lancer_jeu():
    questions = [
        # Niveau 1
        {"q": "Quel périphérique utilise-t-on pour taper du texte ?", "o": ["A) Souris", "B) Clavier", "C) Ecran"], "r": "B"},
        {"q": "Que signifie l'abréviation 'USB' ?", "o": ["A) Universal Serial Bus", "B) United States Binary", "C) Ultra Speed Battery"], "r": "A"},
        {"q": "Lequel de ces objets est un 'smartphone' ?", "o": ["A) iPhone", "B) Processeur", "C) Clé USB"], "r": "A"},
        # Niveau 2
        {"q": "Quel est le navigateur internet créé par Google ?", "o": ["A) Firefox", "B) Safari", "C) Chrome"], "r": "C"},
        {"q": "Quel raccourci clavier permet de 'Coller' ?", "o": ["A) Ctrl + V", "B) Ctrl + P", "C) Ctrl + Z"], "r": "A"},
        {"q": "Quel système d'exploitation est représenté par un petit robot vert ?", "o": ["A) iOS", "B) Android", "C) Windows"], "r": "B"},
        # Niveau 3
        {"q": "Quelle mémoire s'efface quand on éteint l'ordinateur ?", "o": ["A) HDD", "B) RAM", "C) Carte SD"], "r": "B"},
        {"q": "Où se branchent la plupart des composants ?", "o": ["A) Carte mère", "B) Alimentation", "C) Ventilateur"], "r": "A"},
        {"q": "Combien d'octets y a-t-il dans 1 Kilo-octet (Ko) ?", "o": ["A) 100", "B) 1 000", "C) 1 024"], "r": "C"},
        # Niveau 4
        {"q": "Quel langage est utilisé pour le style d'un site ?", "o": ["A) HTML", "B) CSS", "C) Python"], "r": "B"},
        {"q": "Qu'est-ce qu'une adresse IP ?", "o": ["A) Adresse postale", "B) Identifiant réseau", "C) Mot de passe"], "r": "B"},
        {"q": "En programmation, comment appelle-t-on une erreur dans le code ?", "o": ["A) Virus", "B) Glitch", "C) Bug"], "r": "C"},
        # Niveau 5
        {"q": "Que signifie le 'S' dans 'HTTPS' ?", "o": ["A) System", "B) Secure", "C) Speed"], "r": "B"},
        {"q": "Quel composant gère l'affichage des graphismes 3D ?", "o": ["A) CPU", "B) GPU", "C) BIOS"], "r": "B"},
        {"q": "Quel est le système de numération composé uniquement de 0 et de 1 ?", "o": ["A) Binaire", "B) Hexadécimal", "C) Décimal"], "r": "A"},
    ]

    score = 0
    print("--- BIENVENUE AU QUIZ INFORMATIQUE ---")
    
    for i, item in enumerate(questions):
        # Affichage du niveau tous les 3 points
        if i % 3 == 0:
            print(f"\n--- NIVEAU {(i // 3) + 1} ---")
            
        print(f"\nQuestion {i+1}: {item['q']}")
        for option in item['o']:
            print(option)
            
        reponse = input("Ta réponse (A, B ou C) : ").upper()
        
        if reponse == item['r']:
            print("Bravo ! +1 point.")
            score += 1
        else:
            print(f"Dommage... La bonne réponse était {item['r']}.")

    print(f"\n--- FIN DU JEU ---")
    print(f"Ton score final est de {score}/{len(questions)}")

if __name__ == "__main__":
    lancer_jeu()
