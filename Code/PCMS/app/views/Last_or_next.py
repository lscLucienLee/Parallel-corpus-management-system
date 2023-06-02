from django.shortcuts import render, redirect
from Code.PCMS.app import models

corpuses = []
index = 0
max_index = 0


def last_or_next(request):
    choice = request.GET.get("choice")
    corpus_name = request.POST.get("corpus_name")
    global index
    global max_index
    # 用户点击的是“上一条”
    if choice == "0":
        if index == 0:
            print(corpuses)
            print(index)
            return render(request, "create_hand.html",
                          {"left": corpuses[index], "right": corpuses[index + 1],
                           "corpus_name": corpus_name})  # 如果是第一条，点击无效
        else:
            # 保存用户输入
            if index == max_index:
                corpuses.insert(index, request.POST.get("left"))
                corpuses.insert(index + 1, request.POST.get("right"))
            else:
                corpuses[index] = request.POST.get("left")
                corpuses[index + 1] = request.POST.get("right")
            index -= 2
            print(corpuses)
            print(index)
            return render(request, "create_hand.html",
                          {"left": corpuses[index], "right": corpuses[index + 1], "corpus_name": corpus_name})
    # 用户点击的是“下一条”
    elif choice == "1":
        left = request.POST.get("left")
        right = request.POST.get("right")
        # 检查语料框是否为空
        if left == "":
            print(corpuses)
            print(index)
            return render(request, "create_hand.html",
                          {"left_null": "左语料为空！", "left": left, "right": right, "corpus_name": corpus_name})
        if right == "":
            print(corpuses)
            print(index)
            return render(request, "create_hand.html",
                          {"right_null": "右语料为空！", "left": left, "right": right, "corpus_name": corpus_name})
        # 保存用户输入
        if index == max_index:
            corpuses.insert(index, request.POST.get("left"))
            corpuses.insert(index + 1, request.POST.get("right"))
        else:
            corpuses[index] = request.POST.get("left")
            corpuses[index + 1] = request.POST.get("right")
        index += 2
        if index > max_index:
            max_index = index
            print(corpuses)
            print(index)
            return render(request, "create_hand.html", {"corpus_name": corpus_name})
        else:
            print(corpuses)
            print(index)
            return render(request, "create_hand.html",
                          {"left": corpuses[index], "right": corpuses[index + 1], "corpus_name": corpus_name})
