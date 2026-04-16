Youssef GOURAR;
Anis ABDOUELOUWAHAB;
Mohamed BEN ABDELJELIL;
Ruben TINANT


## Contexte du projet

Ce projet est un **escape game éducatif en réalité virtuelle** développé avec A-Frame. Le principe : le joueur explore un bâtiment à plusieurs étages, chaque étage étant composé d'une salle d'apprentissage sur l'informatique (CPU, mémoire, etc.) suivie d'une salle dans laquelle un objet est caché. Pour progresser, le joueur doit répondre à un quiz interactif lié aux contenus de la salle.

---

## Partie [Ruben TINANT]

### Construction des étages

J'ai conçu et mis en place l'architecture 3D du bâtiment en entier à l'aide de primitives A-Frame (`<a-box>`). Chaque étage est structuré de manière cohérente avec des salles, des couloirs et des passages. Une attention particulière a été portée à l'agencement pour éviter les bugs de superposition de textures, qui apparaissent quand deux surfaces sont placées exactement au même endroit.

### Étage 2 — contenu complet

Je me suis occupé de l'intégralité de l'étage 2 : le décor, le placement des éléments interactifs, les panneaux d'information sur le CPU (unité de contrôle, ALU, registres, horloge, mémoire cache), ainsi que les interactions et le quiz associé.

### Système de portes

J'ai développé l'animation des portes : lorsque le joueur s'approche d'une porte et appuie sur **E**, celle-ci s'ouvre ou se ferme avec une animation fluide.

### Téléportation entre étages

J'ai mis en place la fonction de téléportation via JavaScript : des sphères cliquables (verte pour monter, bleue pour descendre) permettent au joueur de passer d'un étage à l'autre en repositionnant la caméra à la bonne hauteur.

### Gestion des collisions

J'ai implémenté un composant A-Frame custom (`simple-collision`) qui empêche le joueur de traverser les murs. À chaque frame, le composant détecte les `<a-box>` correspondant à des murs (hauts et fins) et bloque le déplacement si une collision est détectée, en renvoyant le joueur à sa position précédente.

### Aide aux collègues

En dehors de ma partie, j'ai également apporté mon aide à mes collègues en cours de développement, que ce soit pour déboguer leur code ou pour trouver les solutions techniques adaptées à leurs besoins.

### Bande sonore

J'ai participé à la mise en place de la musique de fond du jeu, intégrée via une balise audio HTML.

---

## Difficultés rencontrées

**Agencement du bâtiment** — Placer les murs, sols et plafonds sans provoquer de bugs de texture a demandé beaucoup d'ajustements. Le moindre décalage de position crée des artefacts visuels visibles dans la scène.

**JavaScript** — C'est la partie qui m'a demandé le plus d'efforts. J'ai utilisé du JavaScript pour pas mal de choses : les animations des portes, la téléportation entre étages, le quiz interactif, les interactions en général. Comprendre comment A-Frame gère les positions et les événements prend du temps, surtout quand les éléments sont imbriqués les uns dans les autres. Pour la gestion des collisions, j'ai eu recours à de l'aide extérieure car c'était trop complexe à mettre en place seul.

---

## Technologies utilisées

- [A-Frame](https://aframe.io/) 1.5.0
- JavaScript vanilla
- Modèles 3D au format `.glb`
