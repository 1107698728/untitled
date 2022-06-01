#user_list=[{"role": "admin", "account": "admin", "password": "123456", "dept": "tester"},{"role": "user", "account": "dev", "password": "123456", "dept": "tester"}]
user_list=[]
user_list=user_list if user_list else from_file_get_data("a.txt")
result={"code":0,"message":""}
def login(username,passwd):
    if username is None and username != "":
        result.update({"code":0,"message":"用户名不能为空"})
        return result
    if passwd is None and passwd != "":
        result.update({"code": 0, "message": "密码不能为空"})
        return result
    for user_info in user_list:
        if username==user_info.get("account") and passwd==user_info.get("password"):
            result.update({"code":1,"message":"登录成功","user_list":user_list})
            return result
    result.update({"code":0,"message":"请检查用户名或密码是否正确"})
    return result

def getuser(username):
    if result.get("code")!=1:
        result.update({"code":11,"message":"无权限：，请先登录："})
        return result
    result.update({"user_list":[]})
    lis=[]
    for x in user_list:
        account=x.get("account")
        if username in account:
            x.pop("password")
            lis.append(x)
    if len(lis):
        result.update({"message":"查询用户成功","user_list":lis})
        return result
    pass

def add_user(account,passwd="123456",**kwargs):
    dic={}
    dic["account"]=account
    dic["password"]=passwd
    dic.update(**kwargs)
    user_list.append(dic)
    file_save("a.txt",user_list)

def from_file_get_data(file_name):
    f = None
    try:
        f=open(file_name,"r")
        line=f.readline()
        user_data=eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()

def file_save(file_name,file_path):
    f = None
    try:
        f = open(file_name, "a")
        f.write(str(file_name))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


if __name__=='__main__':
    result=from_file_get_data("a.txt","r")
    print(result)
    flag=True
    while flag:
        n=input("输入请输入对应的操作："
                "\n 1:)进行登录："
                "\n 2:)进行查询："
                "\n 3:)添加用户："
                "\n q:)退出操作："
                "\n 其他字符:)未知操作，请重新输入：")
        if n not in ("1","2","3","q"):
            print("="*30)
            continue
        if n=="1":
            usr=input("请输入用户名：")
            pwd=input("请输入密码")
            print(login(usr,pwd))
            print("=" * 30)
            continue
        if n=="2":
            usr = input("请输入用户名：")
            print(getuser(usr))
            print("=" * 30)
            continue
        if n=="3":
            username=input("请输入新增用户名：")
            if getuser(username):
                result.update({"code":13,"message":"用户已存在"})
            passwd=input("请输入用户密码：")
            account=input("请输入用户账户：")
            dept=input("请输入用户部门：")
            add_user(account,passwd,username=username,dept=dept)
        if n=="q" or n=="quit":
            flag=False
