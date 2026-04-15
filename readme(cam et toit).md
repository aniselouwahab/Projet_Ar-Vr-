# Escape Building – Défi du toit

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

