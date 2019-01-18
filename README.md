《Python编程 从入门到实践》练手总结 
=== 
最近在看《Python编程 从入门到实践》同步更新课后练习进度，在最后把制作的思维导图放出～

  ### 第一部分：
  #### 第六章
  ##### [6-1](Section_I/Chapter_06/Exercise_06_01.py): 
  PEP 8 字典缩进方式  
  方法一： 
  ```
  friends = {'first_name': 'ming',
             'last_name': 'xiao',
             'age': '18',
             'city': 'nanjing'}
  ``` 
  方法二：  
  ```
  friends = {
      'first_name': 'ming',
      'last_name': 'xiao',
      'age': '18',
      'city': 'nanjing'
  }
  ```
  或者：
  ```
  friends = {
      'first_name': 'ming',
      'last_name': 'xiao',
      'age': '18',
      'city': 'nanjing'
      }
  ```
  #### 第九章
  ##### [9-1](Section_I/Chapter_09/Exercise_09_01.py): 
  创建无参数类的时候可以把类的括号去掉`class User:`   
  定义类之后空余两行再执行相关操作  
  ##### [9-7](Section_I/Chapter_09/Exercise_09_07.py):
  继承父类__init__函数时，使用
  `super().__init__()`而不是`super.__init__()`  
  ##### [9-8](Section_I/Chapter_09/Exercise_09_08.py):
  调用类的时候，即使没有参数传入也不可以将括号删去
  ```
        self.privileges = Privileges()
  ```
  #### 第十章
  ##### [10-12](Section_I/Chapter_10/Exercise_10_12.py):
  处理多个异常，可将异常放在元组中
  ```
    try：
        --snip--
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        --snip--
  ```
  #### 第十一章
  ##### [11-1](Section_I/Chapter_11/Exercise_11_01.py):
  勘误：
  ```diff
    import unittest
    from HelloWorld.Chapter_11.Example.city_functions import city_country

    class TestCityFunctionsCase(unittest.TestCase):
        """测试city_functions功能"""
        def test_city_country(self):
            result = city_country('Santiago', 'Chile')
            self.assertEqual(result, "Santiago, Chile")

  - unittest.main()
  
  + if __name__ == '__main__':
  +     unittest.main()
  ```
  直接使用`unittest.main()`会报错
  
  ### 第二部分
  
---
  ### 项目源码
  #### [项目1：外星人飞船](Section_II/Project_A/alien_invasion):
  PS: conda和pip真是大坑啊, 安装了anaconda3之后，貌似pip命令就默认下载到conda的目录下，而pip3则是默认下载到osx的默认python3目录下……
  ```
  $ pip install pygame
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Requirement already satisfied: pygame in /Users/alessa0/anaconda3/lib/python3.7/site-packages (1.9.4)

  $ pip3 install pygame
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Requirement already satisfied: pygame in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (1.9.4)

  ```
  #### [项目2：数据可视化]():
  #### [项目3：Web应用程序]():
  ###### 持续更新中……