def process_file():
    try:
        f = open("D:\\Machine Learning\python\Revise\data.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()

    process_file()