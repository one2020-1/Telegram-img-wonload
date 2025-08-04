from telethon import TelegramClient
import os

# 你的API ID和API Hash
api_id = ''
api_hash = ''
channel_username = 'TG'  #下载目标链接

# 设置socks5代理
proxy = ('socks5', '123.456.789.111', 123)  # 替换为你的代理IP地址和端口号

# 创建客户端实例
client = TelegramClient('session_name', api_id, api_hash, proxy=proxy)

async def download_images_from_channel(channel_username: str, save_path: str):
    # 确保保存图片的目录存在
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 获取频道实体
    channel = await client.get_entity(channel_username)

    # 遍历频道中的所有消息
    async for message in client.iter_messages(channel):
        if message.photo:
            # 下载图片
            file_path = os.path.join(save_path, f'{message.id}.jpg')
            await message.download_media(file=file_path)
            print(f'Downloaded image: {file_path}')

async def main():
    # 指定保存图片的路径
    save_path = r'C:\dwonload'
    await download_images_from_channel(channel_username, save_path)

# 运行客户端
with client:
    client.loop.run_until_complete(main())
