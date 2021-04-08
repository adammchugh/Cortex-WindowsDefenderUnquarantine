#!/usr/bin/env python3
# encoding: utf-8

import time
import os
import sys
import struct
import hashlib
from binascii import crc32

from cortexutils.analyzer import Analyzer

class WinDefendUnquarantine(Analyzer):
  def __init__(self):
    Analyzer.__init__(self)
    self.service = self.get_param('config.service', None, 'Service parameter is missing')
    self.polling_interval = self.get_param('config.polling_interval', 60)
    self.proxies = self.get_param('config.proxy', None)
    
  def artifacts(self, raw):
    return [self.build_artifact(self.data_type, self.getData(), tags=["assemblyline"], tlp=self.tlp)]
  
  def run(self):
    if self.data_type not in ['file']:
      self.notSupported()

    # Process with unquarantine decrypt

    time.sleep(self.getParam("config.delay", 60))

    self.report({'data': self.getData(), 'input': self._input})
    
  def summary(self, raw):
    return {'taxonomies': [self.build_taxonomy('info', 'windefendunquarantine', self.data_type, self.getData())]}
  
if __name__ == '__main__':
  WinDefendUnquarantine().run()
