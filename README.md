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

## Partie [Youssef Gourar]

## 🎮 Contrôles

| Action | Touche / Méthode |
|--------|------------------|
| Se déplacer | `Z Q S D` ou flèches directionnelles |
| Sauter | `Barre d'espace` |
| Ouvrir une porte | `E` (lorsque le message s'affiche) |
| Interagir avec un quiz / un PNJ | Clic gauche |
| Monter / Descendre d'étage | Cliquer sur les sphères vertes (⬆️) ou bleues (⬇️) |
| Activer le son de fond | Premier clic ou première touche pressée |

### Rez-de-chaussée (Étage 0)
- **Portes fonctionnelles** (ouverture/fermeture avec la touche `E`).
- **Collisions** avec les murs (composant `simple-collision`).
- **Saut** entre les étages (composant `jump-control`).
- Décorations : salon, billard, canapé, plantes, ordinateurs, etc.

### Étage 1 – "Salle Horreur"
- **Ambiance sonore spécifique** : à l'entrée, la musique `horreur.mp3` remplace la musique principale `snk.mp3`.
- **Quiz RAM** : barrette de RAM interactive avec 4 questions. Un son `flop.mp3` retentit en cas d'erreur.
- **PNJ Démon** : affiche une bulle de dialogue au clic.
- **Éléments d'ambiance** : squelettes, zombies, hiboux, cercueil, sang, torches, etc.
- **Portes** accessibles avec l'indicateur "Appuie sur E"

### Fin du jeu (Toit)
- **Message de victoire** : "🎉 BIEN JOUÉ ! VOUS AVEZ RÉUSSI À VOUS ÉCHAPPER ! 🎉"
- **Crédits** : "Projet réalisé par Youssef, Anis, Ruben, Mohamed"
- **Son d'applaudissements** (`applaudissement.mp3`) pendant le feu d'artifice.

### Système audio complet
- **Son d'ascenseur** (`Ding.mp3`) à chaque changement d'étage.
- **Ambiance horreur** (`horreur.mp3`) uniquement à l'étage 1.
- **Son d'erreur quiz** (`flop.mp3`).
- **Applaudissements finaux** (`applaudissement.mp3`).



# Partie ABDOU Elouwahab Anis 

## 📌 Aperçu
Ce projet est une scène 3D interactive développée avec **A-Frame**.  
Le joueur évolue dans un immeuble de plusieurs étages, peut se déplacer librement, monter/descendre les niveaux et relever un défi final sur le toit : ouvrir une trappe secrète pour déclencher le départ de l'hélicoptère et un feu d'artifice de réussite.

---

## 🎥 Ajustements de la caméra

### Problème initial
Par défaut, la caméra d’A-Frame se tournait **derrière** le personnage, rendant la navigation peu intuitive.

### Solution apportée
- Rotation du conteneur `#camera-rig` à `0 180 0` pour orienter correctement la vue vers l’avant.
- Décalage de la caméra sur l’axe Z : `position="0 1.5 -2.5"` afin de placer le regard à hauteur réaliste et dans la bonne direction.

✅ **Résultat** : la caméra regarde désormais naturellement **devant** le joueur, sans nécessiter de réorientation manuelle au démarrage.

---

## 🚁 Décorations du toit & animations

### Hélicoptère et piste d’atterrissage
- Ajout d’un modèle 3D d’hélicoptère (`helico.glb`) positionné sur le toit.
- Ajout d’une piste d’hélicoptère (`heliport_helipad_air_base_helicopter.glb`) pour renforcer le contexte.

### 🎉 Défi “Trappe secrète”
- Une **trappe** (avec couvercle et poignée) est placée sur le toit.
- Le joueur doit **cliquer** sur la poignée ou le couvercle pour l’ouvrir.

### Animation de l’hélicoptère (déclenchée à l’ouverture de la trappe)
1. **Rotation** sur lui-même.
2. **Montée** jusqu’à une certaine hauteur.
3. **Éloignement** vers l’avant et disparition progressive.
4. **Feu d’artifice** en 2D.

### 🎆 Feu d’artifice
- Système de particules personnalisé dessiné sur un `<canvas>`.
- Plusieurs gerbes de couleurs apparaissant aléatoirement à l’écran.
- Effet de traînée, gravité, disparition progressive.

### 🏆 Message de victoire
- Texte scintillant **“BRAVO ! Tu as réussi le défi…”**.
- Animations de rebond et changement de couleur.
- Confettis 3D (`a-particle-system`) visibles quelques secondes.

---

## 🎮 Comment jouer

| Action | Commande |
|--------|----------|
| Se déplacer | `ZQSD` ou `WASD` |
| Regarder autour | Souris |
| Changer d’étage (monter) | Cliquer sur les **sphères vertes** |
| Changer d’étage (descendre) | Cliquer sur les **sphères bleues** |
| Ouvrir la trappe (défi) | Cliquer sur la **poignée** ou le **couvercle** (toit) |

### 🪜 Accès rapide aux étages
- **RDC** : bouton vert (monter) / aucun bouton bleu.
- **Étage 1** : boutons vert (monter) et bleu (descendre).
- **Étage 2** : boutons vert (monter) et bleu (descendre).
- **Toit (étage 3)** : bouton bleu (descendre) + trappe.

---

## 🧱 Technologies utilisées
- [A-Frame 1.5.0](https://aframe.io/) – Framework Web3D / WebVR.
- [A-Frame Physics System](https://github.com/c-frame/aframe-physics-system) – collisions statiques.
- GLTF/GLB – modèles 3D (meubles, hélicoptère, etc.).
- JavaScript natif – logique des téléportations, animations, feu d’artifice.

---

## 📦 Fichiers requis (modèles 3D)

Placez les fichiers `.glb` suivants dans le même dossier que le HTML :

- `Raccoon.glb` (non utilisé directement mais référencé)
- `Door.glb`
- `Computer_Room.glb`
- `lustre.glb`
- `chandelier.glb`
- `table_basse.glb`
- `TV.glb`
- `salon.glb`
- `distributeur.glb`
- `Pot.glb`
- `canape.glb`
- `billard.glb`
- `pouf.glb`
- `Table_bas Glass.glb`
- `pc.glb`
- `chaise.glb`
- `jeux.glb`
- `rack.glb`
- `ac_unit.glb`
- `data_center_rack.glb`
- `Air Conditioner.glb`
- `rack2.glb`
- `red cable 4.glb`
- **`helico.glb`** (hélicoptère)
- **`heliport_helipad_air_base_helicopter.glb`** (piste)

Les textures `puresky.jpg` et `brick.jpg` sont également nécessaires.

---

## 🚀 Lancer le projet

1. Téléchargez tous les fichiers (HTML + modèles + textures).
2. Ouvrez le fichier `.html` dans un navigateur récent (Chrome, Firefox, Edge).
3. Assurez-vous que les fichiers `.glb` sont accessibles (pas de blocage CORS si vous utilisez un serveur local simple).
4. Amusez-vous à explorer l’immeuble et à réussir le défi !

---

## ✨ Améliorations apportées par vos soins

| Élément | Ajustement |
|---------|-------------|
| Caméra | Rotation corrigée pour regarder vers l’avant (au lieu de derrière). |
| Toit | Ajout de l’hélicoptère + héliport. |
| Défi | Trappe cliquable qui déclenche l’animation de l’hélicoptère. |
| Feedback victoire | Message animé, confettis, feu d’artifice 2D. |

---

## 📝 Remarques techniques
- Les collisions sont gérées par `static-body` sur les murs et meubles.
- Le joueur utilise `kinematic-body` pour se déplacer sans tomber.
- Les téléportations entre étages modifient directement la position de `#camera-rig` et réinitialisent la vitesse physique.

---

## 🔊 Ajout du son de l’hélicoptère

Pour une immersion totale, un effet sonore de rotor a été intégré :

### 1. Ajouter le fichier audio dans les `<a-assets>`
(après la ligne `<img id="brick-img" ...>`)
```html
<audio id="heli-sound" src="helicopter-rotor.mp3" preload="auto"></audio>



## Technologies utilisées

- **[A-Frame](https://aframe.io/)** (v1.5.0) – framework web pour la 3D/VR.
- **JavaScript vanilla** – logique des composants personnalisés (collisions, saut, détection de portes, fantôme suiveur, quiz).
- **HTML5 Audio** – gestion des sons et musiques.
- **GLB / glTF** – modèles 3D importés.
