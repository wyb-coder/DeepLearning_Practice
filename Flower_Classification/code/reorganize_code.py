#!/usr/bin/env python3
"""
脚本用于重组 train_V1.py 的代码结构
"""

import re
from pathlib import Path

# 读取原始文件
source_file = Path(r"d:\Study\CS Study\Code\Python\DeepLearning\DeepLearning_Practice\Flower_Classification\code\train_V1.py")
target_file = Path(r"d:\Study\CS Study\Code\Python\DeepLearning\DeepLearning_Practice\Flower_Classification\code\train_V2.py")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.splitlines()

print(f"原始文件行数: {len(lines)}")

# 定义代码段映射 (起始行, 结束行, 模块名)
# 基于之前查看的文件outline
code_sections = {
    "imports": (1, 51),  # Import部分
    "config": (54, 345),  # Configuration handling
    "distributed": (230, 283),  # Distributed context
    "utils": (357, 641),  # Utility functions
    "transforms": (830, 897),  # Transforms
    "dataset": (648, 733),  # Dataset and sampling
    "losses": (741, 778),  # Losses
    "ema": (786, 823),  # EMA & Early Stopping
    "models": (905, 995),  # Models and heads
    "scheduler": (1020, 1118),  # Scheduler and stages
    "trainer": (1268, 1918),  # Training and evaluation loops
    "main": (1986, 2052),  # Main entry
}

# 创建分隔符函数
def create_separator(title):
    return f"""
# ==================================================================================
#                                {title}
# ==================================================================================
"""

# 提取代码段函数
def extract_lines(start, end):
    return '\n'.join(lines[start-1:end])

# 构建重组后的内容
reorganized_content = []

# 1. Import Modules
reorganized_content.append(create_separator("Import Modules"))
reorganized_content.append(extract_lines(1, 51))

# 2. Configuration  
reorganized_content.append(create_separator("Configuration"))
reorganized_content.append(extract_lines(59, 227))  # DEFAULT_CONFIG
reorganized_content.append(extract_lines(286, 345))  # parse_args, load_config, deep_update

# 3. Distributed Training
reorganized_content.append(create_separator("Distributed Training"))
reorganized_content.append(extract_lines(230, 283))

# 4. Utility Functions
reorganized_content.append(create_separator("Utility Functions"))
reorganized_content.append(extract_lines(357, 641))

# 5. Data Transforms
reorganized_content.append(create_separator("Data Transforms"))
reorganized_content.append(extract_lines(830, 1017))

# 6. Dataset & Samplers
reorganized_content.append(create_separator("Dataset & Samplers"))
reorganized_content.append(extract_lines(648, 733))

# 7. Loss Functions
reorganized_content.append(create_separator("Loss Functions"))
reorganized_content.append(extract_lines(741, 778))

#8. EMA & Early Stopping
reorganized_content.append(create_separator("EMA & Early Stopping"))
reorganized_content.append(extract_lines(786, 823))

# 9. Model Architecture
reorganized_content.append(create_separator("Model Architecture"))
reorganized_content.append(extract_lines(905, 1017))
reorganized_content.append(extract_lines(1126, 1472))

# 10. Optimizer & Scheduler
reorganized_content.append(create_separator("Optimizer & Scheduler"))
reorganized_content.append(extract_lines(1020, 1118))
reorganized_content.append(extract_lines(1887, 1917))

# 11. Training & Evaluation
reorganized_content.append(create_separator("Training & Evaluation"))
reorganized_content.append(extract_lines(1268, 1883))
reorganized_content.append(extract_lines(1920, 1979))

# 12. Main Entry Point
reorganized_content.append(create_separator("Main Entry Point"))
reorganized_content.append(extract_lines(1986, 2052))

# 写入重组后的文件
final_content = '\n'.join(reorganized_content)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"重组完成！新文件: {target_file}")
print(f"新文件行数: {len(final_content.splitlines())}")
