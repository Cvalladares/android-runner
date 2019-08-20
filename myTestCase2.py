#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2018  Diego Torres Milano
Created on 2019-08-02 by Culebra v15.8.0
                      __    __    __    __
                     /  \  /  \  /  \  /  \ 
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \ 
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
"""


import re
import sys
import os


import unittest

from com.dtmilano.android.viewclient import ViewClient, CulebraTestCase

TAG = 'CULEBRA'


class CulebraTests(CulebraTestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'debug': {}, 'startviewserver': True, 'compresseddump': True}
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.4, 'find-views-with-content-description': True, 'window': -1, 'orientation-locked': None, 'concertina-config': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': False, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'install-apk': None, 'drop-shadow': False, 'output': 'myTestCase2.py', 'unit-test-method': None, 'interactive': False}
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

        self.vc.dump(window=-1)

        no_id1 = self.vc.findViewByIdOrRaise("id/no_id/1")
        com_google_android_googlequicksearchbox___id_workspace = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/workspace")
        no_id3 = self.vc.findViewByIdOrRaise("id/no_id/3")
        no_id3 = self.vc.findViewWithTextOrRaise(u'Play Store')
        no_id3 = self.vc.findViewWithContentDescriptionOrRaise(u'''Play Store''')
        com_google_android_googlequicksearchbox___id_qsb_widget = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/qsb_widget")
        com_google_android_googlequicksearchbox___id_qsb_widget = self.vc.findViewWithContentDescriptionOrRaise(u'''Google''')
        com_google_android_googlequicksearchbox___id_search_widget_google_logo = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/search_widget_google_logo")
        com_google_android_googlequicksearchbox___id_search_widget_google_logo = self.vc.findViewWithContentDescriptionOrRaise(u'''Go to Discover''')
        com_google_android_googlequicksearchbox___id_search_edit_frame = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/search_edit_frame")
        com_google_android_googlequicksearchbox___id_search_edit_frame = self.vc.findViewWithContentDescriptionOrRaise(u'''Google Search''')
        com_google_android_googlequicksearchbox___id_search_widget_voice_hint = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/search_widget_voice_hint")
        com_google_android_googlequicksearchbox___id_search_widget_voice_hint = self.vc.findViewWithTextOrRaise(u'Say "Ok Google"')
        com_google_android_googlequicksearchbox___id_search_widget_voice_btn = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/search_widget_voice_btn")
        com_google_android_googlequicksearchbox___id_search_widget_voice_btn = self.vc.findViewWithContentDescriptionOrRaise(u'''Voice Search''')
        com_google_android_googlequicksearchbox___id_page_indicator = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/page_indicator")
        com_google_android_googlequicksearchbox___id_page_indicator = self.vc.findViewWithContentDescriptionOrRaise(u'''Home screen 2 of 2, Settings''')
        com_google_android_googlequicksearchbox___id_layout = self.vc.findViewByIdOrRaise("com.google.android.googlequicksearchbox:id/layout")
        no_id11 = self.vc.findViewByIdOrRaise("id/no_id/11")
        no_id11 = self.vc.findViewWithTextOrRaise(u'Messages')
        no_id11 = self.vc.findViewWithContentDescriptionOrRaise(u'''Messages''')
        no_id12 = self.vc.findViewByIdOrRaise("id/no_id/12")
        no_id12 = self.vc.findViewWithContentDescriptionOrRaise(u'''Apps''')
        no_id13 = self.vc.findViewByIdOrRaise("id/no_id/13")
        no_id13 = self.vc.findViewWithTextOrRaise(u'Chrome')
        no_id13 = self.vc.findViewWithContentDescriptionOrRaise(u'''Chrome''')
        no_id14 = self.vc.findViewByIdOrRaise("id/no_id/14")
        no_id14 = self.vc.findViewWithTextOrRaise(u'Camera')
        no_id14 = self.vc.findViewWithContentDescriptionOrRaise(u'''Camera''')



if __name__ == '__main__':
    CulebraTests.main()

