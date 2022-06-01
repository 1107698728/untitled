#user_list=[{"role": "admin", "account": "admin", "password": "123456", "dept": "tester"},{"role": "user", "account": "dev", "password": "123456", "dept": "tester"}]
from path_normal import absolute_path
def from_file_get_data(file_name):
    f = None        #如果文件没有打开，则无法关闭，给个初始值
    try:
        f=open(file_name,"r")
        line=f.readline()
        user_data=eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if f:#文件非空，打开都是非空
            f.close()
user_list=[]
user_txtdata_path=absolute_path("b.txt")
user_list=user_list if user_list else from_file_get_data(user_txtdata_path)
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

class User():
    def getuser(self,username):
        if result.get("code")==0:
            result.update({"code":0,"message":"用户未登录，无法查询结果："})
            return result
        result.update({"user_list":[]})
        lis=[]
        for user in user_list:
            x=user.get("account")
            if username in x:
                user.pop("password")
                lis.append(user)
        if len(lis):
            result.update({"code":13,"message":"查询用户成功","user_list":lis})
        else:
            result.update({"code": 12})
        return result

    def add_user(self,name,passwd="123456",**kwargs):
        dic={}
        dic["account"]=name
        dic["password"]=passwd
        dic.update(**kwargs)
        user_list.append(dic)
        save_data("b.txt",user_list)
        result.update({"message":"添加用户成功"})

def save_data(file_name,file_content):
    f = None
    try:
        f = open(file_name, "w")
        f.write(str(file_content))
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

if __name__=='__main__':
    # result=from_file_get_data("b.txt")
    # print(result)
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
            user=User()
            print(user.getuser(usr))
            print("=" * 30)
            continue
        if n=="3":
            name=input("请输入新增用户名：")
            user=User()
            get_result=user.getuser(name)
            if 12==get_result.get("code"):
                print("-"*30)
                password=input("请输入用户密码：")
                role=input("请输入用户角色：")
                dept=input("请输入用户部门：")
                user.add_user(name,password,username=role,dept=dept)
            if 13==get_result.get("code"):
                result.update({"code":13,"message":"用户已存在，无法添加"})
                print(result)
            print("="*30)
        if n=="q" or n=="quit":
            flag=False
