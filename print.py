# import torch
# import json

# pth_path = "/home/dcx/SimpleClick/weights/pretrained/sbd_config.pth"
# data = torch.load(pth_path, map_location="cpu")

# 过滤掉不能 JSON 序列化的对象
# def filter_non_serializable(obj):
#     if isinstance(obj, torch.Tensor):
#         return obj.tolist()  # 转换 Tensor
#     elif isinstance(obj, dict):
#         return {k: filter_non_serializable(v) for k, v in obj.items()}  # 递归
#     elif isinstance(obj, list):
#         return [filter_non_serializable(v) for v in obj]
#     elif isinstance(obj, (int, float, str, bool)) or obj is None:
#         return obj  # 基本类型保持不变
#     else:
#         return str(obj)  # 其他对象转换为字符串

# json_data = filter_non_serializable(data)

# # 保存 JSON
# json_path = "config.json"
# with open(json_path, "w", encoding="utf-8") as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=4)

# print(f"转换完成，JSON 文件已保存至 {json_path}")
import jtorch

config = jtorch.load("/home/dcx/SimpleClick/weights/pretrained/sbd_config.pth")
model = jtorch.load("/home/dcx/SimpleClick/weights/pretrained/sbd_model.pth")
print(config)
print(model)