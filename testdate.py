from datetime import datetime

x = datetime.now().strftime("%D-%M-%Y %H:%M:%S")
print(x)
print(str(datetime.now()).split('.',1)[-2])