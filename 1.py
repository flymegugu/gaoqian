import subprocess

# 执行命令
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# 检查返回码
if result.returncode == 0:
    print("命令执行成功")
    # 输出命令的输出
    print(result.stdout)
else:
    print("命令执行失败，返回码:", result.returncode)
