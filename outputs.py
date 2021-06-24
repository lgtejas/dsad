import os

def write_outputs(results, path='./outputPS3.txt'):
     with open(path, 'w') as f:
          for result in results:
               f.write(result)
               f.write(os.linesep)


