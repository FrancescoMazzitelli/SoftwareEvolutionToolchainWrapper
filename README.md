<p align= "center">
<img src="https://www.unisannio.it/sites/default/files/emblema.png.pagespeed.ce.L9uvAVRynq.png" alt="Unisannio" width= 30%>
</p>
<p align="center">
    Tools utilizzati nel progetto
</p>
<p align="center">
    <img src="https://img.shields.io/badge/Python-v3-blue" alt="Python">
    <img src="https://img.shields.io/badge/Unisannio-Evoluzione%20e%20qualità%20del%20Software-blue" alt="Unisannio">
    <img src = "https://img.shields.io/badge/ck%20tools-blue">
    <img src = "https://img.shields.io/badge/nicad6-blue">
    <img src = "https://img.shields.io/badge/sonarqube-blue">


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
- Eseguire come amministratore l'eseguibile "GIT bash" e inserire il seguente comando: git config --system core.longpaths true 
- Inserire l'url relativo alla repository da analizzare nel file settings .json:
<p align=center> { "repo": "https://github.com/insert/repository/here" } </p>

## Descrizione del progetto
Il funzionamento del progetto prevede: 
- Download automatico del repository da analizzare direttamente da GIT
- Estrazione dei commits del repository
- Filtraggio dei commits secondo un determinato criterio
- Checkout dinamico del repository in relazione ai commit filtrati
- Applicazione del tool "ck" per l'estrazione di metriche relative al commit filtrato
- Eliminazione dei file non utili all'elaborazione
- Analisi dei file .csv ottenuti tramite pandas
- Plot del grafico di tutte le metriche per commit per visualizzare l'andamento delle metriche nel tempo
- Applicazione (semiautomatica) del tool "nicad6" per l'analisi dei cloni
- Estrazione di dati utili dai file .xml risultato e incapsulamento in .csv
- Analisi dei risultati 
- Applicazione del tool "sonarqube" utilizzato per l'analisi del technical debt
- Analisi dei risultati tramite navigazione della pagina html visualizzata
- Risultati

## Analisi dei cloni (semiautomatica)

Non è stato possibile automatizzare l'esecuzione di nicad6, è quindi necessario:
- Installare txl, presente nella cartella "tools"
    - Windows: dall'interno della cartella corrispondente apri il prompt dei comandi e digita "InstallTxl.bat"
    - Linux: dall'interno della cartella corrispondente apri il prompt dei comandi e digita "./InstallTxl" 
- Installare nicad6, presente nella cartella "tools" tramite il comando "make". Verrà quindi avviata la procedura di compilazione dell'eseguibile tramite gcc e txl
- Copiare il progetto da analizzare nella cartella "systems" di nicad
- Avviare il prompt dei comandi dalla cartella "nicad6" e digitare il seguente somando:
    - Tipo1: ./nicad6 functions java systems/To_Analyze type1-report default-report
    - Tipo2: ./nicad6 functions java systems/To_Analyze type2-report default-report
    - Tipo3: ./nicad6 functions java systems/To_Analyze type3-1-report default-report
- Copiare i file "...clones-0.00-classes.xml" nella cartella "nicad_input". Se non è presente crearla manualmente nella root del progetto oppure avviare il nicad_wrapper dal main e farlo fallire per generare automaticamente la cartella

## Documentazione

La documentazione relativa all'applicazione è consultabile sul seguente sito:

[Link to documentation](http://softwareevolution.infinityfreeapp.com)

## Report

Report di progetto

[Link to report](https://issuu.com/ermanno8/docs/evoluzione_e_qualit_del_software)

## Presentazione

Presentazione del pprogetto

[Link to presentation](https://1drv.ms/p/s!Ala06tk1O0saho5jsOURxSuTx-ljvA?e=lMdh6Y)
