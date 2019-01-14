《Python编程 从入门到实践》练手总结 
=== 
#第九章
  ##9-1：  
  创建无参数类的时候可以把类的括号去掉`class User:`   
  定义类之后空余两行再执行相关操作  
  ##9-7:  
  继承父类__init__函数时，使用
  `super().__init__()`而不是`super.__init__()`  
  ##9-8:
  大型类拆分成小型类后
  ```
    def __init__(self, first_name, last_name, user_info):
        super().__init__(first_name, last_name, user_info)
        self.privileges = Privileges()
  ```
  类的括号删去后调用相关函数时会出错
#第十章
##10-12：
  处理多个异常，可将异常放在元组中
  ```
    try：
        --snip--
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        --snip--
  ```
 ###持续更新中……