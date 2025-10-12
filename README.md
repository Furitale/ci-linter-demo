# CI Linter Demo

这是一个简单的Python项目，演示了CI/CD流程中的代码检查和单元测试。

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行代码检查

```bash
flake8 main.py
```

### 运行单元测试

由于模块导入问题，在Windows PowerShell中使用以下命令运行测试：

```powershell
$env:PYTHONPATH="."; pytest
```

或者在Linux/macOS bash中使用：
```bash
PYTHONPATH=. pytest
```

这会将当前目录添加到Python路径中，使得模块导入能够正常工作。