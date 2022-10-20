#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    
    if values is None:
        values=[]
        # TODO: demander les valeurs ici
        while len(values)<10:
            values.append(input("enter value"))
        nbr_list=[float(value) for value in values if value.isdigit()]
        str_list=[value for value in values if not values.isdigit()]
    return sorted(nbr_list) + sorted(str_list)

def anagrams(words: list = None) -> bool:
    if words is None:
        words=[]
        while len(words)<2:
            words.append(input("Write string"))
        
        if len(words[0])!=len(words[1]):
            return False
        for i in range(len(words[0])):
            if words[0][i] != words[1][len(words[0])-1-i]:
                return False

    return True


def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:


    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
