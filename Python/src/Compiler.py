import compileall

def CompileMe():
    """ Compiles all python files in the current directory."""
    compileall.compile_dir(".", force=True)

if __name__ == '__main__':
    CompileMe()
        
