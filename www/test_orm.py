#demo.py 可正常执行，供参考

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import logging;logging.basicConfig(level=logging.INFO)
import orm
from models import User

# 建立数据库连接池
async def create_pool():
  await orm.create_pool(loop=loop,host='127.0.0.1', port=3306, user='root', password='123', db='awesome')

# 测试插入一条数据
async def test_insert():
  await create_pool()
  u = User(name='xiaopeng', email='chenhao3@qq.com', passwd='1234567890', image='about:blank')
  await u.save()
  logging.info('tesk save ok')

# 测试查询所有
async def test_selectAll():
  await create_pool()
  users = await User.findAll(orderBy='created_at')
  for user in users:
    logging.info('name : %s ,email : %s' % (user.name,user.email))

# 测试根据id查数据
async def test_selectOne(id):
  await create_pool()
  user = await User.find(id)
  logging.info('name : %s ,email : %s' % (user.name,user.email))

#测试更新语句
async def test_update():
  await create_pool()
  user = await User.find('001484536454715a15d7fe53bad4c39909bbfa08e9a3df8000') # 先根据id查出user，再进行更新
  user.email = 'guest@orm.com'
  await user.update()

#测试删除语句
async def test_delete():
  await create_pool()
  users = await User.findAll(orderBy='created_at', limit=(0, 1))
  for user in users:
      logging.info('delete user: %s' % (user.name))
      await user.remove()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_delete())