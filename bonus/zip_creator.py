import zipfile,pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir,'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath) #create scpecialized instance of the path
            archive.write(filepath, arcname=filepath.name) #extracts only last part of filepath, this is so the full folder structure does not gets zipped

if __name__ == "__main__": #if called directly call function below
    make_archive(filepaths=['bonus/my_list.txt','bonus/my_csv.csv'],dest_dir='bonus/dest')