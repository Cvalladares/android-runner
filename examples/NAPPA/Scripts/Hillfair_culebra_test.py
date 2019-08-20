#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (C) 2013-2018  Diego Torres Milano
Created on 2019-08-02 by CulebraTester 
                      __    __    __    __
                     /  \  /  \  /  \  /  \ 
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \ 
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
'''


import re
import sys
import os


import unittest
try:
    sys.path.insert(0, os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

import pkg_resources
pkg_resources.require('androidviewclient>=12.4.0')
from com.dtmilano.android.viewclient import ViewClient, CulebraTestCase
from com.dtmilano.android.uiautomator.uiautomatorhelper import UiAutomatorHelper, UiScrollable, UiObject, UiObject2

TAG = 'CULEBRA'


class CulebraTests(CulebraTestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': True, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 1, 'find-views-with-content-description': True, 'window': -1, 'orientation-locked': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': True, 'verbose-comments': False, 'gui': False, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'install-apk': None, 'drop-shadow': False, 'output': None, 'unit-test-method': None, 'interactive': False}
        cls.sleep = 5

    def setUp(self):
        super(CulebraTests, self).setUp()

    def tearDown(self):
        super(CulebraTests, self).tearDown()

    def preconditions(self):
        if not super(CulebraTests, self).preconditions():
            return False
        return True

    def testSomething(self):
        if not self.preconditions():
            self.fail('Preconditions failed')

        _s = CulebraTests.sleep
        _v = CulebraTests.verbose

        self.vc.click(x=303, y=1288)
        self.vc.sleep(_s)
        self.vc.click(x=807, y=440)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=728, y=1353)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.findObject(bySelector='desc@Navigate up,clazz@android.widget.ImageButton,text@$,package@appteam.nith.hillffair').clickAndWait(eventCondition='until:newWindow', timeout=_s*1000)
        self.vc.click(x=944, y=1141)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.findObject(bySelector='res@appteam.nith.hillffair:id/leaderboard_link,clazz@android.widget.Button,text@LEADERBOARD,package@appteam.nith.hillffair').clickAndWait(eventCondition='until:newWindow', timeout=_s*1000)
        self.vc.uiAutomatorHelper.findObject(bySelector='desc@Navigate up,clazz@android.widget.ImageButton,text@$,package@appteam.nith.hillffair').clickAndWait(eventCondition='until:newWindow', timeout=_s*1000)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=459, y=2296)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=1061, y=2259)
        self.vc.sleep(_s)
        self.vc.click(x=387, y=701)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=424, y=1300)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=1053, y=1997)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.swipe(start=(587, 2281), end=(580, 864), steps=25)
        self.vc.sleep(_s)
        self.vc.click(x=925, y=2190)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=341, y=1599)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=387, y=909)
        self.vc.sleep(_s)
        self.vc.uiAutomatorHelper.pressBack()
        self.vc.sleep(_s)
        self.vc.click(x=1061, y=1573)
        self.vc.sleep(_s)
        self.vc.click(x=1091, y=2243)
        self.vc.sleep(_s)


if __name__ == '__main__':
    CulebraTests.main()
