import os

def compy(message = ""):

    output:str = "...hungry for code..."
    message = str(message)

    # strip the command and trailing whitespaces if any
    code = str(message[6:]).strip()
    if code != "":
        # write the code to file
        fs = open(r"junkpy.py","w+")
        fs.write(code)
        fs.close()
        #execute shell command store the output in var and return
        stream = os.popen('python3 junkpy.py')
        output = stream.read()
        os.system("rm junkpy.py") # remove this line to debug the bot locally

    return output
