import compileall


def CompileMe():
    compileall.compile_dir(".", force=True)

if __name__ == '__main__':
    CompileMe()
        
