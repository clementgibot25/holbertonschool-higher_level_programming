# Python Test Driven Development

## What is an Interactive Test?
An interactive test is a test you can run and observe in real time, often in a terminal or Python shell. It allows you to check the behavior of a function or module by providing concrete usage examples.

## Why are Tests Important?
- They ensure your code works as expected.
- They help prevent bugs and regressions when you modify code.
- They serve as living documentation for users and developers.
- They make code maintenance and refactoring easier.

## How to Write Docstrings to Create Tests
Docstrings are documentation strings placed under the definition of a function or module. They can contain usage examples, called doctests, which Python can automatically test.

Example:
```python
def add(a, b):
    """
    Adds two numbers.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

## How to Write Documentation for Each Module and Function
- **Module**: Add a docstring at the top of the file explaining the general purpose of the module.
- **Function**: Add a docstring below the definition explaining the purpose, arguments, return value, exceptions, and provide examples.

Example:
```python
"""
Simple math module.
Contains addition and subtraction functions.
"""

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int): first number
        b (int): second number
    Returns:
        int: the sum
    """
    return a + b
```

## Basic Option Flags to Create and Run Tests with doctest
- `-v`: verbose mode, shows all tests and their results
- `-m doctest <file.py>`: tests the doctests in the Python file
- `-m doctest <file.txt>`: tests the doctests in a text file

Examples:
```bash
python3 -m doctest -v my_module.py
python3 -m doctest -v tests/my_test.txt
```

## How to Find Edge Cases
- Think about unusual or extreme inputs (0, negative values, very large values, unexpected types)
- Test for expected errors (TypeError, ValueError, etc.)
- Consider cases where arguments are optional or missing
- Check behavior with empty or null data (None, "", [], etc.)

**Tip:**
For each function, ask yourself: "What inputs could break my code?" and write a test for each situation.

---

For more information, see the official documentation:
- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [Python docstrings](https://peps.python.org/pep-0257/)


## Qu’est-ce qu’un test interactif ?
Un test interactif est un test que l’on peut exécuter et observer en temps réel, souvent dans un terminal ou un shell Python. Cela permet de vérifier le comportement d’une fonction ou d’un module en donnant des exemples concrets d’utilisation.

## Pourquoi les tests sont importants ?
- Ils garantissent que le code fonctionne comme prévu.
- Ils préviennent les régressions lors de modifications futures.
- Ils servent de documentation vivante pour les utilisateurs et les développeurs.
- Ils facilitent la maintenance et le refactoring du code.

## Comment écrire des Docstrings pour créer des tests
Les docstrings sont des chaînes de documentation placées sous la définition d’une fonction ou d’un module. Elles peuvent contenir des exemples d’utilisation, appelés doctests, qui seront automatiquement testés par Python.

Exemple :
```python
def add(a, b):
    """
    Additionne deux nombres.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

## Comment écrire la documentation pour chaque module et fonction
- **Module** : Ajouter une docstring en haut du fichier pour expliquer le but général du module.
- **Fonction** : Ajouter une docstring sous la définition pour expliquer le but, les arguments, le retour, les exceptions, et donner des exemples.

Exemple :
```python
"""
Module de calculs mathématiques simples.
Contient des fonctions d’addition et de soustraction.
"""

def add(a, b):
    """
    Additionne deux nombres.

    Args:
        a (int): premier nombre
        b (int): deuxième nombre
    Returns:
        int: la somme
    """
    return a + b
```

## Options de base pour créer et exécuter des tests avec doctest
- `-v` : mode verbeux, affiche tous les tests et leurs résultats
- `-m doctest <fichier.py>` : teste les doctests dans le fichier Python
- `-m doctest <fichier.txt>` : teste les doctests dans un fichier texte

Exemples :
```bash
python3 -m doctest -v mon_module.py
python3 -m doctest -v tests/mon_test.txt
```

## Comment trouver les cas limites (edge cases)
- Penser aux entrées inhabituelles ou extrêmes (0, valeurs négatives, très grandes valeurs, types inattendus)
- Tester les erreurs attendues (TypeError, ValueError, etc.)
- Considérer les cas où les arguments sont optionnels ou manquants
- Vérifier le comportement avec des données vides ou nulles (None, "", [], etc.)

**Astuce :**
Pour chaque fonction, demande-toi : "Quelles entrées pourraient casser mon code ?" et écris un test pour chaque situation.

---

Pour aller plus loin, consulte la documentation officielle :
- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [Python docstrings](https://peps.python.org/pep-0257/)
