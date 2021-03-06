#no_name 递归函数； 判断b string 是不是 a string里面的一个排列, 返回 True 或者 False；
#utilityFunction 返回s string 里面删除s[j]后的 string 
def compare(a, b):
    try:
        assert isinstance(a, str) and isinstance(b, str)

        if len(a) != len(b):
            info = 'Not Same Length'
            return False, info
        else:
            str_a="".join((lambda x:(x.sort(),x)[1])(list(a)))
            str_b="".join((lambda x:(x.sort(),x)[1])(list(b)))

            if str_a == str_b:
                info = 'Same items, Different String'
                return True, info
            else:
                info = 'Different String'
                return False, info

    except Exception as e:
         return False, e


if __name__ == '__main__':
    # UNITE TESTS

    x = 'asd'
    y = 'dsa'
    result, message = compare(x, y)
    print("Test 1:")
    print(message)
    print()

    x = ''
    y = 'dsa'
    result, message = compare(x, y)
    print("Test 2:")
    print(message)
    print()

    x = 'asdf'
    y = 'qwer'
    result, message = compare(x, y)
    print("Test 3:")
    print(message)
    print()

#MAX Function








...
在以前的开发经历中，你遇到过最大的挑战是什么？有何收获？

    和团队高效配合 和 有效沟通；用新技术测试软件；

    收获：遇到不同的团队和队员，要有弹性地和他们交流，不能一股脑只想着自己的事情，而忽略重点

在你过去共事过的同事/同学里，有没有哪个人是你最想感谢的？为什么？

    去年暑假项目主管， 去年做的是个全栈工程师的实习，技术基础是学过的，但是没有很多和外国客户，还有上司的沟通经验；他很耐心地带领着我们的团队按照
    客户的需求完成多个模块； 他可以站在客户的角度去开发产品，改变了我一直以为的程序员只和电脑打交道的"旧思想"

...


