import threading
  
def print_qb(num):
    
    #function to print cube of given num
    
    print("Cube: {}".format(num * num * num))
  
def print_sq(num):
    
    #function to print square of given num
    
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    
    t1 = threading.Thread(target=print_sq, args=(20,))
    t2 = threading.Thread(target=print_qb, args=(20,))
  
    t1.start()
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")