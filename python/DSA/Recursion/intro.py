cnt = 0

def check():
    global cnt    
    if cnt == 5:
        return
    print(cnt)
    cnt = cnt + 1
    check()
if __name__ == "__main__":
    check()

