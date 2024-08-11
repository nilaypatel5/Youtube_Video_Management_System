import mysql.connector


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="youtube_manager"
    )


def list_all_videos(cursor):
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if videos:
        for video in videos:
            print(f"{video[0]}. {video[1]} ({video[2]})")
    else:
        print("No videos found.")


def add_video(cursor, db):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    if name and time:
        cursor.execute("INSERT INTO videos (name, time) VALUES (%s, %s)", (name, time))
        db.commit()
        print("Video added successfully.")
    else:
        print("Both name and time are required.")


def update_video(cursor, db):
    list_all_videos(cursor)
    try:
        video_id = int(input("Enter the ID of the video to update: "))
        new_name = input("Enter new name (press Enter to keep the same): ")
        new_time = input("Enter new time (press Enter to keep the same): ")

        cursor.execute("SELECT * FROM videos WHERE id = %s", (video_id,))
        video = cursor.fetchone()
        if video:
            name = new_name or video[1]
            time = new_time or video[2]
            cursor.execute("UPDATE videos SET name = %s, time = %s WHERE id = %s", (name, time, video_id))
            db.commit()
            print("Video updated successfully.")
        else:
            print("Video not found.")
    except ValueError:
        print("Please enter a valid ID.")


def delete_video(cursor, db):
    list_all_videos(cursor)
    try:
        video_id = int(input("Enter the ID of the video to delete: "))
        cursor.execute("DELETE FROM videos WHERE id = %s", (video_id,))
        db.commit()
        print("Video deleted successfully.")
    except ValueError:
        print("Please enter a valid ID.")


def main():
    db = connect_to_db()
    cursor = db.cursor()

    while True:
        print("\nYouTube Video Management System")
        print("1. List all videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            list_all_videos(cursor)
        elif choice == '2':
            add_video(cursor, db)
        elif choice == '3':
            update_video(cursor, db)
        elif choice == '4':
            delete_video(cursor, db)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
