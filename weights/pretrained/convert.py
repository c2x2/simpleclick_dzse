import torch
import json

# 加载 .pth 文件
pth_path = "sbd_config.pth"  # 替换成你的 .pth 文件路径
data = torch.load(pth_path)  # 加载数据

# 如果数据是 Tensor，需要转换为 Python 数据类型
def tensor_to_list(obj):
    if isinstance(obj, torch.Tensor):
        return obj.tolist()  # 转换为列表
    elif isinstance(obj, dict):
        return {k: tensor_to_list(v) for k, v in obj.items()}  # 递归处理字典
    elif isinstance(obj, list):
        return [tensor_to_list(v) for v in obj]  # 递归处理列表
    else:
        return obj  # 其他类型直接返回

print(type(data))
json_data = tensor_to_list(data)

# 保存为 JSON 文件
json_path = "config.json"  # 替换成你想保存的文件名
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print(f"转换完成，JSON 文件已保存至 {json_path}")
