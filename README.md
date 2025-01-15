# Programme de Tri Adaptatif

## Description
Ce programme implémente une variante du tri par dénombrement (counting sort) spécialement adaptée pour gérer à la fois des nombres entiers et décimaux.

## Fonctionnement

### Paramètres
- **Entrée** : Liste de nombres (entiers ou décimaux)
- **Sortie** : Liste triée de nombres

### Processus de tri
1. **Phase d'analyse**
   - Détermination des valeurs minimales et maximales
   - Calcul automatique du pas optimal pour les nombres décimaux
   - Comptage des occurrences de chaque nombre

2. **Phase de reconstruction**
   - Création d'un nouveau tableau trié
   - Insertion des nombres en respectant leur fréquence d'apparition

### Caractéristiques
- Gestion intelligente des nombres décimaux
- Préservation des doublons
- Optimisation de la mémoire via un dictionnaire de comptage

## Complexité
- **Temporelle** : O(n + r) 
  - n : taille du tableau
  - r : plage des valeurs ((max - min)/pas)
- **Spatiale** : O(k)
  - k : nombre de valeurs uniques

## Utilisation

```python
from main import sort
Exemple d'utilisation
nombres = [3.14, 1.59, 2.65, 3.14, 1.0]
resultat = sort(nombres)
print(resultat) # Affiche la liste triée
```

### Exemple d'utilisation
```python
nombres = [3.14, 1.59, 2.65, 3.14, 1.0]
resultat = sort(nombres)
print(resultat) # Affiche la liste triée
```

## Points forts
- Efficace pour des distributions de nombres limitées
- Adapté aux nombres décimaux et entiers
- Maintien de la stabilité du tri
- Gestion intelligente des valeurs manquantes
- Optimisation de la mémoire via un dictionnaire de comptage
