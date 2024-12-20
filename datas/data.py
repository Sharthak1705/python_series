from  pymongo import MongoClient
from bson import ObjectId

client = MongoClient("Use your mongodb url")
db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def add_video(name,time):
    video_collection.insert_one({"name":name, "time": time})
def  list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']},Name:{video ['name']} and  Time: {video['time']} ")
def delete_video():
    video_collection.delete_one({"_id": ObjectId(video_id)})
def update_video(video_id,new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})
def main():
    while True:
        print("\n Enter the values which you want: ")
        print("1. List all the videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the application")
        choice = input("Enter ypur choice :")
        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enterthe name of the videos : ")
            time = input(" Enter the time of videos: ")
            add_video(name, time)
        elif choice == '3':
            id = input("Enter the video id to update : ")
            name = input("Enter the name of the videos : ")
            time = input(" Enter the time of videos: ")
            update_video(id , name, time)
        elif choice == '4':
           id = input("Enter the video id for remove the video")
           delete_video(id,name, time)
        elif choice == '5' :
            break
        else :
            print("Invalid choice")

if __name__ == "__main__":
    main()