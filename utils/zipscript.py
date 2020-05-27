from zipfile import ZipFile
import os
import shutil



def zip_text_files(path):

    with ZipFile("texts.zip", 'w') as zipObj:

        for rootdir, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.txt'):
                    filePath = os.path.join(rootdir, file)
                    zipObj.write(filePath)


def text_files(path):
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            yield filename

def dicomZip(zip):
    try:
        if zip == 'zip':
            os.chdir("..")
            os.chdir("..")
            shutil.make_archive('dicoms', 'zip', os.path.join(os.getcwd(), "dicoms"))
    except:
        print("Could not make archive.")



# srcdir = r"C:\Users\alexw\Desktop\ziptest"
# destdir = r"C:\Users\alexw\Desktop\ziptest"
# zip_file_path = os.path.join(destdir, "texts.zip")

# os.chdir(srcdir)  # To work around zipfile limitations

# with ZipFile(zip_file_path, mode='w') as zf:
#     for txt_filename in text_files(srcdir):
#         zf.write(txt_filename)