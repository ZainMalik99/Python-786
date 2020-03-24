def sort(MyNations20):
    for z in range(len(MyNations20)-1,0,-1):
        for m in range(z):
            if MyNations20[m]>MyNations20[m+1]:
                temporary = MyNations20[m]
                MyNations20[m]= MyNations20[m+1]
                MyNations20[m+1] = temporary

MyNations20 = [9.597000000,17.1000000,242.495,881.913,643.801,8.511000000,357.386,84.421,80.077,147,181]
sort(MyNations20)
print("The sorted nations array from smallest to largest in terms of size is:")
print(MyNations20)
