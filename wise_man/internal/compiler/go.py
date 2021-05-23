import os

def comgo(message = ""):
    output:str = "...hungry for code..."
    message = str(message)

    # strip the command and trailing whitespaces if any
    code = str(message[6:]).strip()
    if code != "":
        # write the code to file
        fs = open(r"junkgo.go","w+")
        fs.write(code)
        fs.close()
        os.system('go fmt junkgo.go')
        #execute shell command store the output in var and return
        stream = os.popen('go run junkgo.go')
        output = stream.read()
        os.system("rm junkgo.go") # remove this line to debug the bot locally

    return output

