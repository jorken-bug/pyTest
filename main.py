# This is a sample Python script.
import os

import pytest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    pytest.main()
    os.system("allure serve ./temps -o ./reports --clean")  #生成allure报告并打开
    #generate
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
