from prettytable import PrettyTable
import os

table = PrettyTable([])

classid = []
nclones = []
nlines = []
similarity = []
refs = []

def check_input():

    """
    Metodo che controlla se esiste la cartella nicad input
    se non esiste la crea
    """
    
    if not os.path.exists("nicad_input"):
        path = os.path.join("nicad_input")
        os.mkdir(path)

def check_output():
    
    """
    Metodo che controlla se esiste la cartella nicad output
    Se non esiste la crea
    """
    
    if not os.path.exists("nicad_output"):
        path = os.path.join("nicad_output")
        os.mkdir(path)

def filter_xml(f):

    """
    Metodo che filtra i valori presenti nel file XML
    generato da nicad e li aggiunge alle liste create prima
    """
    
    class_ = f.getElementsByTagName('class')
    for n in class_:
        tuple = []
        for e in n.getElementsByTagName('source'):
            tuple.append(e.attributes['file'].value)
        refs.append(tuple)
        classid.append(n.attributes['classid'].value)
        nclones.append(n.attributes['nclones'].value)
        nlines.append(n.attributes['nlines'].value)
        similarity.append(n.attributes['similarity'].value)

def create_table():

    """
    Metodo che aggiunge le colonne alla tabella dei risultati
    """
    
    table.add_column('classid', classid)
    table.add_column('nclones', nclones)
    table.add_column('nlines', nlines)
    table.add_column('similarity', similarity)
    table.add_column('code_ref', refs)

def save_to_csv(file):

    """
    Metodo che salva la tabella in un file CSV
    """
    
    with open('nicad_output/nicad-{}.csv'.format(file), 'w') as w:
        w.write(table.get_csv_string())

def xml_wrapper(file, xml_wrapped):
    
    """
    Metodo che definisce il flow of event del modulo e
    che verrà richiamato dal main 
    """

    global classid, nclones, nlines, similarity, refs

    check_input()
    check_output()
    filter_xml(xml_wrapped)
    create_table()
    save_to_csv(file)

    classid.clear()
    nclones.clear()
    nlines.clear()
    similarity.clear()
    refs.clear()