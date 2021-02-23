import tarfile

file_path = 'C:/Users/ispon/Desktop/pyinstaller-4.2.tar_gz.gz'

tar = tarfile.open(file_path, mode="r:gz")

tar.extractall(path='C:/Users/ispon/Desktop/tmp')

tar.close()
