<p align= "center">
<img src="https://www.unisannio.it/sites/default/files/emblema.png.pagespeed.ce.L9uvAVRynq.png" alt="Unisannio" width= 50%>
</p>
<p align="center">
    Tools utilizzati nel progetto
</p>
<p align="center">
    <img src="https://img.shields.io/badge/Python-v3-blue" alt="Python">
    <img src="https://img.shields.io/badge/Unisannio-Evoluzione%20e%20qualità%20del%20Software-blue" alt="Unisannio">
    <img src = "https://img.shields.io/badge/gitpython-blue">
    <img src = "https://img.shields.io/badge/git-blue">
    <img src = "https://img.shields.io/badge/pandas-blue">
    <img src = "https://img.shields.io/badge/ck%20tools-blue">


# Progetto Evoluzione e qualità del software - Magistrale 2022

Componenti del gruppo:
- Francesco Cosimo Mazzitelli
- Pio Antonio Perugini
- Donato Guerrera
- Ermanno Nicoletti
- Achille Melillo

## Requisiti
Per poter eseguire l'applicazione è necessario:
- Scaricare e installare GIT, Java, Python
- Impostare il percorso relativo  GIT e Java nel path per la definizione delle variabili d'ambiente
- Scaricare ed installare WSL con una distro linux
- Eseguire il comando pip -r requirements.txt che installerà tutte le librerie necessarie al funzionamento dell'applicazione
- Eseguire come amministratore l'eseguibile "GIT bash" e inserire il seguente comando: git config --system core.logpaths true 
- Inserire l'url relativo alla repository da analizzare nel file settings.json:
<p align=center> {
    "repo": "https://github.com/insert/repository/here"
}
</p>

## Descrizione del progetto
Il funzionamento del progetto prevede: 
- Download automatico del repository da analizzare direttamente da GIT
- Estrazione dei commits del repository
- Filtraggio dei commits secondo un determinato criterio
- Checkout dinamico del repository in relazione ai commit filtrati
- Applicazione del tool "ck" per l'estrazione di metriche relative al commit filtrato
- Eliminazione dei file non utili all'elaborazione
- Analisi dei file .csv ottenuti tramite pandas
- Risultati
