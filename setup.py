from cx_Freeze import setup, Executable

setup(name = "Compiladores-E02" ,
      version = "1.0.0" ,
      description = "DESCRIPTION" ,
      executables = [Executable("staticchecker.py", base = "Console")]
)
