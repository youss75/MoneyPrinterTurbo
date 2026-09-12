# Novelbeat — démarrage sans Docker

Ce dossier prépare MoneyPrinterTurbo pour assembler des scènes vidéo et une voix hindi.
Le dépôt GitHub contient le programme ; il faut le lancer sur un ordinateur ou un serveur.
Il ne fournit pas un service vidéo déjà hébergé.

## Lancer sur macOS ou Linux

Installer Git et [uv](https://docs.astral.sh/uv/getting-started/installation/), puis :

```sh
git clone https://github.com/youss75/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo
sh novelbeat/start.sh
```

Si le dépôt est déjà téléchargé, faire `git pull --ff-only` dans son dossier, puis lancer
`sh novelbeat/start.sh`. Ouvrir l'adresse locale affichée, généralement
http://127.0.0.1:8501. La première installation télécharge Python 3.11 et les dépendances
verrouillées par le projet ; elle nécessite Internet et peut prendre plusieurs minutes.

Le lanceur crée `config.toml` uniquement s'il n'existe pas. Il conserve toute configuration
existante. Les préférences initiales sont : interface anglaise, médias locaux, format 9:16,
ordre séquentiel, vitesse normale, voix hindi Swara, sans musique ni sous-titres.
Pour une installation existante, sélectionner ces options dans l'interface.
La voix masculine alternative est `hi-IN-MadhurNeural-Male`.

## Importer les scènes Higgsfield et créer un teaser

1. Générer et vérifier les véritables scènes animées dans Higgsfield, puis télécharger leurs MP4.
   Aucun appel automatique à Higgsfield n'est ajouté ici.
2. Dans MoneyPrinterTurbo, sélectionner les médias locaux et importer les scènes dans l'ordre.
   Fournir le texte hindi exact dans le champ du script, puis sélectionner la voix Swara.
3. Lancer le montage et vérifier le résultat : mouvement des personnages, voix intelligible,
   ordre des scènes et absence de répétition involontaire.

Pour utiliser le modèle en ligne de commande :

```sh
mkdir -p storage/novelbeat
# Déposer scene-01.mp4, scene-02.mp4 et scene-03.mp4 dans ce dossier.
# Adapter le texte dans novelbeat/teaser.example.json.
uv run python cli.py --batch-file novelbeat/teaser.example.json --stop-at video
```

Le texte du modèle est un exemple promotionnel générique, pas une adaptation validée du roman.
Les chemins sont relatifs au fichier JSON. Les trois MP4 doivent exister avant le lancement.
Le résultat et les chemins des fichiers sont indiqués par la CLI ; les tâches sont stockées
dans `storage/tasks`. Les vidéos restent locales, elles ne sont pas publiées sur GitHub.

La durée finale dépend de la narration. MoneyPrinterTurbo peut répéter les plans lorsque
la durée des images ne couvre pas la voix : prévoir suffisamment de scènes différentes.
Le réglage de 8 secondes est une durée de découpe des plans, pas la durée totale du teaser.
Importer un MP4 qui contient une photo figée ne crée pas de mouvement de personnage.

## Voix et sous-titres

La voix Edge TTS nécessite Internet et envoie le script au service de synthèse vocale.
Le modèle fourni utilise un script écrit et des médias locaux : aucune clé de génération
de texte ou de banque vidéo n'est nécessaire. La disponibilité de la voix reste liée au service.

Les sous-titres sont désactivés au départ pour éviter une police incompatible avec le hindi.
Pour les activer, installer une police Devanagari dans `resource/fonts`, la sélectionner
dans l'interface et vérifier visuellement les caractères et la synchronisation.
Pour une narration déjà enregistrée, renseigner `custom_audio_file` dans le manifeste :
elle remplace la synthèse vocale. Les sous-titres de cet audio nécessitent le fournisseur
Whisper dans `config.toml`, avec téléchargement de son modèle au premier usage.

Conserver les clés dans le `config.toml` local ignoré par Git. Le lanceur ne remplace pas
les clés existantes et ne déploie aucun service public.

## Validation

Le modèle est vérifié contre les champs de `VideoParams` et le créateur de configuration
est testé pour préserver un fichier existant. Le lancement complet et le rendu sur la machine
de destination restent à vérifier après installation des dépendances et ajout des MP4.
