from distutils.core import setup
import py2exe

setup(
    #tiga parameter dibawah ini bersifat opsional
    version = "0.1.0",
    description = "Contoh penggunaan py2exe",
    name = "sample",
    
    #nama file yang akan dijadikan .exe
    console = ["sample.py"],
)