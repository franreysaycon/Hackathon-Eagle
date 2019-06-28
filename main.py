#!/usr/bin/env python

import eel
import paramiko
import os
from configparser import ConfigParser
from random import Random


@eel.expose
def start(hostname):
	eagle.open(hostname)


@eel.expose
def stop():
	eagle.close()


def send_log_to_user(log):
	# eel.push()
	pass


class Eagle(object):


	def __init__(self, config_filename):
		self.waiting = True
		self.running = False
		self.ssh = None
		self.sftp = None
		self.logs = {}
		# retrieve configuration from external config file
		self.config = ConfigParser()
		self.config.read(os.sep.join([os.getcwd(), config_filename]))
		self.username = self.get_config('username')
		self.domain = self.get_config('flndevdomain')
		self.maxlines = int(self.get_config('maxlines'))
		self.gaflogsdir = self.get_config('gaflogsdir')
		self.thriftlogsdir = self.get_config('thriftlogsdir')
		self.remotetmp = self.get_config('remotetmpdir')
		self.tempfile = os.sep.join([self.remotetmp, 'log'+str(int(Random().random()*1e12))])
		self.localdir = os.sep.join([os.getcwd(), 'logs'])
		if not os.path.exists(self.localdir):
			os.mkdir(self.localdir)


	def __del__(self):
		if self.sftp:
			self.sftp.close()
			self.sftp = None
		if self.ssh:
			self.ssh.close()
			self.ssh = None


	def get_config(self, option):
		if self.config:
			return self.config.get('eagle', option)


	def get_files_info(self, path):
		files_info = {}
		if self.sftp:
			for filename in self.sftp.listdir(path):
				if filename.split('.')[-1] in ['json', 'log', 'error']:
					fullpath = os.sep.join([path, filename])
					filestat = self.sftp.stat(fullpath)
					print filestat.st_mtime, filestat.st_size, fullpath
					files_info[filename] = dict(
						name=filename,
						longname=fullpath,
						date=filestat.st_mtime,
						size=filestat.st_size,
						start=1,
					)
		return files_info


	def get_logs_info(self):
		logs_info = {}
		logs_info.update(self.get_files_info(self.gaflogsdir))
		logs_info.update(self.get_files_info(self.thriftlogsdir))
		return logs_info


	def get_file(self, log_info):
		print log_info
		stdin, stdout, stderr = self.ssh.exec_command(
			'nl %s | tail -n +%d -q | tail -n %d -q > %s' % (
				log_info['longname'], log_info['start'], self.maxlines, self.tempfile
			)
		)
		localfn = os.sep.join([self.localdir, log_info['name']])
		print log_info['longname'], localfn
		def track_get(partial, total):
			print '%d%%' % ((float(partial) / total)*100)
		self.sftp.get(self.tempfile, localfn, track_get)


	def send(self, log_info):
		self.get_file(log_info)
		locallogfile = os.sep.join([self.localdir, log_info['name']])
		send_log_to_user(locallogfile)


	def watch(self):
		# wait for user to start Eagle
		# while self.waiting and not self.running:
		# 	sleep(1000)

		# initially send the all log files
		self.logs = self.get_logs_info()
		for log_name in self.logs:
			self.send(self.logs[log_name])

		# sleep and watch for log changes
		while self.running and not self.waiting:
			sleep(1000);
			logs_info = self.get_logs_info()
			for log_key in logs_info:
				if (
					log_info[log_key]['date'] != self.logs[log_key]['date']
					or
					log_info[log_key]['size'] != self.logs[log_key]['size']
				):
					# the remote file has changed, send the log
					self.send(log)
					# update the cached log info
					self.logs[log_key] = log_info[log_key]

		# watch was stopped, wait for 5 seconds before exiting
		# sleep(5000)


	def open(self, hostname):
		if hostname:
			self.ssh = paramiko.SSHClient()
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.load_system_host_keys()
			self.ssh.connect(
				hostname='.'.join([hostname, self.domain]), username=self.username
			)
			self.sftp = self.ssh.open_sftp()
			self.sftp.chdir(self.gaflogsdir)
			self.sftp.getcwd()
			self.waiting = False
			self.running = True


	def close(self):
		self.running = False


def main():
	print 'Welcome to Eagle!'
	eagle = Eagle('eagle.conf')
	eagle.open('mario-fli')
	# eel.init('src/web')
	# eel.start('index.html', size=(1000, 800))
	eagle.watch()


if __name__ == "__main__":
	main()
