《Python编程 从入门到实践》练手总结 
=== 
最近在看《Python编程 从入门到实践》同步更新课后练习进度，在最后把制作的思维导图放出～

  ### 第一部分：
  #### 第六章
  ##### [6-1](section_i/chapter_06/exercise_06_01.py): 
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
  ##### [9-1](section_i/chapter_09/exercise_09_01.py): 
  创建无参数类的时候可以把类的括号去掉`class User:`   
  定义类之后空余两行再执行相关操作  
  ##### [9-7](section_i/chapter_09/exercise_09_07.py):
  继承父类__init__函数时，使用
  `super().__init__()`而不是`super.__init__()`  
  ##### [9-8](section_i/chapter_09/exercise_09_08.py):
  调用类的时候，即使没有参数传入也不可以将括号删去
  ```
        self.privileges = Privileges()
  ```
  #### 第十章
  ##### [10-12](section_i/chapter_10/exercise_10_12.py):
  处理多个异常，可将异常放在元组中
  ```
    try：
        --snip--
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        --snip--
  ```
  #### 第十一章
  ##### [11-1](section_i/chapter_11/exercise_11_01.py):
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
  
---
  ### 第二部分:
  ### 项目源码
  #### [项目1：外星人飞船](section_ii/project_a/alien_invasion):
  PS: conda和pip真是大坑啊, 安装了anaconda3之后，貌似pip命令就默认下载到conda的目录下，而pip3则是默认下载到osx的默认python3目录下……
  ```
  $ pip install pygame
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Requirement already satisfied: pygame in /Users/alessa0/anaconda3/lib/python3.7/site-packages (1.9.4)

  $ pip3 install pygame
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Requirement already satisfied: pygame in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (1.9.4)

  ```
1. ship_speed_factor 设置小数，但是centerx等属性只能接受整数，所以步进应该是1, 2, 1, 2……设置了连续移动所以看不太出来

  ##### [13-4](section_ii/project_a/chapter_13/exercise_13_04.py):
  设置雨滴超出屏幕后新建雨滴对象  
  修改create_fleet函数，当single=True时创建单行对象，single=False时创建多行对象
  [game_functions.py](section_ii/project_a/chapter_13/example_4/game_functions.py):
  ```diff
  + from random import randint
  
  - def create_fleet(rain_settings, screen, rains):
  + def create_fleet(rain_settings, screen, rains, single=False):
    rain = Rain(rain_settings, screen)
    number_rains_x = get_number_rain_x(rain_settings, rain.rect.width)
  + if single:
  +     number_rows = 1
  + else:
        number_rows = get_number_rows(rain_settings, rain.rect.height)

    for number_row in range(number_rows):
        for number_rain in range(number_rains_x):
  +         # 控制雨滴随机生成
  +         random_number = randint(-10, 10)
  +         if random_number > 0:
                create_rain(rain_settings, screen, rains, number_rain,
                            number_row)
  ```
  问题：原本在update_rains(rain_settings, rains)中remove对象后直接使用create_fleet
  (rain_settings, 
  screen, rains, single=True)
  ，但是有一个问题，因为遍历rains是一个过程，remove操作不是同步的，而创建单行对象又不只是创建一个对象，会造成重复  
  解决：在settings中添加一个属性self.rain_create_allowed用于控制新建单行对象操作，具体如下
  
  [game_functions.py](section_ii/project_a/chapter_13/example_4/game_functions.py):
  ```diff
  - def update_rains(rain_settings, rains):
  + def update_rains(rain_settings, screen, rains):
    """更新雨群中所有雨滴的位置"""
    rains.update()
    # 删除消失的雨滴

    for rain in rains.copy():
  +     if rain.rect.top >= rain_settings.screen_height:
            rains.remove(rain)
  +         rain_settings.rain_create_allowed = True
  +     else:
  +         # 防止重复新建雨滴对象
  +         if rain_settings.rain_create_allowed:
  +             create_fleet(rain_settings, screen, rains, single=True)
  +             rain_settings.rain_create_allowed = False
  ```
  [settings.py](section_ii/project_a/chapter_13/example_4/settings.py):
  ```diff
  + # 允许新建雨滴对象（用于超出屏幕范围后删除对象及新建对象）
  +     self.rain_create_allowed = False
  ```
  [exercise_13_04.py](section_ii/project_a/chapter_13/exercise_13_04.py):
  ```diff
      while True:
        gf.check_events()
  -     gf.update_rains(rain_settings, rains)
  +     gf.update_rains(rain_settings, screen, rains)
        gf.update_screen(rain_settings, screen, rains)
  ```
  #### [项目2：数据可视化]():
  #### [项目3：Web应用程序]():
  ###### 持续更新中……