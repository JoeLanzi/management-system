import os
import time

import cv2
import pandas as pd
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from facial_recognition import facial_recognition as fr
from gdatabase import get_info, get_occ
from gsheets_extract import extract_occupancy, extract_temperature


class MyHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        print(f'\n[INFO] event type: {event.event_type}  path: {event.src_path}')
        print ("[INFO] processing data . . .")
        
        # if image jpg or png run facial recognition
        if (os.path.splitext(event.src_path)[-1].lower() == ".jpg" or os.path.splitext(event.src_path)[-1].lower() == ".png"):
            # Auto handler for csv
            extract_temperature()
            extract_occupancy()

            fc_image, name = fr("encodings.pickle",event.src_path,"hog")
            #os.remove(event.src_path)
            info,id = get_info(name)
            cv2.imwrite(r"C:/inetpub/wwwroot/images/"+id+".jpg",fc_image )
            get_occ()

            print ("[INFO] updating database . . .")
            # Save data to database
            try:
                database = pd.read_csv(r"C:/inetpub/wwwroot/database.csv")
            except pd.errors.EmptyDataError:
                info.index = info.index + 1
                info.to_csv(r'C:/inetpub/wwwroot/database.csv')
            else:
                data = pd.concat([database.loc[:, database.columns != 'Unnamed: 0'],info], ignore_index=True)
                data.index = data.index + 1
                data.to_csv(r'C:/inetpub/wwwroot/database.csv')
            print ("[INFO] Done")


def main():

    print ("[INFO] File Handler Running...")

    observer = Observer()
    event_handler = MyHandler() # create event handler
    observer.schedule(event_handler, path='../Capstone Data') # set observer to use created handler in image temp directory
    observer.start()

    # threding until exception keyboard interrupt [Ctrl + C]
    # then stop + rejoin the observer
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

#arguments
if __name__ == '__main__':
    main()
    wait = input()