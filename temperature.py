a = input('請輸入溫度:')
b = a.replace('.', '')
 
if a.count('.')>1:
   print('小數點只能有一個')
elif a.startswith('+') or not a[0].isdigit():
     print('只能以數字或是負號開頭')
elif a[0].isdigit():
     print('溫度為:',float(a))
elif a.startswith('-'):
    if not b[1:].isdigit():
        print('無法轉換溫度')
    else:
     print('溫度為:',float(a))

else:
   print('無法轉換溫度')