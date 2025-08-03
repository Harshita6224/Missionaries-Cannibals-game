import os
import shutil
import re
import requests
from bs4 import BeautifulSoup


def move_jpg_files(source_folder,target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in os.listdir(source_folder):
        if file.lower().endswith('.jpg'):
            shutil.move(os.path.join(source_folder,file),os.path.join(target_folder,file))
    print(f"Moved .jpg files to {target_folder}")

def extract_emails(input_file,output_file):
    if not os.path.isfile(input_file):
        print(f"The file {input_file} does not exist.")
        return
    
    with open(input_file,'r') as file:
        content=file.read()

    email_pattern=r'[a-zA-Z0-9._%+-] + @[a-zA-Z0-9.-] +\.[a-zA-Z]{2,}'   

    emails=re.findall(email_pattern,content)
    unique_email=set(emails)

    with open(output_file,'w') as file:
        for email in unique_email:
            file.write(email + '\n')

    print(f"Extracted {len(unique_email)} unique email addresses to {output_file}.")

def scrape_page_title(url,output_file):
    try:
       response=requests.get(url)
       response.raise_for_status()

       soup=BeautifulSoup(response.text,'html.parser')
       title=soup.title.string.strip() if soup.title else "No title found"

       with open(output_file,'w') as file:
           file.write(title)
       print(f"Successfully scraped title:'{title}'and saved to {output_file}")

    except Exception as e:
        print(f"Failed to scrape title: {e}")

if __name__=="__main__":
    
    move_jpg_files('source_folder','target_folder')
    extract_emails('input.txt','emails.txt')
    scrape_page_title('https://example.com','webpage_title.txt')