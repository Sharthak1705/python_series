import json
#in json we are using two method that are load and dump

#in json the data which can be read at that time we used load

#in json the data which can be write at that time we used dump

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError: # excepion contain the many method to handle the error 
        return []
    
def save(videos):
    with open('youtube.txt','w') as file:
        return json.dump(videos, file) #in this file we open and write the data

def list_all_videos(videos):
    print("\n")
    # print('*' * 70) it will be print for designining purpose not necessary.
    for index, video in enumerate(videos, start=1):#we used enumerator for the indexing and also the select the specific video 
        print(f"{index}.{video['name']},Duration:{video['time']}")  #in this case we are used the function 
        print('*' * 70)  
def add_video(videos):
    name =input("Enter the video name:")
    time = input("Enter the video time:")
    videos.append({'name':name, 'time':time})
    save(videos)
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number is Update for You : "))
    if 1<=index <=len(videos):  # it is used for the  index start position when using enumerator  and also the lagic area to update the video
        name =input("Enter the video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time':time }
        save(videos)
    else:
        print("invalid index selected")
 
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the value of videos which you want to delete: ")) 
    if 1 <= index <=len(videos): #same as above logic area
        del videos[index-1]
        save(videos)
    else:
        print("Invalid video index selected")

def main(): #this is used for determine the main function
  videos = load_data()
  while True:
    print("\n Youtube Manager :")
    print("1. List all youtube video")
    print("2. Add the youtube video")
    print("3. Update a youtube video details")
    print("4. Delete a youtube video")
    print("5. Exit your video")
    choice = input("Enter your choice:")
    # print(videos)
    match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            delete_video(videos)
        case '5':
            break
        case _:
            print("Invalid choice")
if __name__ ==  "__main__": # dunder keyword
  main()