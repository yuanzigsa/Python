todos = []

def add_todo():
    """添加待办事项"""
    todo = input("请输入待办事项：")
    todos.append(todo)
    print("已添加待办事项：{}".format(todo))

def view_todos():
    """查看待办事项"""
    if len(todos) == 0:
        print("暂无待办事项。")
    else:
        print("当前待办事项：")
        for i, todo in enumerate(todos, start=1):
            print("{}. {}".format(i, todo))

def remove_todo():
    """删除待办事项"""
    view_todos()
    if len(todos) == 0:
        print("暂无待办事项。")
    else:
        choice = input("请输入要删除的待办事项序号：")
        try:
            choice = int(choice)
            if choice > 0 and choice <= len(todos):
                todo = todos.pop(choice - 1)
                print("已删除待办事项：{}".format(todo))
            else:
                print("无效的序号，请重新输入。")
        except ValueError:
            print("无效的序号，请重新输入。")

def main():
    """主程序"""
    while True:
        print("请选择操作：")
        print("1. 添加待办事项")
        print("2. 查看待办事项")
        print("3. 删除待办事项")
        print("4. 退出")
        choice = input("请输入操作选项（1/2/3/4）：")

        if choice == '1':
            add_todo()
        elif choice == '2':
            view_todos()
        elif choice == '3':
            remove_todo()
        elif choice == '4':
            print("退出待办事项清单应用。")
            break
        else:
            print("错误：无效的选项！请重新选择。")

if __name__ == '__main__':
    main()
