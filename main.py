# Error Handling and Exceptions
    # FileNotFound 
    # KeyError
    # IndexError
    # Type Error
# Raising your own errors
# NATO phonetic decription exercise
# JSON file format
    #json.dump(data, data_storage, indent=4-readibility) -  to write
    #json.load(file_path(data_storage)) to read
    #json.update()



def try_excepttion():
        
    try: # There should be a condition 
        file = open("newfile.txt")
        a_dictionary = {"key": "value"}
        print(a_dictionary["keys"])
    except FileNotFoundError: #In case of condition not working
        file = open("newfile.txt", "w")
        file.write("Something new")
        print("FIle no found error cought")
    except KeyError as error: # In the case of condition not working catching the error with veriable
        print(f" The key {error } not found")
    else: # In case of condition working
        content = file.read()   
        print(content)
    finally: # Doesn`t matter what this will be executed
        file.close()

height = float(input("Height: "))
weight = float(input("Weight: "))

if height >3:
    raise ValueError("Human height cannot exceed 3 meters.")




