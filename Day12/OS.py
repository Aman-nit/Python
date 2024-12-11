import os


# os.getcwd()
# get the current working directory
print(os.getcwd())# Output: Current working directory path

# os.chdir()
# Change the current working directory.
# os.chdir('Day10')
print(dir(os))
print(os.system('mkdir new_folder'))
import subprocess

result = subprocess.run(['ls'], capture_output=True, text=True)
print(result.stdout)


import subprocess

process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout.decode())  # Decodes and prints the command's output
