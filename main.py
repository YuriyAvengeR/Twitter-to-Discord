link = input("type your link: ")
#link = "https://x.com/kurolee97/status/1710716731738685728?s=20 https://x.com/kurolee97/status/1710716731738685728?s=20 https://x.com/kurolee97/status/1710716731738685728?s=20 https://x.com/kurolee97/status/1710716731738685728?s=20 https://x.com/kurolee97/status/1710716731738685728?s=20 https://x.com/kurolee97/status/1710716731738685728?s=20"
import time
import pyperclip
extend = "https://vxtwitter."
linkSplit = link.split(" ")
toCopy = []
ind = 1


for i in linkSplit:
    summ = (f"{ind}. {extend}{i[10:]}")
    if ind >= 5:
        ind = 1
    else:
        ind = ind + 1
    toCopy.append(summ)
    print(summ)
else:
    listToStr = '\n'.join([str(elem) for elem in toCopy])
    pyperclip.copy(listToStr)
    print("Done")
    time.sleep(2000)







