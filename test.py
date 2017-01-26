#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 获取系统的基本信息
import psutil


class SysInfo(object):
	# 获取系统基本信息类
	def __init__(self):
		self.mem = psutil.virtual_memory()
		self.cpu_logical = psutil.cpu_count()
		self.cpu = psutil.cpu_count(logical=False)
		self.cpu_time = psutil.cpu_times()
		self.disk = psutil.disk_partitions()
		self.users = psutil.users()

	def show_mem(self):
		# 输出系统的内存使用情况
		print('-------Memory--------')
		print('Total: %.2f MB' % (self.mem.total/(1024*1024)))
		print('Used: %.2f MB' % (self.mem.used/(1024*1024)))
		print('Free: %.2f MB' % (self.mem.free/(1024*1024)))

	def show_cpu(self):
		# 输出系统的CPU资源
		print('---------CPU---------')
		print('CPU: %d' % self.cpu)
		print('CPU_Logical: %d' % self.cpu_logical)

	def show_cpu_time(self):
		# 输出系统的CPU占用情况
		print('-------CPU Time-------')
		print('user time: %s' % self.cpu_time.user)
		print('system time: %s' % self.cpu_time.system)
		print('idle time: %s' % self.cpu_time.idle)
		print('interrupt time: %s' % self.cpu_time.interrupt)
		# print('user iowait: %s' % self.cpu_time.iowait)

	def show_disk(self):
		# 输出系统的硬盘使用情况
		print('---------Disk--------')
		for disk in self.disk:
			try:
				disk_info = psutil.disk_usage(disk.mountpoint)
				print('%s : { Total: %.2f MB, Used: %.2f MB, Free: %.2f MB, Percent: %.2f%%}'\
				% (disk.mountpoint, (disk_info.total / (1024 * 1024)), (disk_info.used / (1024 * 1024)),\
				(disk_info.free / (1024 * 1024)), disk_info.percent))
			except FileNotFoundError as msg:
				# print(msg)
				pass

	def show_user(self):
		# 输出系统目前的使用用户
		print('---------User--------')
		users = self.users
		for user in users:
			print('username: %s, host: %s' % (user.name, user.host))


a = SysInfo()
a.show_mem()
a.show_cpu()
a.show_cpu_time()
a.show_disk()
a.show_user()
