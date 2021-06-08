import webbrowser
import time

sometext = "Hi there!"

html_content = f"<html> <head> <h1>{sometext}</h1> </head> <body> </body> </hmtl>"

with open("index.html","w") as html_file:  //creating index.html file with write file permission
    html_file.write(html_content)  
    print("Html file created!")

time.sleep(2);
webbrowser.open_new_tab("index.html")  //to open html file in browser
