import os, time
import tempfile

fh = tempfile.TemporaryFile(mode='w+')
files=[]


def file_size(file_path):
    if os.path.isfile(file_path):
        modTimesinceEpoc = os.path.getmtime(file_path)
        return [os.path.getsize(file_path), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))]


def robo1(path,type):

    for r, d, f in os.walk(path):
        for file in f:

            if type in file:
                files.append(os.path.join(r, file))


    st = ""
    for file in files:
        a, b = file_size(file)
        st += str(b) + "     " + file + "\t" + " "+ "\t"+ str(a) + "\t" + "  " + "\n"
    print(st)
    fh.write(st)


def rootfile():
    fh.seek(0)
    return fh.read()


def dele():
    fh.seek(0)
    fh.truncate(0)
    return fh






