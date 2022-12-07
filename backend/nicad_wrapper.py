from subprocess import PIPE, STDOUT
import subprocess
import os

absolute_nicad_dir = os.path.abspath('tools/nicad6')
relative_nicad_dir = 'tools/nicad6'
txl_dir = os.path.abspath('tools/txl_linux')
to_analye = os.path.abspath('To_Analyze')

def wsl_open():
    os.system("wsl")

def wsl_exit():
    os.system("exit")

def txl():
    os.chdir(txl_dir)
    #txl = subprocess.Popen('wsl ./InstallTxl', stdout = PIPE, stdin=PIPE, stderr = PIPE, encoding='ascii')
    #output = txl.communicate('y')
    #print(output)
    os.system("wsl ./InstallTxl")

def txl_make():
    os.chdir(txl_dir+"/bin")
    txl = absolute_nicad_dir+"/txl"
    #os.chdir(txl)
    #subprocess.call(['wsl', './txl', 'make', txl])
    #subprocess.call(['wsl', 'make'])
    os.system("wsl ./txl make {}".format(txl))

def type1_clones():
    os.chdir(absolute_nicad_dir)
    #os.system('wsl -e sh -c "./nicad6 functions java {} type1-report default-report"'.format(to_analye))
    subprocess.call(['wsl', './nicad6', 'functions', 'java', to_analye, 'type1-report', 'default-report'])
    #os.system('wsl -e sh -c "ls"')
    #os.system("wsl ls")
    #os.system("wsl chmod +rx nicad.sh")
    #os.system("wsl ./nicad.sh")

def type2_clones():
    os.chdir(nicad_dir)
    subprocess.call(['wsl', './nicad6','functions', 'java', to_analye, 'type2-report', 'default-report'])

def type3_clones():
    os.chdir(nicad_dir)
    subprocess.call(['wsl', './nicad6','functions', 'java', to_analye, 'type3-2-report', 'default-report'])

def generate_clones_metrics():
    type1_clones()
    type2_clones()
    type3_clones()