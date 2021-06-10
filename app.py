from flask import Flask
app = Flask(__name__)

def write_to_file():
    file1 = open("mytext.txt","a")
    L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
    # \n is placed to indicate EOL (End of Line)
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close() #Close the file

@app.route("/")
def hello():
    write_to_file()
    return "Hello World!"


if __name__ == "__main__":
   app.run(host='0.0.0.0')