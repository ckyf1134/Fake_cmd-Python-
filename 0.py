print('Microsoft Windows [版本 10.0.19043.1889]')
print('(c) Microsoft Corporation。保留所有权利。')
print(' ')
while 1 == 1:
    input1=input('C:\Windows\System32>')
    if input1 == 'exit':
        break
    elif input1 == 'del c:/*':
        print('Removing......Finish.')
    elif input1 == '':
        input2=input('C:\Windows\System32>')
        if input2 == '':
            1 == 1
        else:
            print("'"+input2+"'"+'不是内部或外部命令，也不是可运行的程序或批处理文件。')
    else:
        print("'"+input1+"'"+'不是内部或外部命令，也不是可运行的程序或批处理文件。')
exit
