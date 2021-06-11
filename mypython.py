import webbrowser
import time

sometext = "Hi there!"

html_content = f"<html> <head> <h1>{sometext}</h1> </head> <body> </body> </hmtl>" 

with open("index.html","w") as html_file:  
    html_file.write(html_content)  
    print("Html file created!")

time.sleep(4);
webbrowser.open_new_tab("index.html") 
