import os

# Changing a directory to "/home/newdir"
os.chdir("/Users/innuendo/Desktop/udemy-final-downloads")
path = os.getcwd()

# file = open("/Users/innuendo/sillistfiles", 'r')
# lines= file.readlines()

# count=0
# for line in lines:
#     line = line.strip()
#     spl = line.split()
#
#     for s in spl:
#         if s.endswith(".mp4"):
#             count+=1
#             # print(s)
#             s1=s.split("/")
#             print(s1[0]+ "/"+ str(count))
#             renamefile = s1[0]+ "/"+ str(count)
#             os.rename(s, renamefile)

# print(spl[8])

# files = os.listdir(path)
#
# for file in files:
#     startStr=""
#     if len(file) == 1:
#         startStr="00"
#     elif len(file) == 2:
#         startStr="0"
#
#     os.rename(file, startStr + file + ".mp4")

os.chdir("/Users/innuendo/Desktop/udemy-final-downloads/DockerForJavaDevelopers")

file = open("/Users/innuendo/Desktop/python_to_rename/DockerCourseFiles.txt", 'r')
dir = "/Users/innuendo/Desktop/udemy-final-downloads/DockerForJavaDevelopers"
print(os.listdir(dir))
lines = file.readlines()

count = 684
for line in lines:
    print(str(count) + " " + line.strip() + ".mp4")
    os.rename(str(count) + ".mp4", str(count) + " " + line.strip() + ".mp4")
    count += 1
