Bonjour !


vous trouver dans le dossier Test Data sciecne les fichier suivant :
    app.py : Api flask qui contient le model et le scaler entrainer 

    best_nba_classifier.pkl : model logistic regression entrainer 

    scaler.pikl :c'est le partie qui assuer la transformation des nouveau données pour 
    que le model entrainer recois les donner comme les donneés que nous avons utiliser pour l'entrainer

    streamlit_app.py:c'est le front fait avec streamlit pour utiliser le model plus simplement pour n'import utilisateur

    test_jupyter:c'est le notebook pour entrainer le model et le scaler !(j'ai utiliser le code de test.py)





pour lancer le test :

1)lancer le app.py dans un powershell ou une terminale Vscode ou un gitbach ...:
  Python app.py 
     app.py c'est le "back-end" c'est l'Api qui recois les donneés et qui envoie les résultat de prédiction vers notre "front-end" streamlit app  

2) lancer le "front-end" dans un power shell ou une terminale Vscode ou un gitbach ...:
   Streamlit run streamlit_app.py

maintenant tu peux régler les donner de perfermonce de jouer pour detecter ou predire c'est il faut le recruter ou non !
