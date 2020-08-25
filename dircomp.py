import os, filecmp, sys

# support both absolute and relative path
if sys.argv[2][0] == '\\' or sys.argv[2][1:3] == ':\\':
    cur = ''
else:
    cur = os.getcwd() + '\\'

os.chdir(sys.argv[1])
filecount = 0

for t in os.walk("."):
    tmp = t[0][2:]      # current walking directory
    #print(f'dir:{t[0]}\n')
    if tmp != '':
         tmp += '\\'

    for f in (t[2]):
        filecount += 1
        fullpath1 = f'{t[0]}\\{f}'
        fullpath2 = f'{cur}{sys.argv[2]}\\{tmp}{f}'    # reconstruct the full-path filename

        #print (t[0], fullpath1, fullpath2)
        if filecmp.cmp(fullpath1, fullpath2, shallow = False):
            print (f'{fullpath2} : identical\n')
        else:
            print (f'{fullpath2} : mismatch. terminated')
            sys.exit()

print(f'All files identical. Total number of files compared : {filecount}')
