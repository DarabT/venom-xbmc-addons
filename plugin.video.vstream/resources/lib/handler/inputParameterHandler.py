# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons

import sys

from resources.lib.util import UnquotePlus, Unquote


class cInputParameterHandler:
    def __init__(self):
        aParams = dict()
        try:
            # specific vStreamIO
            import addonPythonScript.Thread_argv as Thread_argv
            argv = Thread_argv.get_custom_argv()
        except ImportError:
            argv = sys.argv

        if len(argv) >= 2 and len(argv[2]) > 0:
            args = argv[2].replace(' & ', ' ')
            aParams = dict(part.split('=') for part in args[1:].split('&'))

        self.__aParams = aParams

    def getAllParameter(self):
        return self.__aParams

    def getValue(self, sParamName):
        if self.exist(sParamName):
            sParamValue = self.__aParams[sParamName]
            if not sParamValue.startswith('http') and not 'url' in sParamName.lower():
                return UnquotePlus(sParamValue)
            else:
                return Unquote(sParamValue)
        return False

    def exist(self, sParamName):
        if sParamName in self.__aParams:
            return sParamName
