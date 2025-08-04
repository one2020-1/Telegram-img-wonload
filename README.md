# Telegram Channel Image Downloader

一个用于批量下载Telegram频道图片的Python工具。

## 功能特性

- 🖼️ 批量下载Telegram频道中的所有图片
- 🌐 支持SOCKS5代理连接
- ⚡ 异步下载，提高下载效率
- 📁 自动创建保存目录
- 🏷️ 按消息ID自动命名图片文件

## 环境要求

- Python 3.7+
- Telethon库
- 有效的Telegram API凭据
- SOCKS5代理（可选，用于网络受限环境）

## 安装依赖

```bash
pip install telethon
```

## 配置说明

### 1. 获取Telegram API凭据

1. 访问 [https://my.telegram.org/](https://my.telegram.org/)
2. 登录你的Telegram账号
3. 点击 "API development tools"
4. 创建新应用，获取 `api_id` 和 `api_hash`

### 2. 配置代码参数

在 `Telegram-img-d.py` 中修改以下参数：

```python
# API凭据
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# 目标频道用户名（不包含@符号）
channel_username = 'TARGET_CHANNEL'

# 代理设置（可选）
proxy = ('socks5', 'PROXY_IP', PROXY_PORT)

# 图片保存路径
save_path = r'YOUR_SAVE_PATH'
```

## 使用方法

1. **克隆或下载项目**
   ```bash
   git clone <repository-url>
   cd tg-img
   ```

2. **安装依赖**
   ```bash
   pip install telethon
   ```

3. **配置参数**
   - 修改 `api_id` 和 `api_hash`
   - 设置目标频道 `channel_username`
   - 调整保存路径 `save_path`

4. **运行脚本**
   ```bash
   python Telegram-img-d.py
   ```

5. **首次运行**
   - 系统会要求输入手机号码
   - 输入收到的验证码完成登录
   - 登录信息会保存在 `session_name.session` 文件中

## 代码结构

```
tg-img/
├── Telegram-img-d.py    # 主程序文件
├── README.md           # 项目说明文档
└── img/               # 图片保存目录（自动创建）
```

## 核心功能

### `download_images_from_channel(channel_username, save_path)`

异步函数，负责：
- 获取指定频道的实体信息
- 遍历频道中的所有消息
- 识别并下载图片类型的消息
- 按消息ID命名保存图片

### 主要特点

- **异步处理**：使用 `async/await` 提高下载效率
- **自动目录创建**：如果保存目录不存在会自动创建
- **代理支持**：支持SOCKS5代理，适用于网络受限环境
- **文件命名**：使用消息ID作为文件名，避免重复和冲突

## 注意事项

⚠️ **重要提醒**

1. **API凭据安全**：不要将API凭据提交到公共代码仓库
2. **频道权限**：确保你有权限访问目标频道
3. **下载限制**：遵守Telegram的API使用限制
4. **存储空间**：确保有足够的磁盘空间存储图片
5. **网络稳定**：建议在稳定的网络环境下运行

## 常见问题

### Q: 如何获取频道用户名？
A: 在Telegram中打开频道，查看频道信息，用户名通常以@开头，使用时去掉@符号。

### Q: 代理是必需的吗？
A: 不是必需的。如果网络环境允许直接访问Telegram，可以将proxy参数设为None。

### Q: 支持哪些图片格式？
A: 支持Telegram支持的所有图片格式，下载时统一保存为.jpg格式。

### Q: 如何下载特定时间范围的图片？
A: 可以修改 `iter_messages()` 方法，添加时间过滤参数。

## 许可证

本项目仅供学习和个人使用。使用时请遵守相关法律法规和Telegram服务条款。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

---

**免责声明**：本工具仅用于合法用途，用户需自行承担使用责任。
