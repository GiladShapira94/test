import subprocess
subprocess.run(["chmod", "u+x","./test.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
subprocess.call('/User/Varonish/archive/test.sh')

