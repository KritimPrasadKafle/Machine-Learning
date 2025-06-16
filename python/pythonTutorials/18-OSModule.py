import os
print(os.getcwd())

os.chdir('/home/kritim/Desktop/')
print(os.getcwd())

print(os.listdir())

# os.mkdir('OS-Demo-2/Sub-Dir-1')
# os.makedirs('OS-Demo-2/Sub-Dir-1')

# os.rmdir('OS-Demo-2/Sub-Dir-1')
# os.removedirs('OS-Demo-2/Sub-Dir-1')

# os.makedirs('test.txt')
# os.rename('test.txt', 'demo.txt')

print(os.stat('demo.txt'))

# print(os.stat('demo.txt').st_mtime)

for dirpath, dirnames, filenames in os.walk('/home/kritim/Desktop/'):
    print('Current Path:', dirpath)
    print('Directories:',dirnames)
    print('Files:', filenames)
    print()
# print(os.walk())
print(os.listdir())

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)


print(os.path.exists('/tmp/test.txt'))