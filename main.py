import os
import pickle

class SearchEngine: 
    def __init__(self):
        self.file_index = [] #list to store directory index returned by os wal func
        self.results = [] #to store result of each search
        self.matches = 0 #counter for matching files
        self.records = 0 #No of records search till now

    def create_new_index(self,root_path):
        #creates a new index and save to a file when used at startup
        #cretes new index and saves it to a pcikle file 
        #dump the content of file_index in file_index.pkl in write mode
        self.file_index = [ (root,files) for root , dirs , files in os.walk(root_path) if files ]
        with open('file_index,pkl' , 'wb') as f:
            pickle.dump(self.file_index,f)

    def load_existing_index(self):
        #browses the index already created so we don't have to create new one
        #if file index does not exist it returns an error else it reads it in read mode
        try:
            with open('file.index.pkl','rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = []

    def search(self,name,search_type = 'contains'):
        #searcges based on the types name/start_with/end_with
        #resets variable 
        #perform search by changing both in lower case
        #when found do some proper formatting '\ ----> /' and put it in result
        #now export all the results in text file
        self.results.clear()
        self.matches = 0
        self.records = 0

        for path , files in self.file_index:
            for file in files:
                self.records += 1
                if(search_type == 'contains' and name.lower() in file.lower() or
                    search_type == 'startswith' and file.lower().startswith(name.lower()) or
                    search_type == 'endswith' and file.lower().endswith(name.lower())):

                        result = path.replace('\\' , '/') + '/' + file
                        self.results.append(result)
                        self.matches +=1
                else:
                    continue
        
        with open('search_results.txt' , 'w' , encoding="utf-8") as f:
            for row in self.results :
                f.write(row + '\n')

def test1():
    s = SearchEngine()
    check = 'YES'
    while check.upper() != 'NO':
        disk = input("Enter The Disk Name: ")
        s.create_new_index(disk.upper() + ':/')
        FileName = input("Enter The File Name: ")
        s.search(FileName)

        print()
        print('>> There were {:,d} matches out of {:,d} records searched , '.format(s.matches , s.records))
        print()
        print('This Query produced the following matches : \n')
        for match in s.results:
            print(match)
        temp = input('Continue Searching : ')
        check = temp

test1()