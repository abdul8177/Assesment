import os

# Function to rename multiple files
i = 0
limit = 6800

for filename in os.listdir('D:\\lfw\\human\\'):
    if i < limit:
        dst = "human" +'.'+ str(i) + '.jpg'
        src = 'D:\\lfw\\human\\' + filename
        dst = 'D:\\lfw\\human\\' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1

for filename in os.listdir('D:\\lfw\\not_human\\'):
    if i < limit:
        dst = "not_human" +'.'+ str(i) + '.jpg'
        src = 'D:\\lfw\\not_human\\' + filename
        dst = 'D:\\lfw\\not_human\\' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1
